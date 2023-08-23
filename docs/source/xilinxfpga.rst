Xilinx FPGA
===================

.. _xilinxfpga:


Xilinx ZCU102
---------------------
Zynq UltraScale+ MPSoC ZCU102 Evaluation Kit: https://www.xilinx.com/products/boards-and-kits/ek-u1-zcu102-g.html

    * ZCU102 Evaluation Board User Guide
    * Form factor for PCIe Gen2x4 Host, Micro-ATX chassis footprint
    * Zynq® UltraScale+ ™ XCZU9EG-2FFVB1156E MPSoC (quad-core Arm® Cortex-A53, dual-core Cortex-R5F real-time processors, and a Mali-400 MP2 graphics processing)
    * 2x FPGA Mezzanine Card (FMC) interfaces for I/O expansion, including 16 16.3Gb/s GTH transceivers and 64 user-defined differential I/O signals. FMC #1 (8 GTH) and FMC #2 (8 GTH) PL GT assignment
    * 24 GTH gigabit transceivers (16.3 Gb/s capable) on the PL-side, grouped into four channels referred to as Quads (total six Quads), Two are wired to the FMC0 HPC connector (J5), 
    * J5 (HPC0) and J4 (HPC1) use a 10 x 40 form factor (Table 3‐44:J5 HPC0 FMC Section A and B Connections to XCZU9EG U1)
    * The ZU9EG contains many useful processor system (PS) hard block peripherals exposed through the Multi-use I/O (MIO) interface and a variety of FPGA programmable logic (PL), high-density (HD) and high-performance (HP) banks.
    * DDR4 SODIMM - 4GB 64-bit w/ ECC attached to processing system (PS)
    * DDR4 Component - 512MB 16-bit attached to programmable logic (PL)
    * Onboard JTAG configuration circuitry to enable configuration over USB (J2)
    * 12V wall adapter or ATX
    * Switch SW6 Configuration: JTAG (0000, switch on,on,on,on), QSPI (0010), and SD (1110)
    * A Host PC resident system controller user interface (SCUI) based on on-board MSP430: tutorial on the SCUI (XTP433) and board setup instructions (XTP435)

