# Copyright (C) 2019 Analog Devices, Inc.
#
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without modification,
# are permitted provided that the following conditions are met:
#     - Redistributions of source code must retain the above copyright
#       notice, this list of conditions and the following disclaimer.
#     - Redistributions in binary form must reproduce the above copyright
#       notice, this list of conditions and the following disclaimer in
#       the documentation and/or other materials provided with the
#       distribution.
#     - Neither the name of Analog Devices, Inc. nor the names of its
#       contributors may be used to endorse or promote products derived
#       from this software without specific prior written permission.
#     - The use of this software may or may not infringe the patent rights
#       of one or more patent holders.  This license does not release you
#       from the requirement that you obtain separate licenses from these
#       patent holders to use this software.
#     - Use of the software either in source or binary form, must be run
#       on or directly connected to an Analog Devices Inc. component.
#
# THIS SOFTWARE IS PROVIDED BY ANALOG DEVICES "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES,
# INCLUDING, BUT NOT LIMITED TO, NON-INFRINGEMENT, MERCHANTABILITY AND FITNESS FOR A
# PARTICULAR PURPOSE ARE DISCLAIMED.
#
# IN NO EVENT SHALL ANALOG DEVICES BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
# EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, INTELLECTUAL PROPERTY
# RIGHTS, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR
# BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT,
# STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF
# THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

import time

import adi
import matplotlib.pyplot as plt
from scipy import signal
from argparse import ArgumentParser
import numpy as np

def spectrogram_test():
    sample_rate = 1e6

    # Generate tone plus noise
    t = np.arange(1024*1000)/sample_rate # time vector
    f = 50e3 # freq of tone
    x = np.sin(2*np.pi*f*t) + 0.2*np.random.randn(len(t))
    plt.figure(0)
    plt.xlabel("Time [s]")
    plt.ylabel("Signal Value")
    plt.plot(t[0:1024], x[0:1024],'.-')

    fft_size = 1024
    num_rows = len(x) // fft_size # // is an integer division which rounds down
    spectrogram = np.zeros((num_rows, fft_size))
    for i in range(num_rows):
        spectrogram[i,:] = 10*np.log10(np.abs(np.fft.fftshift(np.fft.fft(x[i*fft_size:(i+1)*fft_size])))**2)
    plt.figure(1)
    plt.imshow(spectrogram, aspect='auto', extent = [sample_rate/-2/1e6, sample_rate/2/1e6, 0, len(x)/sample_rate])
    plt.xlabel("Frequency [MHz]")
    plt.ylabel("Time [s]")
    plt.show()
    print('done')

def psd_test():
    #Power Spectral Density (PSD)
    Fs = 1e6 # lets say we sampled at 1 MHz
    # assume x contains your array of IQ samples
    N = 1024
    x = x[0:N] # we will only take the FFT of the first 1024 samples
    x = x * np.hamming(len(x)) # apply a Hamming window
    PSD = np.abs(np.fft.fft(x))**2 / (N*Fs)
    PSD_log = 10.0*np.log10(PSD)
    PSD_shifted = np.fft.fftshift(PSD_log)

    center_freq = 2.4e9 # frequency we tuned our SDR to
    f = np.arange(Fs/-2.0, Fs/2.0, Fs/N) # start, stop, step.  centered around 0 Hz
    f += center_freq # now add center frequency
    plt.plot(f, PSD_shifted)
    plt.show()


