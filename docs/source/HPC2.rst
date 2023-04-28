HPC2
=====

.. _setup:

Load software module and request GPU node
------------

Check available software and load the required modules

.. code-block:: console

   $ module avail
   $ module load python39 slurm/slurm/21.08.6 gcc/11.2.0 cuda12.0/toolkit/12.0.1
   $ conda info --envs #check available conda environments
   $ conda activate mycondapy39
   
Use Slurm to request one GPU node, and setup required paths

.. code-block:: console

   $ srun --pty /bin/bash # request GPU node
   [sjsuid@cs002 ~]$ nvidia-smi # got the GPU node 'cs002', check the gpu via "nvidia-smi"
   [sjsuid@cs002 ~]$ module load python39 cuda12.0/toolkit/12.0.1 #load python and cuda module
   [sjsuid@cs002 ~]$ nvcc -V # check cuda version
   [sjsuid@cs002 ~]$ conda activate mycondapy39
   (mycondapy39) [sjsuid@cs002 ~]$ export LD_LIBRARY_PATH=/data/cmpe249-fa22/mycuda/TensorRT-8.4.2.4/lib:$LD_LIBRARY_PATH #add tensorrt library if needed
   (mycondapy39) [sjsuid@cs002 ~]$ CUDNN_PATH=$(dirname $(python -c "import nvidia.cudnn;print(nvidia.cudnn.__file__)")) #get cudnn path
   (mycondapy39) [sjsuid@cs002 ~]$ export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$CONDA_PREFIX/lib/:$CUDNN_PATH/lib #add cudnn path (only needed for Tensorflow)

The GPU node does not have internet access, if you need to access the Jupyter web in your local browser, you can establish one tunnel from your local computer to the HPC headnode, then create another tunnel from the HPC headnode to the GPU node

.. code-block:: console

   $ ssh -L 10001:localhost:10001 010796032@coe-hpc2.sjsu.edu #from your local computer to HPC headnode, you can use any port number (10001)
   $ ssh -L 10001:localhost:10001 010796032@cs002 #in HPC head node to gpu node
   $ jupyter lab --no-browser --port=10001 #start the jupyter lab on port 10001 (the port should be the same port used for tunnel)

After jupyter lab is started, you can copy paste the URL shown in the terminal into your local browser to access the Jupyter lab.

Conda Environment Setup Tutorial
------------

To use this tutorial package, first install it using pip:

.. code-block:: console

   (.venv) $ pip install lumache

Creating recipes
----------------
