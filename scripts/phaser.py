
import datetime
import os
import socket
import sys
import time
import numpy as np

import adi
from adi import ad9361
from adi.cn0566 import CN0566

# Figure out if we're running on the Raspberry Pi, indicated by a host name of "phaser".

if socket.gethostname().find(".") >= 0:
    my_hostname = socket.gethostname()
else:
    my_hostname = socket.gethostbyaddr(socket.gethostname())[0]

if "phaser" in my_hostname:  # See if we're running locally on Raspberry Pi
    rpi_ip = "ip:localhost"
    sdr_ip = "ip:192.168.2.1"  # Historical - assume default Pluto IP
    print("Hostname is phaser, connecting to ", rpi_ip, " and ", sdr_ip)

else:  # NOT running on the phaser, connect to phaser.local over network
    rpi_ip = "ip:phaser.local"  # IP address of the remote Raspberry Pi
    my_phaser = CN0566(uri=rpi_ip)
    #     rpi_ip = "ip:169.254.225.48" # Hard code an IP here for debug
    # sdr_ip = "ip:pluto.local"  # Pluto IP, with modified IP address or not
    sdr_ip = "ip:phaser.local:50901"  # Context Forwarding in libiio 0.24!
    my_sdr = ad9361(uri=sdr_ip)
    print("Hostname is NOT phaser, connecting to ", rpi_ip, " and ", sdr_ip)


my_phaser.sdr = my_sdr  # Set my_phaser.sdr

gpios = adi.one_bit_adc_dac(rpi_ip)
gpios.gpio_vctrl_1 = 1  # 1=Use onboard PLL/LO source  (0=disable PLL and VCO, and set switch to use external LO input)
gpios.gpio_vctrl_2 = (
    1  # 1=Send LO to transmit circuitry  (0=disable Tx path, and send LO to LO_OUT)
)

# setup GPIOs to control if Tx is output on OUT1 or OUT2
gpios.gpio_div_mr = 1
gpios.gpio_div_s0 = 0
gpios.gpio_div_s1 = 0
gpios.gpio_div_s2 = 0
gpios.gpio_tx_sw = 0  # gpio_tx_sw is "gpio_w" on schematic.  0=OUT1, 1=OUT2
time.sleep(0.5)