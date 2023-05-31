ADI
===============================

ADI HDL Design
---------------
ADI HDL related information
  * ADI HDL repo: https://github.com/analogdevicesinc/hdl
  * ADI Reference Designs HDL User Guide: https://wiki.analog.com/resources/fpga/docs/hdl
  * all the projects have no-OS (baremetal https://github.com/analogdevicesinc/no-OS) and a Linux (https://github.com/analogdevicesinc/Linux) support.

The HDL repository is divided into two seperate sections
  * projects with all the currently supported projects. There are two special folders inside the /hdl/projects: 
      * common: contains all the base designs, for all currently supported FPGA development boards
      * scripts (Tcl scripts): defined all the custom Tcl processes, which are used to create a project, define the system and generate programming files for the FPGA.
  * library with all the Analog Devices Inc. proprietary IP cores and hdl modules, which are required to build the projects. The library folder contains all the IP cores and common modules. An IP, in general, contains Verilog files, which describe the hardware logic, constraint files, to ease timing closure, and Tcl scripts, which generate all the other files required for IP integration (*_ip.tcl for Vivado and *_hw.tcl for Quartus).

Running the HDL on hardware. HDL build alone will NOT let you do anything useful. You would need a software running on the processor (Microblaze, NIOS or ARM) to make the design work. There are two software solutions: 1) Linux and 2) No-OS. Ref: https://wiki.analog.com/resources/fpga/docs/run

HDL Architecture: https://wiki.analog.com/resources/fpga/docs/arch

Using and modifying the HDL designs: https://wiki.analog.com/resources/fpga/docs/tips


adrv9009
--------
ADRV9009: https://www.analog.com/en/products/adrv9009.html
ADRV9009 hardware reference guide: https://www.analog.com/media/en/technical-documentation/user-guides/adrv9008-1-w-9008-2-w-9009-w-hardware-reference-manual-ug-1295.pdf
ADRV9009, ADRV9008 highly integrated, wideband RF transceiver Linux device driver： https://wiki.analog.com/resources/tools-software/linux-drivers/iio-transceiver/adrv9009

SDR Integrated Transceiver Design Resources: https://www.analog.com/en/design-center/landing-pages/001/integrated-rf-agile-transceiver-design-resources.html
    * Download the ADRV9008/ADRV9009 Design File Package
  

Wideband RF Transceiver Evaluation Software (TES): https://www.analog.com/en/design-center/landing-pages/001/transceiver-evaluation-software.html
    * ADRV9008/ADRV9009 Evaluation Software with GUI for Evaluation Board (ZIP)
    * ADRV9008/ADRV9009 API Source Code (ZIP)
    * ADRV9008-x and ADRV9009 Profile Configuration Tool (Filter Wizard) (ZIP)
    * ADRV9009-SDCARD

ADRV9009/ADRV9008 No-OS System Level Design Setup: https://wiki.analog.com/resources/eval/user-guides/adrv9009/no-os-setup
    * Arria 10 GX board supported
    * Demo application ADRV9009-W on ZCU102: DMA_EXAMPLE, TINYIIOD demo

iio-oscilloscope
-----------------
https://github.com/analogdevicesinc/iio-oscilloscope
https://wiki.analog.com/resources/tools-software/linux-software/iio_oscilloscope#installation

Analog Devices Kuiper Linux
https://wiki.analog.com/resources/tools-software/linux-software/kuiper-linux
User: root, password: analog; User: analog, password: analog
The SD card includes several folders in the root directory of the BOOT partition. In order to configure the SD card to work with a specific FPGA board and ADI hardware, several files must be copied onto the root directory.

Configuring the SD Card for Raspberry Pi Projects:

Intel Arria10 SOC board schematic: https://www.analog.com/media/en/technical-documentation/eval-board-schematic/a10_soc_devkit_a3.pdf