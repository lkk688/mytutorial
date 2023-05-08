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

