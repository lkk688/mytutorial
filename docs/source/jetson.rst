NVIDIA Jetson
=============

Quick Start
--------------
The working directory in SSD (Samsung 970 EVO 1TB) in lkk@xavieragx:/ssd$
    * conda activate mycondapy310


Jetson Xavier AGX Setup
-----------------------
Detailed steps see my Google doc: https://docs.google.com/document/d/1OAvlxpsP6h7YDicX29Bo7IWV_irWsoOyeB0_lujoHME/edit#heading=h.l55ml9jogv02

Jetpack page: https://developer.nvidia.com/embedded/jetpack


Show Jetpack version: 

.. code-block:: console

    sudo apt show nvidia-jetpack #show 5.0.2
    git clone https://github.com/jetsonhacks/jetsonUtilities.git #option2
    cd jetsonUtilities
    python jetsonInfo.py

(Not tried, list file not found) To upgrade from previous JetPack 5.x releases, first edit etc/apt/sources.list.d/nvidia-l4t-apt-source.list to point to the 35.3 repo (just change the version to r35.3 in both lines). Next, use the following commands, then physically reboot the system:

.. code-block:: console

    sudo apt update
    sudo apt dist-upgrade
    sudo apt install --fix-broken -o Dpkg::Options::="--force-overwrite"

Jetson Orin Nano
----------------
Jetson Orin Nano: Jetson Orin Nano 8GB with SD card slot (P3767-0005)
Jetson Orin Nano Developer Kit User Guide: https://developer.nvidia.com/embedded/learn/jetson-orin-nano-devkit-user-guide/index.html
Develop guide: https://docs.nvidia.com/jetson/archives/r35.3.1/DeveloperGuide/index.html

Install Miniconda for ARM
-------------------------
Ref: https://conda.io/projects/conda/en/stable/user-guide/install/linux.html

.. code-block:: console

    wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-aarch64.sh
    bash Miniconda3-latest-Linux-aarch64.sh #select the install location to /ssd/miniconda3, select conda init
    conda config --set auto_activate_base false # if do not want to activate base automatically
    conda list
    conda update conda
    conda --version
    conda info
    conda update -n base conda
    conda create --name mycondapy310
    conda env create -f environment.yml #Creating an environment from an environment.yml file
    conda activate mycondapy310 #activate environment
    conda env list
    conda info --envs #same to the previous one
    conda deactivate #deactivate environment

You can control where a conda environment lives by providing a path to a target directory when creating the environment.

.. code-block:: console

    conda create --prefix ./envs jupyterlab=3.2 matplotlib=3.5 numpy=1.21
    conda activate ./envs

To remove this long prefix in your shell prompt, modify the env_prompt setting in your .condarc file:

.. code-block:: console

    $ conda config --set env_prompt '({name})'

You may need to update your environment, you can update the contents of your environment.yml file accordingly and then run the following command:

.. code-block:: console

    conda env update --prefix ./env --file environment.yml  --prune

Install VSCode for ARM
-------------------------

.. code-block:: console

    VERSION=latest
    wget -N -O vscode-linux-deb.arm64.deb https://update.code.visualstudio.com/$VERSION/linux-deb-arm64/stable
    sudo apt install ./vscode-linux-deb.arm64.deb
    # Install a Python linter
    pip3 install pylint
    # Install a Python formatter
    pip3 install black

    # Install the Python extension for Visual Studio Code
    # Extension name is ms-python.python
    code --install-extension ms-python.python --force
