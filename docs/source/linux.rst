Linux Machine Setup
====================

https://docs.google.com/document/d/17vIhJuqDILWZhxh3WPh_voTGPPe-221xAEj_djWgSJE/edit

.. code-block:: console

    $ sudo ubuntu-drivers devices
    $ sudo apt install nvidia-driver-530
    $ sudo apt install openssh-server

.. code-block:: console

    (base) lkk@lkk-intel13:~$ conda activate mycondapy310
    (mycondapy310) lkk@lkk-intel13:~$ nvcc -V
    nvcc: NVIDIA (R) Cuda compiler driver
    Copyright (c) 2005-2022 NVIDIA Corporation
    Built on Wed_Sep_21_10:33:58_PDT_2022
    Cuda compilation tools, release 11.8, V11.8.89
    Build cuda_11.8.r11.8/compiler.31833905_0
