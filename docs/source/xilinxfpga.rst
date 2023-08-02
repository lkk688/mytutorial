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

Board setup process
    * Download Silicon Labs CP210x USB-to-UART Bridge VCP Drivers from https://www.silabs.com/developers/usb-to-uart-bridge-vcp-drivers?tab=downloads (Linux version is not needed)

Basic tutorial:
https://www.realdigital.org/doc/4ddc6ee53d1a2d71b25eaccc29cdec4b
https://www.so-logic.net/en/knowledgebase/fpga_universe/tutorials/Basic_FPGA_Tutorial_Verilog
https://digilent.com/reference/vivado/getting_started/start

https://wiki.analog.com/resources/fpga/docs/build
https://wiki.analog.com/resources/eval/user-guides/adrv9009/reference_hdl
https://github.com/analogdevicesinc/hdl/tree/master/projects/adrv9009/zcu102