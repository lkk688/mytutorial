Intel FPGA
===================

.. _arria10gx:

#:ref:`Arria10GX <_arria10gx>`

Intel Arria 10 GX Kit
---------------------

Device Information
~~~~~~~~~~~~~~~~~~
Go to the `Intel Arria 10 GX Kit <https://www.intel.com/content/www/us/en/products/details/fpga/development-kits/arria/10-gx.html>`_ official website, download the ** Intel® Arria® 10 GX FPGA Package ** in the downloads section. Unzip it and install the Board Test System.
 * Intel Arria 10 GX Kit features a 10AX115S2F45I1SG device
 * Two FMC loopback cards supporting transceiver, LVDS and single-ended I/Os
 * Two FMC low-pin count (LPC + 15 transceivers) connector.
 * PCIe x8 edge connector.

Boot the device
~~~~~~~~~~~~~~~~
Follow ** Arria 10 FPGA Development Kit User Guide **, setup the SW6.4 to the ON position (factory default) and SW5 to default setting (MSEL0~2=100 position, OFF for 1, ON for 0), attach the Ethernet cable, then power on the FPGA board via J13 and set the SW1 to on.  When the board powers up, the parallel flash loader (PFL) on the MAX V reads a design from flash memory and configures the FPGA. When the configuration is complete, green LEDs illuminate signaling the device configured successfully. If the configuration fails, the red LED illuminates. The LCD will first display "Connecting", then show IP address "192.168.1.68". 

In the host computer, connect to this IP address to open the web page for the ** Board Update Portal ** . There are two files required:
  * The hardware file is the SRAM Object File (.sof) containing the FPGA image; 
  * The software file is Executable and Linkable Format File (.elf) containing the software application
(required only if the design includes a software application)

These two files need to convert to Flash format (the format required to program the Flash) via Nios II EDS, in Nios II Command Shell

.. code-block:: console 
  $ sof2flash --input=yourfile_hw.sof --output=yourfile_hw.flash --pfl --optionbit=0x00180000 --programmingmode=PS --offset=0x02D00000
  $ elf2flash --base=0x0 --end=0x0FFFFFFF --reset=0x09300000 --input=yourfile_sw.elf --output=yourfile_sw.flash --boot=$SOPC_KIT_NIOS2/components/altera_nios2/boot_loader_cfi.srec/strong>
  
When the upload is complete, Press button PGM_SEL (S5) until PGM_LED 1 is lit then press button PGM_CONFIG (S6) to configure the FPGA with the new image.
Or move the dipsw factory_load(SW6.4) to user position, then power cyle the board to configure FPGA from user portion of the flash.

The development board includes integrated USB-Blaster circuitry for FPGA programming. We need to install the On-Board USB-Blaster II driver on the host computer.

Install Quartus
~~~~~~~~~~~~~~~~

Download Quartus from `Intel FPGA Software Download Center <https://www.intel.com/content/www/us/en/collections/products/fpga/software/downloads.html>`_, select '23.1 for Windows'-> Multiple Download->Select Quartus-pro-23.1xxx-windows.tar (38.8GB device support not included) and Intel Arria 10 device support.

.. code-block:: console 

  C:\Users\lkk\Downloads>tar xvf Quartus-pro-23.1.0.115-windows.tar
  C:\Users\lkk\Downloads>tar xvf Quartus-pro-23.1.0.115-devices-1.tar

"components" folder is created after tar command, run the 'QuartusProSetup-23.1.0.115-windows' file inside the components. Select "H:\intelFPGA\quartus23.1" as the installation directory, select componets want to install (arria10 device is selected), skip MATLAB setup (only version R2013b and above)


Installation guide: https://cdrdv2-public.intel.com/666293/quartus_install-683472-666293.pdf
https://www.intel.com/content/www/us/en/docs/programmable/683472/23-1/setting-environment-variables.html