Board setup process in Windows
    * Download Silicon Labs CP210x USB-to-UART Bridge VCP Drivers from https://www.silabs.com/developers/usb-to-uart-bridge-vcp-drivers?tab=downloads (Linux version is not needed)
    * In windows, open control panel-system-device manager. There will be four “Silicon Labs Quad CP210x” COM ports, 0 through 3; Interface 0 & 1 are for the ARM processor; Interface 2 is for PL Fabric (MicroBlaze) use; Interface 3 is for the MSP430
    * Downdload and install Tera Term (https://ttssh2.osdn.jp/index.html.en)
    * Power the board, open terminal program, select COM port, and set the baud to 115200
    * Refer XTP 433 for System Controller GUI
    * Ethernet setup: change adapter setting, right-click Ethernet Adapter and select properties. Click Configure, Set the Link Speed & Duplex to Auto Negotiation then click OK. Set the IPv4 address to "192.168.1.2", subnet "255.255.255.0", default gateway "192.168.1.255"

 Xilinx Vivado
---------------------
Vivado installation tutorial: https://www.realdigital.org/doc/1fd3322461ac4bcc1fcd6bcc6c5907ec

.. code-block:: console 

    (base) lkk@lkk-intel12:~/Xilinx$ ls
    DocNav  Downloads  Model_Composer  Vitis_HLS  Vivado  xic  Xilinx.lic
    (base) lkk@lkk-intel12:~/Xilinx$ cd Vivado/
    (base) lkk@lkk-intel12:~/Xilinx/Vivado$ ls
    2023.1
    (base) lkk@lkk-intel12:~/Xilinx/Vivado$ cd 2023.1/
    (base) lkk@lkk-intel12:~/Xilinx/Vivado/2023.1$ ls
    bin       fonts     lib                  product_rel_win.log  settings64.sh
    data      gnu       lnx64                reportstrategies     strategies
    doc       ids_lite  platforms            scripts              tps
    examples  include   product_rel_lin.log  settings64.csh
    (base) lkk@lkk-intel12:~/Xilinx/Vivado/2023.1$ source settings64.sh
    (base) lkk@lkk-intel12:~/Xilinx/Vivado/2023.1$ vivado &

Install Linux cable Drivers

.. code-block:: console 

    (base) lkk@lkk-intel12:~/Xilinx/Vivado/2023.1/data/xicom/cable_drivers/lin64/install_script/install_drivers$ ls
    52-xilinx-digilent-usb.rules  install_digilent.sh  setup_xilinx_ftdi
    52-xilinx-ftdi-usb.rules      install_drivers
    52-xilinx-pcusb.rules         setup_pcusb
    (base) lkk@lkk-intel12:~/Xilinx/Vivado/2023.1/data/xicom/cable_drivers/lin64/install_script/install_drivers$ sudo ./install_drivers
    
After Vivado is started, Click on “Create Project” in the Quick Start panel. This will open the New Project dialog. Click Next to continue.

.. image:: imgs/FPGA/zcu102newproject1.png
  :width: 600
  :alt: zcu102newproject1

Set Project Name and Location. Select Project Type (RTL). There are no existing sources and constraints to add, so just click Next.

.. image:: imgs/FPGA/zcu102newproject2.png
  :width: 600
  :alt: zcu102newproject2

.. note::

    Constraint files provide information about the physical implementation of the design. They are created by the user, and used by the synthesizer. Constraints are parameters that specify certain details about the design. As examples, some constraints identify which physical pins on the chip are to be connected to which named circuit nodes in your design; some constraints setup various physical attributes of the chip, like I/O pin drive strength (high or low current); and some constraints identify physical locations of certain circuit components. The Xilinx Design Constraints (.xdc filetpye) is the file format used for describing design constraints, and you need to create an .xdc file in order to synthesize your designs for a Real Digital board.

Select the board of "zcu102"

.. image:: imgs/FPGA/zcu102newproject3.png
  :width: 600
  :alt: zcu102newproject3

On the last page of the Create Project Wizard, there is a summary of the project configuration. click Finish to finish creating an empty project.

.. image:: imgs/FPGA/zcu102newproject4.png
  :width: 600
  :alt: zcu102newproject4

After you have finished with the Create Project Wizard, the main IDE window will be displayed.

.. image:: imgs/FPGA/zcu102newproject5.png
  :width: 600
  :alt: zcu102newproject5

.. note::

    All projects require at least two types of source files - an HDL file (Verilog or VHDL) to describe the circuit, and a constraints file to provide the synthesizer with the information it needs to map your circuit into the target chip. After the constraint file is created, the design can be synthesized. The synthesis process translates Verilog source code into logical operations, and it uses the constraints file to map the logical operations into a given chip. In particular (for our needs here), the constraints file defines which Verilog circuit nodes are attached to which pins on the Xilinx chip package, and therefore, which circuit nodes are attached to which physical devices on your board. The synthesis process creates a “.bit” file that can be directly programmed into the Xilinx chip.

To create a Verilog source file for your project, right-click on “Design Sources” in the Sources panel, and select Add Sources. 

.. image:: imgs/FPGA/zcu102newprojectaddsource1.png
  :width: 600
  :alt: zcu102newprojectaddsource1

The Add Sources dialog box will appear as shown - select “Add or create design sources” and click next. 

.. image:: imgs/FPGA/zcu102newprojectaddsource2.png
  :width: 600
  :alt: zcu102newprojectaddsource2


In the Add or Create Design Sources dialog, click on Create File, enter project1_demo as filename, and click OK. 

.. image:: imgs/FPGA/zcu102newprojectaddsource3.png
  :width: 600
  :alt: zcu102newprojectaddsource3

Skip the Define Module dialog by clicking OK to continue.

.. code-block:: console 

    module hello_demo(
        output led0, led1,
        input sw0, sw1, sw2
        );
    wire x;
    
    assign led0 = sw0 & sw1;
    assign x = sw0 | sw1;
    assign led1 = x & sw2;
    
    endmodule

To create a constraint file, expand the Constraints heading in the Sources panel, right-click on constrs_1, and select Add Sources. An Add Sources dialog will appear. 

.. image:: imgs/FPGA/zcu102addconstraintfile.png
  :width: 600
  :alt: zcu102addconstraintfile

Select Add or Create Constraints and click Next to cause the “Add or Create Constraints” dialog box to appear. Click on Create File, enter the filename and click OK.

.. image:: imgs/FPGA/zcu102addconstraintfile2.png
  :width: 600
  :alt: zcu102addconstraintfile2

In the constraint file, we need to add the pin assignment for the clock pins. We can check the zcu102 clock source list and understand that ZCU102 get clock "CLK_74_25" and "CLK_125" from U69 SI5341 clock generator.

.. image:: imgs/FPGA/zcu102clocksource.png
  :width: 600
  :alt: zcu102clocksource

In ZCU102 schematic, we can see the schematic of the SI5341 clock generator, it generates a differential pair of clock "CLK_74_25_P" and "CLK_74_25_N":

.. image:: imgs/FPGA/zcu102SI5341schematic.png
  :width: 600
  :alt: zcu102SI5341schematic

We can add constraint of the clock and the pin assignment of these clock pins

.. image:: imgs/FPGA/zcu102clockconstraint.png
  :width: 600
  :alt: zcu102clockconstraint

In the constraint file, we also need to add the FPGA pin assignment for LEDs and Buttons, we can get the schematic information for the LEDs and Buttons:

.. image:: imgs/FPGA/zcu102ledbuttonschematic.png
  :width: 600
  :alt: zcu102ledbuttonschematic

After your Verilog and constraint files are complete, you can Synthesize the design project. In the synthesis process, Verilog code is translated into a “netlist” that defines all the required circuit components needed by the design (these components are the programmable parts of the targeted logic device - more on that later). You can start the Synthesize process by clicking on Run Synthesis button in the Flow Navigator panel

.. image:: imgs/FPGA/zcu102runsynthesis.png
  :width: 600
  :alt: zcu102runsynthesis

After the design is synthesized, you must run the Implementation process. The implementation process maps the synthesized design onto the Xilinx chip targeted by the design. Click the Run Implementation button in the Flow Navigator panel

After the design is successfully implemented, you can create a .bit file by clicking on the Generate Bitstream process located in the Flow Navigator panel. The process translates the implemented design into a bitstream which can be directly programmed into your board's device.

.. image:: imgs/FPGA/zcu102generatebitstream.png
  :width: 600
  :alt: zcu102generatebitstream

After the bitstream is successfully generated, you view the implementation. 

.. image:: imgs/FPGA/zcu102viewimplementation.png
  :width: 600
  :alt: zcu102viewimplementation

In the implementation graph, the FPGA resource allocation is displayed in the device view.

.. image:: imgs/FPGA/zcu102implementation.png
  :width: 600
  :alt: zcu102implementation


You can program your board using the Hardware Manager. Click Open Hardware Manager located at the bottom of Flow Navigator panel. Click on Open target link underneath Hardware Manager. Select Auto Connect to automatically identify your board. If Vivado successfully detects your board, the Hardware panel (located at the top left corner of Hardware Manager) will show the board's logic device part number.

.. image:: imgs/FPGA/zcu102deviceprogramming1.png
  :width: 600
  :alt: zcu102deviceprogramming1

Select the device you want to program, right click and select Program Device. A Program Device pop-up dialog window will appear, with the generated bit file selected in the text box. Click on Program to download the bitstream to your board.


.. image:: imgs/FPGA/zcu102deviceprogramming2.png
  :width: 600
  :alt: zcu102deviceprogramming2

.. image:: imgs/FPGA/zcu102deviceprogramming3.png
  :width: 600
  :alt: zcu102deviceprogramming3

Verilog
--------

In Verilog, combinational logic output signals are said to be “continuously driven”, meaning they take new values immediately after input changes. Memory outputs do not take on new values immediately after their data inputs change; rather, their outputs can change only after a change on a clock or reset signal, i.e., “procedurally driven”.

Verilog source files use “modules” to define all circuits, and the module statement is the first line of code in a Verilog source file. The module statement names the module so it can be accessed by other designs and tools as needed, and it defines all input and output signals. 

When writing “Behavioral Verilog” code, the module statement is followed by any number of continuous assignment or procedural assignment statements to define the circuit's behavior. When writing “Structural Verilog”, the module statement is followed by any number of instantiations of other modules.

Verilog source files define how signals are driven over time. Two data/signal types are used - the “wire” type for continuously driven signals arising from an input pin or a combinational logic circuit; and the “reg” type for procedurally driven signals that (usually) arise from a memory circuit.

Continuous assignment statements drive “wire” signals, and so continuous assignment statements define combinational logic circuits. They begin with the keyword “assign” followed by the output signal name, and then the conditions under which the output is driven.

Procedural assignment statements drive “reg” signals, and so procedural assignments are used to define memory circuits. They begin with the keyword “always” that identifies a procedural block the simulator must always execute.

Input signals to modules are always type “wire”; output signals from modules can be type “wire” or “reg”. If additional wire or reg signals are needed inside a module (for example, to transport signals between assignment statements), they must be explicitly declared after the module statement 

ADRV9009
---------
In ADRV9009 web page (https://www.analog.com/en/products/adrv9009.html)
    * ADRV9008/ADRV9009 Evaluation Software with GUI for Evaluation Board (ZIP) (adrv9009-eval-software-with-gui), installed in Windows, but cannot connect to the ZCU102 board, it may only works for ZC706 board
    * adrv9008-x-adrv9009-profile-config-tool: show MATLAB lib error
    * ADRV9009-SDCARD, for zc706? sPut the "BOOT.bin", "devicetree.dtb", and "uImage" to ZCU102 SD Card, the linux cannot be boot. 

ADI TES software does not support for ZCU102, only support ZYNQ3. The configuration files can be generated without a physical board.

ADI HDL Code
-------------

Build the HDL code: https://wiki.analog.com/resources/fpga/docs/build

.. code-block:: console 

    (base) lkk@lkk-intel12:~/Xilinx/FPGADeveloper$ mkdir adi
    (base) lkk@lkk-intel12:~/Xilinx/FPGADeveloper$ cd adi
    (base) lkk@lkk-intel12:~/Xilinx/FPGADeveloper/adi$ git clone https://github.com/analogdevicesinc/hdl.git
    (base) lkk@lkk-intel12:~/Xilinx/FPGADeveloper/adi/hdl$ git status
    On branch master
    Your branch is up to date with 'origin/master'.

    nothing to commit, working tree clean
    (base) lkk@lkk-intel12:~/Xilinx/FPGADeveloper/adi/hdl$ git checkout hdl_2021_r1
    Branch 'hdl_2021_r1' set up to track remote branch 'hdl_2021_r1' from 'origin'.
    Switched to a new branch 'hdl_2021_r1'

    $ source ~/Xilinx/Vivado/2023.1/settings64.sh
    #export PATH=$PATH:/opt/Xilinx/Vivado/202x.x/bin:/opt/Xilinx/Vitis/202x.x/bin
    (base) lkk@lkk-intel12:~/Xilinx/FPGADeveloper/adi/hdl/projects/adrv9009/zcu102$ export ADI_IGNORE_VERSION_CHECK=1
    (base) lkk@lkk-intel12:~/Xilinx/FPGADeveloper/adi/hdl/projects/adrv9009/zcu102$ make
    ....
    Building adrv9009_zcu102 project [/home/lkk/Xilinx/FPGADeveloper/adi/hdl/projects/adrv9009/zcu102/adrv9009_zcu102_vivado.log] ... OK
    (base) lkk@lkk-intel12:~/Xilinx/FPGADeveloper/adi/hdl/projects/adrv9009/zcu102$ ls
    adrv9009_zcu102.cache          adrv9009_zcu102_vivado.log  system_top.v
    adrv9009_zcu102.gen            adrv9009_zcu102.xpr         timing_impl.log
    adrv9009_zcu102.hw             Makefile                    timing_synth.log
    adrv9009_zcu102.ip_user_files  mem_init_sys.txt            vivado.jou
    adrv9009_zcu102.runs           system_bd.tcl               vivado.log
    adrv9009_zcu102.sdk            system_constr.xdc
    adrv9009_zcu102.srcs           system_project.tcl
    (base) lkk@lkk-intel12:~/Xilinx/FPGADeveloper/adi/hdl/projects/adrv9009/zcu102$ ls adrv9009_zcu102.sdk/
    system_top.xsa



ADI Linux Image Boot
---------------------
https://wiki.analog.com/resources/tools-software/linux-software/kuiper-linux
https://wiki.analog.com/resources/tools-software/linux-software/zynq_images/windows_hosts

In Windows host, download SD Card Formatter from https://www.sdcardformatter.com/. Insert the SD card and launch SD Card Formatter, type "boot" in Volume label, then click "Format"

Open Balena Etcher (Download from https://sourceforge.net/projects/etcher.mirror/files/v1.18.11/), select the Linux image (.img) file, 

Open SD card, find folder "zynqmp-zcu102-rev10-adrv9009", copy "BOOT.BIN" and "system.dtb" to the root of the BOOT partition; In folder "zynqmp-common", copy "Image" to the root.

After the SD card is finished, load the SD card into the ZCU102 board, in the J100 connector. Connect a micro USB cable from the ZCU102 board USB UART port (J83) to the USB port on the host machine. Configure the board to boot in SD-boot mode by setting switch SW6 to 1-ON, 2-OFF, 3- OFF, and 4-OFF.

In Windows Machine, download and install Silicon Labs CP210x USB-to-UART Bridge VCP Drivers from https://www.silabs.com/developers/usb-to-uart-bridge-vcp-drivers?tab=downloads. Open "Device Manager", you will see "Silicon Labs Quad CP2108 USB to UART Bridge: Interface 0 (COM4) -3 (COM7)". Open Tera Term, select port "COM4", then click "Setup-Ports" to change the baud rate to "115200", then enter.

Turn on the ZCU102 Board using SW1, and wait until Linux loads on the board. At this point, you can see the initial boot sequence messages on your terminal screen. After the Linux is booted, you can check the IP address of the ZCU102 board.

.. image:: imgs/FPGA/zcu102linuxbootwindowsterminal.png
  :width: 600
  :alt: zcu102linuxbootwindowsterminal

During the bootup, there are adrv9009 spi1.1 Error:

.. image:: imgs/FPGA/zcu102adrv9009booterror.png
  :width: 600
  :alt: zcu102adrv9009booterror

You can also check the error message via "dmesg", ref: https://www.cyberciti.biz/faq/unix-linux-apple-osx-bsd-screen-set-baud-rate/,
http://wiki.espressobin.net/tiki-index.php?page=Serial+connection+-+Linux

.. code-block:: console 

    $ sudo dmesg | grep tty
    [    0.178023] printk: console [tty0] enabled
    [    0.713714] serial8250: ttyS0 at I/O 0x3f8 (irq = 4, base_baud = 115200) is a 16550A
    [39228.154004] usb 1-5: FTDI USB Serial Device converter now attached to ttyUSB0
    [39247.737114] ftdi_sio ttyUSB0: FTDI USB Serial Device converter now disconnected from ttyUSB0
    [58323.816351] usb 1-5: FTDI USB Serial Device converter now attached to ttyUSB0
    [58761.456823] ftdi_sio ttyUSB0: FTDI USB Serial Device converter now disconnected from ttyUSB0
    [58767.946276] usb 1-5: cp210x converter now attached to ttyUSB0
    [58767.946904] usb 1-5: cp210x converter now attached to ttyUSB1
    [58767.947546] usb 1-5: cp210x converter now attached to ttyUSB2
    [58767.948152] usb 1-5: cp210x converter now attached to ttyUSB3

In Linux machine, the tera term can be replaced by minicom:

.. code-block:: console 

    $ sudo minicom -s
    #minicom -D /dev/ttyUSB0
    # setup Serial port setup
    sudo apt install ckermit

.. image:: imgs/FPGA/zcu102linuxterminal.png
  :width: 600
  :alt: zcu102linuxterminal

ADRV9009-W/PCBZ Zynq UltraScale+ MPSoC ZCU102 Quick Start
---------------------------------------------------------

https://wiki.analog.com/resources/eval/user-guides/adrv9009/quickstart/zynqmp

Building the ZynqMP / MPSoC Linux kernel and devicetrees from source (https://wiki.analog.com/resources/eval/user-guides/ad-fmcomms2-ebz/software/linux/zynqmp)

https://xilinx-wiki.atlassian.net/wiki/spaces/A/overview

.. code-block:: console 

    (base) lkk@lkk-intel12:~/Xilinx$ source ./Vivado/2023.1/settings64.sh
    (base) lkk@lkk-intel12:~/Xilinx/FPGADeveloper$ git clone https://github.com/analogdevicesinc/linux.git
    (base) lkk@lkk-intel12:~/Xilinx/FPGADeveloper/linux$ git checkout master
    (base) lkk@lkk-intel12:~/Xilinx/FPGADeveloper$ export PATH=$PATH:/home/lkk/Xilinx/Vitis/2023.1/gnu/aarch64/lin/aarch64-linux/bin
    (base) lkk@lkk-intel12:~/Xilinx/FPGADeveloper/linux$ export ARCH=arm64
    (base) lkk@lkk-intel12:~/Xilinx/FPGADeveloper/linux$ export CROSS_COMPILE=/home/lkk/Xilinx/FPGADeveloper/gcc-linaro-7.5.0-2019.12-x86_64_aarch64-linux-gnu/bin/aarch64-linux-gnu-

    (base) lkk@lkk-intel12:~/Xilinx/FPGADeveloper/linux$ make adi_zynqmp_defconfig
    (base) lkk@lkk-intel12:~/Xilinx/FPGADeveloper/linux$ make -j5 Image UIMAGE_LOADADDR=0x8000
    ....
      LD      vmlinux
    SORTTAB vmlinux
    SYSMAP  System.map
    OBJCOPY arch/arm64/boot/Image
    (base) lkk@lkk-intel12:~/Xilinx/FPGADeveloper/linux$ ls arch/arm64/boot/
    dts  Image  install.sh  Makefile
    (base) lkk@lkk-intel12:~/Xilinx/FPGADeveloper/linux$ cp arch/arm64/boot/Image ~/Documents/
    (base) lkk@lkk-intel12:~/Xilinx/FPGADeveloper/linux$ cp arch/arm64/boot/dts/xilinx/zynqmp-zcu102-rev10-adrv9009.dts ~/Documents/system.dtb

dts file in arch/arm64/boot/dts/xilinx/


https://releases.linaro.org/components/toolchain/binaries/latest-7/aarch64-linux-gnu/
https://snapshots.linaro.org/gnu-toolchain/14.0-2023.06-1/aarch64-linux-gnu/


Building the ZynqMP boot image

.. code-block:: console 

    (base) lkk@lkk-intel12:~/Xilinx/FPGADeveloper/mybuild$ ls
    bootgen_sysfiles      build_zynqmp_boot_bin.sh  system.dtb
    bootgen_sysfiles.tgz  Image                     system_top.xsa
    (base) lkk@lkk-intel12:~/Xilinx/FPGADeveloper/mybuild$ chmod +x build_zynqmp_boot_bin.sh

    (base) lkk@lkk-intel12:~/Xilinx/FPGADeveloper/mybuild$ source ~/Xilinx/Vivado/2023.1/settings64.sh

    (base) lkk@lkk-intel12:~/Xilinx/FPGADeveloper/mybuild$ ./build_zynqmp_boot_bin.sh system_top.xsa ./bootgen_sysfiles/u-boot_xilinx_zynqmp_zcu102_revA.elf ./bootgen_sysfiles/bl31.elf 
    + cp build_boot_bin/build/sdk/hw0/export/hw0/sw/hw0/boot/pmufw.elf output_boot_bin/pmufw.elf
    + cd output_boot_bin
    + bootgen -arch zynqmp -image zynq.bif -o BOOT.BIN -w

    ****** Bootgen v2023.1
    **** Build date : Apr 18 2023-23:27:00
        ** Copyright 1986-2022 Xilinx, Inc. All Rights Reserved.
        ** Copyright 2022-2023 Advanced Micro Devices, Inc. All Rights Reserved.

    [INFO]   : Bootimage generated successfully

    (base) lkk@lkk-intel12:~/Xilinx/FPGADeveloper/mybuild$ ls output_boot_bin/
    bl31.elf  fsbl.elf   system_top.bit  u-boot.elf
    BOOT.BIN  pmufw.elf  system_top.xsa  zynq.bif

References
------------

Basic tutorial:
https://www.realdigital.org/doc/4ddc6ee53d1a2d71b25eaccc29cdec4b
https://www.so-logic.net/en/knowledgebase/fpga_universe/tutorials/Basic_FPGA_Tutorial_Verilog
https://digilent.com/reference/vivado/getting_started/start
https://github.com/pulp-platform/pulp/blob/master/fpga/pulp-zcu102/rtl/xilinx_pulp.v
https://github.com/fpgadeveloper/ethernet-fmc-zynq-gem/blob/master/Vivado/src/constraints/zcu102-hpc0.xdc
https://xilinx.github.io/Embedded-Design-Tutorials/docs/2021.1/build/html/docs/Introduction/ZynqMPSoC-EDT/8-boot-and-configuration.html
A first look at Verilog: https://www.realdigital.org/doc/0bb58d31f393f8a7c6b5ac4a0d84876e

https://wiki.analog.com/resources/fpga/docs/build
https://github.com/analogdevicesinc/hdl
https://wiki.analog.com/resources/eval/user-guides/adrv9009/reference_hdl
https://wiki.analog.com/resources/eval/user-guides/adrv9009/quickstart/zynqmp
https://github.com/analogdevicesinc/hdl/tree/master/projects/adrv9009/zcu102
https://wiki.analog.com/resources/tools-software/linux-drivers-all#building_the_adi_linux_kernel
https://wiki.analog.com/resources/tools-software/linux-build/generic/zynqmp

https://wiki.analog.com/resources/tools-software/linux-software/kuiper-linux

Starting 2019.2, SDK, SDSoC™ and SDAccel™ development environments are unified into an all-in-one Vitis™ unified software platform for application acceleration and embedded software development.
https://www.xilinx.com/products/design-tools/legacy-tools/sdk.html
https://www.xilinx.com/products/design-tools/vitis/vitis-platform.html