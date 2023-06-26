Linux Machine Setup
====================

https://docs.google.com/document/d/17vIhJuqDILWZhxh3WPh_voTGPPe-221xAEj_djWgSJE/edit

Install NVIDIA driver
---------------------

.. code-block:: console

    $ sudo ubuntu-drivers devices
    $ sudo apt install nvidia-driver-530

Install Basic Software
-----------------------

.. code-block:: console

    $ sudo apt install openssh-server
    (base) lkk@lkk-intel13:~$ conda activate mycondapy310
    (mycondapy310) lkk@lkk-intel13:~$ nvcc -V
    nvcc: NVIDIA (R) Cuda compiler driver
    Copyright (c) 2005-2022 NVIDIA Corporation
    Built on Wed_Sep_21_10:33:58_PDT_2022
    Cuda compilation tools, release 11.8, V11.8.89
    Build cuda_11.8.r11.8/compiler.31833905_0

Mount Disk
----------

.. code-block:: console

    $ df -H
    Filesystem      Size  Used Avail Use% Mounted on
    tmpfs            14G  3.4M   14G   1% /run
    /dev/nvme0n1p2  2.0T   83G  1.8T   5% /
    tmpfs            68G  549k   68G   1% /dev/shm
    tmpfs           5.3M  4.1k  5.3M   1% /run/lock
    /dev/nvme0n1p1  536M  6.4M  530M   2% /boot/efi
    tmpfs            14G  156k   14G   1% /run/user/1000
    tmpfs            14G  140k   14G   1% /run/user/1001
    $ lsblk
    NAME        MAJ:MIN RM   SIZE RO TYPE MOUNTPOINTS
    loop0         7:0    0     4K  1 loop /snap/bare/5
    loop1         7:1    0 244.5M  1 loop /snap/firefox/2800
    loop2         7:2    0  63.5M  1 loop /snap/core20/1891
    loop4         7:4    0  73.8M  1 loop /snap/core22/750
    loop5         7:5    0  73.9M  1 loop /snap/core22/766
    loop6         7:6    0 244.8M  1 loop /snap/firefox/2760
    loop7         7:7    0 349.7M  1 loop /snap/gnome-3-38-2004/137
    loop8         7:8    0 349.7M  1 loop /snap/gnome-3-38-2004/140
    loop9         7:9    0  53.3M  1 loop /snap/snapd/19457
    loop10        7:10   0 460.7M  1 loop /snap/gnome-42-2204/105
    loop11        7:11   0  91.7M  1 loop /snap/gtk-common-themes/1535
    loop12        7:12   0  45.9M  1 loop /snap/snap-store/638
    loop13        7:13   0  12.3M  1 loop /snap/snap-store/959
    loop14        7:14   0  63.4M  1 loop /snap/core20/1950
    loop15        7:15   0  53.3M  1 loop /snap/snapd/19361
    loop16        7:16   0   428K  1 loop /snap/snapd-desktop-integration/57
    loop17        7:17   0   452K  1 loop /snap/snapd-desktop-integration/83
    loop18        7:18   0 466.5M  1 loop /snap/gnome-42-2204/111
    sda           8:0    0   9.1T  0 disk 
    nvme0n1     259:0    0   1.8T  0 disk 
    ├─nvme0n1p1 259:1    0   512M  0 part /boot/efi
    └─nvme0n1p2 259:2    0   1.8T  0 part /var/snap/firefox/common/host-hunspell

You can see disk "sda" from the "lsblk" is not mounted. 

.. code-block:: console

    lkk@lkk-intel13:/$ sudo mkdir DATA10T

    lkk@lkk-intel13:/$ sudo nano -Bw /etc/fstab
    /dev/sda        /DATA10T        ext4    defaults        0       2
    lkk@lkk-intel13:/$ sudo mount -a
    (base) lkk@lkk-intel13:/$ df -H
    Filesystem      Size  Used Avail Use% Mounted on
    tmpfs            14G  3.4M   14G   1% /run
    /dev/nvme0n1p2  2.0T   83G  1.8T   5% /
    tmpfs            68G  549k   68G   1% /dev/shm
    tmpfs           5.3M  4.1k  5.3M   1% /run/lock
    /dev/nvme0n1p1  536M  6.4M  530M   2% /boot/efi
    tmpfs            14G  156k   14G   1% /run/user/1000
    tmpfs            14G  140k   14G   1% /run/user/1001
    /dev/sda         10T   37k  9.5T   1% /DATA10T


Common errors
-------------

.. code-block:: console
    (mycondapy310) lkk@lkk-intel13:~/Developer/3DDepth$ python ./VisUtils/testmayavi.py
    qt.qpa.plugin: Could not load the Qt platform plugin "xcb" in "/home/lkk/miniconda3/envs/mycondapy310/lib/python3.10/site-packages/cv2/qt/plugins" even though it was found.
    This application failed to start because no Qt platform plugin could be initialized. Reinstalling the application may fix this problem.

    Available platform plugins are: xcb, eglfs, linuxfb, minimal, minimalegl, offscreen, vnc, wayland-egl, wayland, wayland-xcomposite-egl, wayland-xcomposite-glx, webgl

    pip3 install --upgrade pyside2 pyqt5
    pip uninstall opencv-python
    pip uninstall opencv-python-headless
    pip install opencv-python-headless

    python ./VisUtils/testmayavi.py
    libGL error: No matching fbConfigs or visuals found
    libGL error: failed to load driver: swrast