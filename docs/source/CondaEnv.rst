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

The tensorflow may show warning of "Could not load dynamic library 'libnvinfer.so.7'; dlerror: libnvinfer.so.7" and "Could not load dynamic library 'libnvinfer_plugin.so.7'; dlerror: libnvinfer_plugin.so.7" because of missing TensorRT library. You can refer the TensorRT section to install TensorRT8 and copy the libxx.so.8 to libxxx.so.7 to remove the warning.

.. code-block:: console
   $ cp /home/lkk/Developer/TensorRT-8.5.3.1/lib/libnvinfer_plugin.so.8 /home/lkk/Developer/TensorRT-8.5.3.1/lib/libnvinfer_plugin.so.7
   $ cp /home/lkk/Developer/TensorRT-8.5.3.1/lib/libnvinfer_plugin.so.8 /home/lkk/Developer/TensorRT-8.5.3.1/lib/libnvinfer_plugin.so.7

Waymo OpenDataset Installation
----------------

First install [openexr](https://www.excamera.com/sphinx/articles-openexr.html) for HDR images required by Waymo opendataset, then install waymo-open-dataset package

.. code-block:: console

   $ sudo apt-get install libopenexr-dev
   $ conda install -c conda-forge openexr
   $ conda install -c conda-forge openexr-python
   $ python3 -m pip install waymo-open-dataset-tf-2-11-0==1.5.1 #it will force install tensorflow2.11

TensorRT Installation
----------------

Use the tar installation options for [TensorRT](https://docs.nvidia.com/deeplearning/tensorrt/install-guide/index.html#installing-tar)
After the tar file is downloaded, untar the file, setup the TensorRT path, and install the tensorrt python package:

.. code-block:: console

   $ tar -xzvf TensorRT-8.5.3.1.Linux.x86_64-gnu.cuda-11.8.cudnn8.6.tar.gz
   $ export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/home/lkk/Developer/TensorRT-8.5.3.1/lib
   (mycondapy310) lkk@lkk-intel13:~/Developer/TensorRT-8.5.3.1/python$ python -m pip install tensorrt-8.5.3.1-cp310-none-linux_x86_64.whl #install the tensorrt python package
   (mycondapy310) lkk@lkk-intel13:~/Developer/TensorRT-8.5.3.1/graphsurgeon$ python -m pip install graphsurgeon-0.4.6-py2.py3-none-any.whl
   (mycondapy310) lkk@lkk-intel13:~/Developer/TensorRT-8.5.3.1/onnx_graphsurgeon$ python -m pip install onnx_graphsurgeon-0.3.12-py2.py3-none-any.whl
   
Check the TensorRT sample code from [TensorRTSample](https://docs.nvidia.com/deeplearning/tensorrt/sample-support-guide/index.html#samples)

