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

Set Project Name and Location. Select Project Type (RTL). There are no existing sources and constraints to add, so just click Next.

.. note::

    Constraint files provide information about the physical implementation of the design. They are created by the user, and used by the synthesizer. Constraints are parameters that specify certain details about the design. As examples, some constraints identify which physical pins on the chip are to be connected to which named circuit nodes in your design; some constraints setup various physical attributes of the chip, like I/O pin drive strength (high or low current); and some constraints identify physical locations of certain circuit components. The Xilinx Design Constraints (.xdc filetpye) is the file format used for describing design constraints, and you need to create an .xdc file in order to synthesize your designs for a Real Digital board.

Select the board of "zcu102"

On the last page of the Create Project Wizard, there is a summary of the project configuration. click Finish to finish creating an empty project.

After you have finished with the Create Project Wizard, the main IDE window will be displayed.

.. note::

    All projects require at least two types of source files - an HDL file (Verilog or VHDL) to describe the circuit, and a constraints file to provide the synthesizer with the information it needs to map your circuit into the target chip. After the constraint file is created, the design can be synthesized. The synthesis process translates Verilog source code into logical operations, and it uses the constraints file to map the logical operations into a given chip. In particular (for our needs here), the constraints file defines which Verilog circuit nodes are attached to which pins on the Xilinx chip package, and therefore, which circuit nodes are attached to which physical devices on your board. The synthesis process creates a “.bit” file that can be directly programmed into the Xilinx chip.

To create a Verilog source file for your project, right-click on “Design Sources” in the Sources panel, and select Add Sources. The Add Sources dialog box will appear as shown - select “Add or create design sources” and click next. In the Add or Create Design Sources dialog, click on Create File, enter project1_demo as filename, and click OK. Skip the Define Module dialog by clicking OK to continue.

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

To create a constraint file, expand the Constraints heading in the Sources panel, right-click on constrs_1, and select Add Sources. An Add Sources dialog will appear as shown. Select Add or Create Constraints and click Next to cause the “Add or Create Constraints” dialog box to appear. Click on Create File, enter the filename and click OK.


After your Verilog and constraint files are complete, you can Synthesize the design project. In the synthesis process, Verilog code is translated into a “netlist” that defines all the required circuit components needed by the design (these components are the programmable parts of the targeted logic device - more on that later). You can start the Synthesize process by clicking on Run Synthesis button in the Flow Navigator panel

After the design is synthesized, you must run the Implementation process. The implementation process maps the synthesized design onto the Xilinx chip targeted by the design. Click the Run Implementation button in the Flow Navigator panel

After the design is successfully implemented, you can create a .bit file by clicking on the Generate Bitstream process located in the Flow Navigator panel. The process translates the implemented design into a bitstream which can be directly programmed into your board’s device.

After the bitstream is successfully generated, you can program your board using the Hardware Manager. Click Open Hardware Manager located at the bottom of Flow Navigator panel

Click on Open target link underneath Hardware Manager. Select Auto Connect to automatically identify your board. If Vivado successfully detects your board, the Hardware panel (located at the top left corner of Hardware Manager) will show the board’s logic device part number

Select the device you want to program, right click and select Program Device. A Program Device pop-up dialog window will appear, with the generated bit file selected in the text box. Click on Program to download the bitstream to your board.

Verilog
--------

In Verilog, combinational logic output signals are said to be “continuously driven”, meaning they take new values immediately after input changes. Memory outputs do not take on new values immediately after their data inputs change; rather, their outputs can change only after a change on a clock or reset signal, i.e., “procedurally driven”.

Verilog source files use “modules” to define all circuits, and the module statement is the first line of code in a Verilog source file. The module statement names the module so it can be accessed by other designs and tools as needed, and it defines all input and output signals. 

When writing “Behavioral Verilog” code, the module statement is followed by any number of continuous assignment or procedural assignment statements to define the circuit's behavior. When writing “Structural Verilog”, the module statement is followed by any number of instantiations of other modules.

Verilog source files define how signals are driven over time. Two data/signal types are used - the “wire” type for continuously driven signals arising from an input pin or a combinational logic circuit; and the “reg” type for procedurally driven signals that (usually) arise from a memory circuit.

Continuous assignment statements drive “wire” signals, and so continuous assignment statements define combinational logic circuits. They begin with the keyword “assign” followed by the output signal name, and then the conditions under which the output is driven.

Procedural assignment statements drive “reg” signals, and so procedural assignments are used to define memory circuits. They begin with the keyword “always” that identifies a procedural block the simulator must always execute.

Input signals to modules are always type “wire”; output signals from modules can be type “wire” or “reg”. If additional wire or reg signals are needed inside a module (for example, to transport signals between assignment statements), they must be explicitly declared after the module statement 

ADI
----
https://wiki.analog.com/resources/fpga/docs/build

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






References
------------

Basic tutorial:
https://www.realdigital.org/doc/4ddc6ee53d1a2d71b25eaccc29cdec4b
https://www.so-logic.net/en/knowledgebase/fpga_universe/tutorials/Basic_FPGA_Tutorial_Verilog
https://digilent.com/reference/vivado/getting_started/start

A first look at Verilog: https://www.realdigital.org/doc/0bb58d31f393f8a7c6b5ac4a0d84876e

https://wiki.analog.com/resources/fpga/docs/build
https://github.com/analogdevicesinc/hdl
https://wiki.analog.com/resources/eval/user-guides/adrv9009/reference_hdl
https://github.com/analogdevicesinc/hdl/tree/master/projects/adrv9009/zcu102