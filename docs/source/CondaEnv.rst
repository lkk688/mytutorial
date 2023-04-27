CondaEnv
=====

.. _setup:

Conda Environment Setup Tutorial
------------

Install Miniconda

.. code-block:: console

   curl https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -o Miniconda3-latest-Linux-x86_64.sh
   bash Miniconda3-latest-Linux-x86_64.sh


Create a Conda virtual environment with python 3.10 (the default python version is 3.11):

.. code-block:: console

   (base) lkk@lkk-intel13:~$ conda create --name mycondapy310 python=3.10
   (base) lkk@lkk-intel13:~$ conda activate mycondapy310 #To activate this environment
   (mycondapy310) lkk@lkk-intel13:~$ conda info --envs #check existing conda environment
   (mycondapy310) lkk@lkk-intel13:~$ conda deactivate #To deactivate an active environment

Then install CUDA and cuDNN with conda and pip, and setup the environment path for cudnn

.. code-block:: console
   
   (mycondapy310) lkk@lkk-intel13:~$ conda install -c conda-forge cudatoolkit=11.8.0
   (mycondapy310) lkk@lkk-intel13:~$ pip install nvidia-cudnn-cu11==8.6.0.163
   (mycondapy310) lkk@lkk-intel13:~$ CUDNN_PATH=$(dirname $(python -c "import nvidia.cudnn;print(nvidia.cudnn.__file__)"))
   (mycondapy310) lkk@lkk-intel13:~$ echo $CUDNN_PATH
   /home/lkk/miniconda3/envs/mycondapy310/lib/python3.10/site-packages/nvidia/cudnn
   (mycondapy310) lkk@lkk-intel13:~$ export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$CONDA_PREFIX/lib/:$CUDNN_PATH/lib

You can automate it with the following commands. The system paths will be automatically configured when you activate this conda environment.

.. code-block:: console
   
   (mycondapy310) lkk@lkk-intel13:~$ mkdir -p $CONDA_PREFIX/etc/conda/activate.d
   (mycondapy310) lkk@lkk-intel13:~$ echo 'CUDNN_PATH=$(dirname $(python -c "import nvidia.cudnn;print(nvidia.cudnn.__file__)"))' >>      $CONDA_PREFIX/etc/conda/activate.d/env_vars.sh
   (mycondapy310) lkk@lkk-intel13:~$ echo 'export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$CONDA_PREFIX/lib/:$CUDNN_PATH/lib' >> $CONDA_PREFIX/etc/conda/activate.d/env_vars.sh
   (mycondapy310) lkk@lkk-intel13:~$ cat $CONDA_PREFIX/etc/conda/activate.d/env_vars.sh #check the content of the file

Install cuda development kit, otherwise 'nvcc' is not available

.. code-block:: console

   $ conda install -c conda-forge cudatoolkit-dev
   $ nvcc -V #show Cuda compilation tools, release 11.7, V11.7.64
   
Tensorflow Installation
----------------

Install the latest Tensorflow via pip, and verify the GPU setup

.. code-block:: console

   $ pip install tensorflow==2.12.*
   $ python3 -c "import tensorflow as tf; print(tf.config.list_physical_devices('GPU'))" #show [PhysicalDevice(name='/physical_device:GPU:0', device_type='GPU')]

TensorRT Installation
----------------

