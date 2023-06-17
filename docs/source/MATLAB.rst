MATLAB
=================


MATLAB with Analog Device
---------------------------
Analog Devices Transceiver Toolbox For MATLAB and Simulink: https://wiki.analog.com/resources/tools-software/transceiver-toolbox
    * ADRV9009 is supported with Xilinx ZCU102
    * Download and install Transceiver toolbox (AnalogDevicesTransceiverToolbox_v21.2.1.mltbx) from: https://github.com/analogdevicesinc/TransceiverToolbox/releases, double click the mltbx file will open MATLAB and install the toolbox.
    * Install libiio
    * Install either: Communications Toolbox Support Package for Xilinx Zynq-Based Radio or Communications Toolbox Support Package for Analog Devices ADALM-Pluto Radio (These support packages provide the necessary libIIO MATLAB bindings used by ADI's system objects)



API Doc: https://analogdevicesinc.github.io/TransceiverToolbox/master/
In https://analogdevicesinc.github.io/TransceiverToolbox/master/install/, Download libiio MATLAB Binding Standalone Installer (R2021b+), which requires Signal Processing Toolbox.

TransceiverToolbox examples:
https://github.com/analogdevicesinc/TransceiverToolbox/tree/master/trx_examples/targeting
https://github.com/analogdevicesinc/TransceiverToolbox/tree/master/trx_examples/streaming

Communications Toolbox Support Package for Analog Devices ADALM-Pluto Radio: https://www.mathworks.com/help/supportpkg/plutoradio/index.html?s_tid=CRUX_lftnav

Install Support Package for Analog Devices ADALM-PLUTO Radio: https://www.mathworks.com/help/supportpkg/plutoradio/ug/install-support-package-for-pluto-radio.html

n the MATLAB Home tab, in the Environment section, click Add-Ons, select Get Hardware Support Packages.

.. image:: imgs/ADI/matlabgethardwaresupport.png
    :width: 900
    :alt: matlabgethardwaresupport

Install Support Package for Analog Devices ADALM-PLUTO Radio

.. image:: imgs/ADI/matlabinstallcommunication.png
    :width: 900
    :alt: matlabinstallcommunication


.. note::

    The IIS System Object interfaces are deprecated. The IIO System Object is based on the MATLAB System Objects™ specification. It is designed to exchange data over Ethernet with an ADI hardware system connected to a FPGA/SoC platform running the ADI Linux distribution. ref: https://wiki.analog.com/resources/tools-software/linux-software/libiio/clients/matlab_simulink

The IIO System Object is built upon the libiio library and enables a MATLAB or Simulink model to 
    * Stream data to and from a target
    * Control the settings of a target, and
    * Monitor different target parameters. Please use the Transceiver Toolbox, 

Process streaming signals and large data with System objects: https://www.mathworks.com/discovery/stream-processing.html

Connect device in MATLAB
------------------------

.. code-block:: console 

    rx = adi.ADRV9009.Rx;
    rx.uri = 'ip:192.168.86.21';
    data = rx();
    Warning: System Object 'adi.ADRV9009.Rx' is inherited from mixin class 'matlab.system.mixin.SampleTime' that will no longer be supported. Remove
    'matlab.system.mixin.SampleTime' and define corresponding System object methods instead. 
    Warning: System Object 'adi.ADRV9009.Rx' is inherited from mixin class 'matlab.system.mixin.CustomIcon' that will no longer be supported. Remove
    'matlab.system.mixin.CustomIcon' and define corresponding System object methods instead. 
    Error using matlabshared.libiio.base/cstatusid
    Failed to write attribute: calibrate_frm_en to device.

    Error in matlabshared.libiio.device/iio_device_attr_write

    Error in adi.common.Attribute/setDeviceAttributeRAW (line 133)
                bytes = iio_device_attr_write(obj,phydev,attr,value);

    Error in adi.ADRV9009.Rx/setupInit (line 219)
                obj.setDeviceAttributeRAW('calibrate_frm_en',num2str(obj.EnableFrequencyHoppingModeCalibration));

    Error in adi.common.RxTx/configureChanBuffers (line 219)
                setupInit(obj);

    Error in matlabshared.libiio.base/setupImpl

    Error in adi.common.RxTx/setupImpl (line 117)
                setupImpl@matlabshared.libiio.base(obj);

The code below will show the same error:

.. code-block:: console 

    rx = adi.ADRV9009.Rx('uri','ip:192.168.86.21');
    rx.EnabledChannels = 1;
    rx.kernelBuffersCount = 1;
    for k=1:20
        valid = false;
        while ~valid
            [y, valid] = rx();
        end
    end

Try to use AD9361 to connect:

.. code-block:: console 

    rx = adi.AD9361.Rx;
    rx.uri = 'ip:192.168.86.21';
    data = rx();
    Warning: System Object 'adi.AD9361.Rx' is inherited from mixin class 'matlab.system.mixin.SampleTime' that will no longer be supported. Remove
    'matlab.system.mixin.SampleTime' and define corresponding System object methods instead. 
    Warning: System Object 'adi.AD9361.Rx' is inherited from mixin class 'matlab.system.mixin.CustomIcon' that will no longer be supported. Remove
    'matlab.system.mixin.CustomIcon' and define corresponding System object methods instead. 
    Error using matlabshared.libiio.base/cstatusid
    Failed to find device: cf-ad9361-lpc.

    Error in matlabshared.libiio.base/getDev

    Error in matlabshared.libiio.base/setupImpl

    Error in adi.common.RxTx/setupImpl (line 117)
                setupImpl@matlabshared.libiio.base(obj);

.. code-block:: console 

    iio_attr -u ip:192.168.1.10 -d


https://github.com/analogdevicesinc/TransceiverToolbox/blob/master/%2Badi/%2BADRV9009/Rx.m
In function setupInit(obj): obj.setDeviceAttributeRAW('calibrate_frm_en',num2str(obj.EnableFrequencyHoppingModeCalibration));

Building the Toolbox Manually: https://wiki.analog.com/resources/tools-software/transceiver-toolbox

Device attributes related code in https://github.com/bpkempke/adi-linux/blob/master/drivers/iio/adc/adrv9009.c

.. code-block:: console 

    static IIO_DEVICE_ATTR(calibrate_frm_en, S_IRUGO | S_IWUSR,
                adrv9009_phy_show,
                adrv9009_phy_store,
                ADRV9009_INIT_CAL | (TAL_FHM_CALS << 8));
    static struct attribute *adrv9009_phy_attributes[] = {
        &iio_dev_attr_ensm_mode.dev_attr.attr,
        &iio_dev_attr_ensm_mode_available.dev_attr.attr,
        &iio_dev_attr_calibrate.dev_attr.attr,
        &iio_dev_attr_calibrate_rx_qec_en.dev_attr.attr,
        &iio_dev_attr_calibrate_tx_qec_en.dev_attr.attr,
        &iio_dev_attr_calibrate_tx_lol_en.dev_attr.attr,
        &iio_dev_attr_calibrate_tx_lol_ext_en.dev_attr.attr,
        &iio_dev_attr_calibrate_rx_phase_correction_en.dev_attr.attr,
        &iio_dev_attr_calibrate_frm_en.dev_attr.attr,
        NULL,
    };

Design Examples in MATLAB
-------------------------
Communications Toolbox: https://www.mathworks.com/help/comm/index.html?s_tid=hc_product_card

Supported Hardware Software-Defined Radio: https://www.mathworks.com/help/comm/supported-hardware-software-defined-radio.html

Guided Host-Radio Hardware Setup: https://www.mathworks.com/help/supportpkg/xilinxzynqbasedradio/ug/guided-host-radio-hardware-setup.html

Communications Toolbox Support Package for Xilinx Zynq-Based Radio: https://www.mathworks.com/help/supportpkg/xilinxzynqbasedradio/index.html
    * Hardware and Software Requirements: https://www.mathworks.com/help/supportpkg/xilinxzynqbasedradio/ug/hardware-and-software-requirements.html
    * Support Xilinx ZC706 with AD FMCOMMS2345
    * sdrdev: Create radio object for interfacing with Xilinx Zynq-based radio hardware: https://www.mathworks.com/help/supportpkg/xilinxzynqbasedradio/ug/sdrdev.html
    * common problems: https://www.mathworks.com/help/supportpkg/xilinxzynqbasedradio/ug/common-problems-and-fixes.html

dev = sdrdev(___,'IPAddress',192.168.86.25)
dev = sdrdev('AD936x') #Create a radio object 
info(dev) #Use this object to get radio hardware information.
testConnection(dev) #test host-radio connectivity.

QPSK Modem Design Workflow: https://wiki.analog.com/resources/eval/user-guides/ad-fmcomms2-ebz/software/matlab_bsp_modem
Frequency Hopping Example Design: https://wiki.analog.com/resources/eval/user-guides/adrv936x_rfsom/tutorials/frequency_hopping
Loopback Delay Estimation Design: https://wiki.analog.com/resources/eval/user-guides/adrv936x_rfsom/tutorials/loopback_delay_estimation
LTE eNB Transmitter Conformance Tests Using ADALM-PLUTO: https://wiki.analog.com/resources/tools-software/transceiver-toolbox/examples/pluto_lte_app
HW/SW Co-Design with AXI4-Stream Using Analog Devices AD9361/AD9364: https://www.mathworks.com/help/supportpkg/xilinxzynqbasedradio/ug/hwsw-co-design-with-axi4-stream-using-analog-devices-ad9361-ad9364.html

https://www.mathworks.com/help/supportpkg/plutoradio/application-specific-examples.html

Image Transmission and Reception Using LTE Waveform and SDR: https://www.mathworks.com/help/supportpkg/plutoradio/ug/transmission-and-reception-of-an-image-using-lte-toolbox-and-a-single-pluto-radio.html

Spectrum Sensing with Deep Learning to Identify 5G and LTE Signals: https://www.mathworks.com/help/supportpkg/plutoradio/ug/spectrum-sensing-with-deep-learning-to-identify-5g-lte-signals.html