def DDStest(sdr):
    # Configure properties
    sdr.rx_enabled_channels = [0, 1]
    sdr.tx_enabled_channels = [0, 1]
    sdr.trx_lo = 2000000000
    sdr.tx_cyclic_buffer = True
    sdr.tx_hardwaregain_chan0 = -10
    sdr.tx_hardwaregain_chan1 = -10
    print(sdr.tx_hardwaregain_chan0)
    print(sdr.tx_hardwaregain_chan1)
    sdr.gain_control_mode_chan0 = "slow_attack" #"fast_attack"
    sdr.gain_control_mode_chan1 = "slow_attack"

    # Read properties
    print("TRX LO %s" % (sdr.trx_lo))

    # Send data
    sdr.dds_enabled = [1, 1, 1, 1, 1, 1, 1, 1]
    sdr.dds_frequencies = [2000000, 0, 2000000, 0, 2000000, 0, 2000000, 0]
    sdr.dds_scales = [1, 0, 1, 0, 1, 0, 1, 0]
    sdr.dds_phases = [0, 0, 90000, 0, 0, 0, 90000, 0]


    # Collect data
    fsr = int(sdr.rx_sample_rate)
    for r in range(20):
        x = sdr.rx()
        f, Pxx_den = signal.periodogram(x[0], fsr)
        f2, Pxx_den2 = signal.periodogram(x[1], fsr)
        plt.clf()
        plt.semilogy(f, Pxx_den)
        plt.semilogy(f2, Pxx_den2)
        plt.ylim([1e-7, 1e4])
        plt.xlabel("frequency [Hz]")
        plt.ylabel("PSD [V**2/Hz]")
        plt.draw()
        plt.pause(0.05)
        time.sleep(0.1)

    plt.show()

def txtest(sdr):
    #generate a sinusoid at +100 kHz, then transmit the complex signal at a carrier frequency of 915 MHz, 
    # causing the receiver to see a carrier at 915.1 MHz.
    sample_rate = 1e6 # Hz
    center_freq = 915e6 # Hz

    sdr.sample_rate = int(sample_rate)
    sdr.tx_rf_bandwidth = int(sample_rate) # filter cutoff, just set it to the same as sample rate
    sdr.tx_lo = int(center_freq)
    sdr.tx_hardwaregain_chan0 = -50 # Increase to increase tx power, valid range is -90 to 0 dB

    N = 10000 # number of samples to transmit at once
    t = np.arange(N)/sample_rate
    samples = 0.5*np.exp(2.0j*np.pi*100e3*t) # Simulate a sinusoid of 100 kHz, so it should show up at 915.1 MHz at the receiver
    samples *= 2**14 # The PlutoSDR expects samples to be between -2^14 and +2^14, not -1 and +1 like some SDRs

    # Transmit our batch of samples 100 times, so it should be 1 second worth of samples total, if USB can keep up
    for i in range(100):
        sdr.tx(samples) # transmit the batch of samples once

def rxtest(sdr):
    #sets the sample rate to 1 MHz, sets the center frequency to 100 MHz, 
    # sets the gain to 70 dB with automatic gain control turned off.
    sample_rate = 1e6 # Hz
    center_freq = 100e6 # Hz
    num_samps = 10000 # number of samples returned per call to rx()

    sdr.gain_control_mode_chan0 = 'manual'
    sdr.rx_hardwaregain_chan0 = 70.0 # dB
    sdr.rx_lo = int(center_freq)
    sdr.sample_rate = int(sample_rate)
    sdr.rx_rf_bandwidth = int(sample_rate) # filter width, just set it to the same as sample rate for now
    sdr.rx_buffer_size = num_samps

    samples = sdr.rx() # receive samples off Pluto
    sample_len=len(samples)
    print(samples[0:10])
    plt.figure(0)
    plt.plot(np.arange(sample_len), samples,'.-')

    avg_pwr = np.var(samples) # (signal should have roughly zero mean)
    print("Average power:", avg_pwr)

    gainlevel=sdr._get_iio_attr('voltage0','hardwaregain', False)
    print("Current gain level:", gainlevel)

def main():
    parser = ArgumentParser()
    parser.add_argument('--devicename',  type=str, default='adrv9009', help='SDR name')#
    parser.add_argument('--ip', type=str, default='192.168.86.25', help='ip address')
    args = parser.parse_args()

    # Create radio
    uri='ip:'+args.ip
    sdr = adi.adrv9009(uri=uri)#"ip:192.168.86.25"


    sdr.sample_rate = int(2.5e6)
    sdr.rx()

    #DDStest(sdr)


def simulation():
    spectrogram_test()

if __name__ == '__main__':
    #main()
    simulation()