To setup the License for Quartus II, visit Intel license center. To add one computer, use "ipconfig /all" to get the physical address as the NIC ID (ref: https://www.intel.com/content/www/us/en/docs/programmable/683472/21-3/creating-a-computer-profile.html). After the computer NIC ID is assigned, click to generate license. Get the license file over email and save to "H:\intelFPGA"

Nios® II EDS on Windows requires Ubuntu 18.04 LTS on Windows Subsystem for Linux (WSL). Nios® II EDS requires you to install an Eclipse IDE manually.
Nios II EDS need WSL1 not WSL2
https://www.intel.com/content/www/us/en/docs/programmable/683472/23-1/installing-windows-subsystem-for-linux.html
https://cdrdv2-public.intel.com/666293/quartus_install-683472-666293.pdf


BoardTestSystem
~~~~~~~~~~~~~~~~
Connect the board J3 USB port to host PC, set factory_load(SW6.4) to user position (OFF mode), turn on the board. Open BoardTestSystem application inside the "examples" folder of the download board package. Remember to disable the Windows Realtime Projection, otherwise the BoardTestSystem will be blocked and deleted. Select "Restore -> Factory Restore".

Perform configuration of different parts in BoardTestSystem
 * Click Configure->Configure with Flash/GPIO design. After configuration, the GPIO tab will be enabled. You can change the LCD display, GPIO, LEDs, and Switches.
 
You can use the Quartus Programmer to configure the FPGA with your SRAM Object File (.sof)
Start the Quartus Programmer, open Programmer inside Tools
 * Select hardware setup select: USB-BlasterII
 * Click Auto Detect and select the devices "10AX115S2" in the list. It will show three device in the JTAG chain.
 * Click Change File and select the path to the desired .sof.

Quartus installation is required to run BoardTestSystem, otherwise it will show error when you open the BoardTestSystem, :
  Current bitMode value is 64
  Current $QUARTUS_ROOTDIR = null

Create a Quartus Project
~~~~~~~~~~~~~~~~~~~~~~~~
Click file > new project wizard… to begin the new project wizard, setup the directory for this project: "click file > new project wizard… to begin the new project wizard", and select the "Arria10 GX" in the Board section. Go back to the "device" tab, it will show "10AX115S2F45I1SG" in the list, select the device, then click Next. 


Next page shows add files. For this project we do not need to add any files, click Next. For this introduction to Quartus we will not be writing any code, therefore we do not need to use any EDA tools for this project. Just leave everything set to the default and click next. It will show a Summary page with project directory and selected device. Click Finish.

Go ahead and click file > new… to open the new file dialog box. We are going to create our first block diagram/schematic file, simply select it from the list and click ok. Save the file, click file > save as… and then give your file a name, choose the current path and click save. It will save as a '.bdf' file.

Click the symbol tool from the tool bar, this will open the symbol browser where you will notice three categories listed in the libraries box. Drop down primitives > logic to access basic logic functions. Select **and2** and then click ok to add the gate to the design. Once done you can press the esc key to exit the symbol tool.

Click the Pins dropdown button in the toolbar, and select output pin. Place to the diagram and connect to the **and2** output. Place two input pins and connect them to both inputs on the AND gate. In order to change the name of the pin you can either double click the pin name in the editor or right click the pin and choose properties. Go ahead and run analysis and elaboration using the tool found in the menu bar at the top of the screen.


There are different stages of processing required to convert our design into something that can be loaded on to the FPGA.
  * Analysis – in this part of the process Quartus checks the design for any errors such as syntax or semantic error.
  * Elaboration – in the first stage of compilation, Quartus maps out the design in RTL blocks. These are the building blocks within the FPGA that perform basic functions such as memory storage, logic gates and registers.
  * Synthesis – in the final stage of compilation, Quartus synthesizes a design at the logic level, converting the RTL design into a gate level design.

Once the process has completed you will have a compilation report and the analysis and elaboration process in the left-hand menu will have a green tick next to it. Now we can open the pin planner by clicking assignments > pin planner from the menu at the top of the screen (In order to get our pins to appear in the pin planner we could run a full compilation)

We can open the pin planner by clicking assignments > pin planner from the menu at the top of the screen. The input pins should correspond to the physical pins you have connected to the push buttons and the output pin should correspond to the output pin with the LED connected. Check the schematic of the Arria10 GX board. You can find following pin assignments
  * S3 PB0 switch->Net 'USER_PB0'->'T12' pin, in IO BANK-3E
  * S2 PB1 switch->Net 'USER_PB1'->'U12' pin, in IO BANK-3E
  * D10 LED_GR contains Green and Red Leds, voltage low to lit the LED 
    * Green -> Net 'USER_LED_G0'->'L28' pin, in IO BANK-3H
    * Red -> Net 'USER_LED_R0'->'L27' pin, in IO BANK-3H
  
Once you are done you can close the pin planner. You should notice that Quartus has labelled the pins with the physical outputs that we have just assigned. To load the design on to the FPGA, we must first run a complete compilation, which will synthesize the design and then create a binary .sof file that can be loaded on to the FPGA.

Once the compilation has complete we can open the programming tool in order to load our design on to the FPGA. You can either use the button on the top toolbar or click tools > programmer from the menu bar. On the programming menu you should see your programmer (e.g. the USB-Blaster) appearing at the top of the screen if your device is connected and configured correctly. If you see "no device" then you may need to select it by clicking "hardware setup…". You should also see the .sof file appearing in the list. Click "Start" to program the FPGA.

If you see the Progress failed. You can reboot the FPGA and change the SW4.2 dip switch from OFF to ON to disable MAX V in the JTAG chain and only leave Arria 10 in the JTAG. 

After the download is successfully, you can press any of the PB0 and PB1 switch to turn on the Green LED.

ADRV9009 Example
---------------------
Follow the ADRV9009+Arria10 GX example: https://wiki.analog.com/resources/eval/user-guides/adrv9009/quickstart/a10gx

.. code-block:: console 

 (base) lkk@Alienware-LKKi7G8:/mnt/h/intelFPGA/quartus23.1/nios2eds$ export PATH=/mnt/h/intelFPGA/quartus23.1/nios2eds/bin:$PATH
 (base) lkk@Alienware-LKKi7G8:/mnt/h/FPGADeveloper/adrv9009_a10gx/adrv9009_a10gx$ nios2-configure-sof adrv9009_a10gx.sof
 Searching for SOF file:
 in .
   adrv9009_a10gx.sof

 Info: *******************************************************************
 Info: Running Quartus Prime Programmer
 Info: Command: quartus_pgm --no_banner --mode=jtag -o p;./adrv9009_a10gx.sof
 Info (213045): Using programming cable "USB-BlasterII [USB-1]"
 Info (213011): Using programming file ./adrv9009_a10gx.sof with checksum 0x30E72CA2 for device 10AX115S2F45@1
 Info (209060): Started Programmer operation at Mon May  8 23:34:35 2023
 Info (209016): Configuring device index 1
 Info (209017): Device 1 contains JTAG ID code 0x02E660DD
 Info (209007): Configuration succeeded -- 1 device(s) configured
 Info (209011): Successfully performed operation(s)
 Info (209061): Ended Programmer operation at Mon May  8 23:34:50 2023
 Info: Quartus Prime Programmer was successful. 0 errors, 0 warnings
     Info: Peak virtual memory: 1936 megabytes
     Info: Processing ended: Mon May  8 23:34:50 2023
     Info: Elapsed time: 00:00:23
     Info: System process ID: 34076
 (base) lkk@Alienware-LKKi7G8:/mnt/h/FPGADeveloper/adrv9009_a10gx/adrv9009_a10gx$ export PATH=/mnt/h/intelFPGA/quartus23.
 1/nios2eds/bin/gnu/H-x86_64-mingw32/bin/:$PATH
 (base) lkk@Alienware-LKKi7G8:/mnt/h/FPGADeveloper/adrv9009_a10gx/adrv9009_a10gx$ nios2-download -g zImage
 Using cable "USB-BlasterII [USB-1]", device 1, instance 0x00
 Processor is already paused
 Initializing CPU cache (if present)
 OK
 Downloaded 5471KB in 0.5s (10942.0KB/s)
 Verified OK
 Starting processor at address 0xC4000000
 (base) lkk@Alienware-LKKi7G8:/mnt/h/FPGADeveloper/adrv9009_a10gx/adrv9009_a10gx$ nios2-terminal.exe
 nios2-terminal: connected to hardware target using JTAG UART on cable
 nios2-terminal: "USB-BlasterII [USB-1]", device 1, instance 0
 nios2-terminal: (Use the IDE stop button or Ctrl-C to terminate)

nios2-terminal has no response, switch to WSL1 for testing. As stated in  Quartus install instruction, Nios II EDS only works with WSL1, in section 2.3.1 of: https://cdrdv2-public.intel.com/666293/quartus_install-683472-666293.pdf

Install a new distribution (Ubuntu20.04), set the wsl version from 2 to 1, ref: https://learn.microsoft.com/en-us/windows/wsl/basic-commands

.. code-block:: console 

 C:\Users\lkk>wsl --list --online
 C:\Users\lkk>wsl --install -d Ubuntu-20.04
 C:\Users\lkk>wsl --list --verbose
   NAME            STATE           VERSION
 * Ubuntu-22.04    Running         2
   Ubuntu-20.04    Running         2

 C:\Users\lkk>wsl --set-version Ubuntu-20.04 1
 Conversion in progress, this may take a few minutes.
 The operation completed successfully.

 C:\Users\lkk>wsl --list --verbose
   NAME            STATE           VERSION
 * Ubuntu-22.04    Running         2
   Ubuntu-20.04    Stopped         1
 C:\Users\lkk>wsl --distribution Ubuntu-20.04 --user lkk #start the linux
 >wsl -t Ubuntu-20.04 #shut down the linux
 
.. code-block:: console 
 lkk@Alienware-LKKi7G8:~$ ls
 QuartusProSetup-23.1.0.115-linux.run  QuartusProSetup-part2-23.1.0.115-linux.qdz  quartus  ubuntu20
 lkk@Alienware-LKKi7G8:~$ ./QuartusProSetup-23.1.0.115-linux.run --mode text --installdir ./quartus
 lkk@Alienware-LKKi7G8:~/adi$ export PATH=~/quartus/quartus/bin/:$PATH
 lkk@Alienware-LKKi7G8:~/adi$ git clone https://github.com/analogdevicesinc/hdl.git
 lkk@Alienware-LKKi7G8:~/adi/hdl/projects/adrv9009/a10soc$ sudo apt update
 lkk@Alienware-LKKi7G8:~/adi/hdl/projects/adrv9009/a10soc$ sudo apt install make
 lkk@Alienware-LKKi7G8:~/adi/hdl/projects/adrv9009/a10soc$ sudo apt install build-essential
 lkk@Alienware-LKKi7G8:~/adi/hdl/projects/adrv9009/a10soc$ sudo apt install dos2unix
 lkk@Alienware-LKKi7G8:~/adi/hdl/projects/adrv9009/a10soc$ sudo apt-get install libncurses5

Follow the ADI Building HDL instruction: https://wiki.analog.com/resources/fpga/docs/build, build the adrv9009/a10soc project:

.. code-block:: console 

 lkk@Alienware-LKKi7G8:~/adi/hdl/projects/adrv9009/a10soc$ export ADI_IGNORE_VERSION_CHECK=1
 lkk@Alienware-LKKi7G8:~/adi/hdl/projects/adrv9009/a10soc$ make
 Building adrv9009_a10soc [/home/lkk/adi/hdl/projects/adrv9009/a10soc/adrv9009_a10soc_quartus.log] .

 2023.05.10.00:23:53 Error: Unknown device part 10AS066N3F40E2SG
 CRITICAL WARNING: Quartus version mismatch; expected 22.4.0, got 23.1.0.

 lkk@Alienware-LKKi7G8:~/adi/hdl/projects/adrv9009/a10soc$ cat adrv9009_a10soc.qsf
 set_global_assignment -name DEVICE 10AS066N3F40E2SG
 set_global_assignment -name QSYS_FILE system_bd.qsys

Show build error of "Unknown device part 10AS066N3F40E2SG". The device setup code is in "projects/scripts/adi_project_intel.tcl" and based on the project name:

.. code-block:: console 
 
  if [regexp "_a10gx" $project_name] {
     set family "Arria 10"
     set device 10AX115S2F45I1SG
   }

   if [regexp "_a10soc" $project_name] {
     set family "Arria 10"
     set device 10AS066N3F40E2SG
   }

Change the project name in Makefile and system_project.tcl to "adrv9009_a10gx", it still show "Error: Unknown device part 10AX115S2F45I1SG". Setup some paths and run quartus_sh in command line (similar to make) and show progress in terminal.

.. code-block:: console 

 export ALTERA_ROOT="/home/lkk/quartus/"		# Change this to the path you've installed Altera Quartus at
 export QUARTUS_ROOTDIR_OVERRIDE="$ALTERA_ROOT/quartus"
 export QSYS_ROOTDIR="$QUARTUS_ROOTDIR_OVERRIDE/sopc_builder/bin"
 export QUARTUS_LIBRARY_PATHS="$QUARTUS_ROOTDIR_OVERRIDE/linux64/:/lib/x86_64-linux-gnu/"
 export SOPC_KIT_NIOS2="$ALTERA_ROOT/nios2eds"
 export LD_LIBRARY_PATH="$LD_LIBRARY_PATH:$QUARTUS_LIBRARY_PATHS"
 export PATH="$PATH:$ALTERA_ROOT/quartus/bin"
 lkk@Alienware-LKKi7G8:~/adi/hdl/projects/adrv9009/a10soc$ quartus_sh --64bit -t system_project.tcl
 2023.05.10.10:26:44 Error: Unknown device part 10AX115S2F45I1SG
 child process exited abnormally
     while executing
 "exec -ignorestderr $quartus(quartus_rootpath)/sopc_builder/bin/qsys-generate  system_bd.qsys --synthesis=VERILOG --family=$family --part=$device  --qu..."
     (procedure "adi_project" line 161)
     invoked from within
 "adi_project adrv9009_a10gx"
     (file "system_project.tcl" line 4)
 


https://www.intel.com/content/www/us/en/support/programmable/support-resources/design-guidance/arria-10.html#tab-blade-1-0
Quartus II Scripting Reference Manual: https://www.intel.com/programmable/technical-pdfs/654662.pdf

ADRV9009 Arria 10 GX Quick Start Guide: https://wiki.analog.com/resources/eval/user-guides/adrv9009/quickstart/a10gx
IIO Oscilloscope: https://wiki.analog.com/resources/tools-software/linux-software/iio_oscilloscope
Nios2 Linux on the Altera FPGA Development Boards: https://wiki.analog.com/resources/tools-software/linux-drivers/platforms/nios2
ADRV9009 HDL Reference Design: https://wiki.analog.com/resources/eval/user-guides/adrv9009/reference_hdl
https://github.com/analogdevicesinc/hdl/tree/master/projects/adrv9009
https://github.com/analogdevicesinc/hdl/tree/master
ADI™ Reference Designs HDL User Guide: https://wiki.analog.com/resources/fpga/docs/hdl
Building HDL: https://wiki.analog.com/resources/fpga/docs/build#windows_environment_setup
Intel® Arria® 10 FPGA Developer Center: https://www.intel.com/content/www/us/en/support/programmable/support-resources/design-guidance/arria-10.html
