Intel FPGA
===================

.. _arria10gx:

#:ref:`Arria10GX <_arria10gx>`

Intel Arria 10 GX Kit
---------------------

Boot the device
~~~~~~~~~~~~~~~~
Get the `Intel Arria 10 GX Kit <https://www.intel.com/content/www/us/en/products/details/fpga/development-kits/arria/10-gx.html>`_ official website, download the ** Intel® Arria® 10 GX FPGA Package ** in the downloads section. Unzip it and install the Board Test System.

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

Click New Project Wizard in Quartus, 


https://www.intel.com/content/www/us/en/support/programmable/support-resources/design-guidance/arria-10.html

Open the BoardTestSystem, show error:
Current bitMode value is 64
Current $QUARTUS_ROOTDIR = null


Nios® II EDS on Windows requires Ubuntu 18.04 LTS on Windows Subsystem for Linux (WSL). Nios® II EDS requires you to install an Eclipse IDE manually.
Nios II EDS need WSL1 not WSL2
https://www.intel.com/content/www/us/en/docs/programmable/683472/23-1/installing-windows-subsystem-for-linux.html
https://cdrdv2-public.intel.com/666293/quartus_install-683472-666293.pdf

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

nios2-terminal has no response, switch to WSL1 for testing

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
 C:\Users\lkk>wsl --distribution Ubuntu-20.04 --user lkk

