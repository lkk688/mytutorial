PhasedArray
=============

References
---------------
Phased Array (Phaser) Development Platform: https://www.analog.com/en/design-center/reference-designs/circuits-from-the-lab/cn0566.html

The CN0566 main board implements an 8-element phased array, downconverting mixers, local oscillator (LO), and digital control circuitry. The CN0566 outputs are two IF signals at a nominal frequency of 2.2 GHz, that are digitized by a PlutoSDR module.

The RF input signal is received from an onboard 8-element patch antenna that operates from 10 to 10.5 GHz. Each antenna element is input to an ADL8107, a low noise amplifier (LNA) that operates from 6-18GHz with 1.3dB NF and 24 dB gain. The output of these amplifiers is fed into the main core of this circuitry, two of the ADAR1000. The ADAR1000 is an 8 GHz to 16 GHz, 4-Channel, beamformer that allows per-channel, 360° phase adjustment with 2.8° resolution, and 31dB gain adjustment with 0.5dB resolution. The ADAR1000s are capable of bidirectional, half-duplex operation. However, CN0566 only connects the ADAR1000 receive paths. The outputs of four LNAs get phase and amplitude shifted by an ADAR1000, then summed together at its RFIO output.

The ADAR1000's RFIO output passes through a low pass filter before entering the LTC5548 mixer. The low pass filter removes the high side image of the mixer as well as any re-radiation of the high side LO. LTC5548 outputs an IF of approximately 2.2 GHz which passes through a low pass filter (LPF) to remove mixer spurs and attenuate any RF or LO leakage. The LPF's output, at Rx1 and Rx2, can then be mixed down and sampled by an external 2-channel SDR receiver, such as the ADALM-Pluto.

ADAR1000 (https://www.analog.com/en/products/ADAR1000.html): 8 GHz to 16 GHz, 4-Channel, X Band and Ku Band Beamformer, 4-wire SPI interface

ADL8107 (https://www.analog.com/en/products/ADL8107.html): Low Noise Amplifier, 6 GHz to 18 GHz

LTC5548 (https://www.analog.com/en/products/ltc5548.html) 2GHz to 14GHz Microwave Mixer with Wideband DC-6GHz IF, Upconversion or Downconversion

ADRF5019 (https://www.analog.com/en/products/ADRF5019.html) Silicon, SPDT Switch, Nonreflective, 100 MHz to 13 GHz

ADF4159 (https://www.analog.com/en/products/adf4159.html) Direct Modulation/Fast Waveform Generating, 13 GHz, Fractional-N Frequency Synthesizer


.. image:: imgs/ADI/CN0566_01.png
  :width: 600
  :alt: CN0566 diagram


ADF4159 Linux Device Driver: https://wiki.analog.com/resources/tools-software/linux-drivers/iio-pll/adf4159
ADAR1000 Linux Device Driver: https://wiki.analog.com/resources/tools-software/linux-drivers/iio-transceiver/adar1000

Download Design FIles: CN0566 BOM.csv, allergo.brd, schematic.pdf
CN0566 Phased Array User Guide: https://wiki.analog.com/resources/eval/user-guides/circuits-from-the-lab/cn0566

https://wiki.analog.com/resources/eval/user-guides/circuits-from-the-lab/cn0566/overview_setup

HB100 microwave source
HB100 with Arduino: https://techmaze.romman.store/product/99187053

SD Card Image:
https://wiki.analog.com/resources/tools-software/linux-software/kuiper-linux
https://www.raspberrypi.com/news/raspberry-pi-imager-imaging-utility/

https://wiki.analog.com/_media/resources/eval/user-guides/circuits-from-the-lab/cn0566/phaser_lab_instructions_june14_2022_no_title.pdf

https://github.com/analogdevicesinc/pyadi-iio
https://github.com/analogdevicesinc/pyadi-iio/tree/master/examples/phaser
https://github.com/analogdevicesinc/pyadi-iio/blob/master/adi/cn0566.py
https://github.com/analogdevicesinc/pyadi-iio/blob/master/examples/adrv9009.py
https://github.com/analogdevicesinc/pyadi-iio/blob/master/examples/phaser/phaser_gui.py

Quick Start
------------

https://wiki.analog.com/resources/eval/user-guides/circuits-from-the-lab/cn0566/quickstart

.. code-block:: console 

  wget https://github.com/mthoren-adi/rpi_setup_stuff/raw/main/phaser/phaser_sdcard_setup.sh
  sudo chmod +x phaser_sdcard_setup.sh
  ./phaser_sdcard_setup.sh
  sudo reboot
  wget https://github.com/mthoren-adi/rpi_setup_stuff/raw/main/phaser/config_phaser.txt
  cp config_phaser.txt config.txt
  sudo mv /boot/config.txt /boot/config_original.txt
  sudo reboot

After running the script, the hostname will be phaser.local, sample code in "~/pyadi-iio/examples/phaser", "phaser_find_hb100.py" and "phaser_gui.py"

Initial Calibration (https://wiki.analog.com/resources/eval/user-guides/circuits-from-the-lab/cn0566/calibration). Place the HB100 directly in front of the array at approximately 1.5 m away. Then run:

.. code-block:: console 

  python phaser_examples.py cal

Pluto firmware update: https://wiki.analog.com/university/tools/pluto/users/firmware

Update the Pluto configuration to enable the AD9361's second channel (https://wiki.analog.com/university/tools/pluto/users/customizing#updating_to_the_ad9364)

.. code-block:: console 

  ssh analog@192.168.86.20 #password: analog
  cat /media/analog/PlutoSDR/config.txt
  iio_info -n pluto.local
  ping pluto.local
  iio_attr -C fw_version --uri="ip:192.168.2.1"
    fw_version: v0.35
  analog@phaser:~ $ ssh root@192.168.2.1 #password: analog

  $ fw_printenv attr_name
  attr_name=compatible
  $ fw_printenv attr_val
  attr_val=ad9361
  $ fw_printenv compatible
  compatible=ad9361
  $ fw_printenv mode
  mode=2r2t


