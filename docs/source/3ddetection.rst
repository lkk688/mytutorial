3D Object Detection
===================

OpenCOOD
------------------

Use `OpenCOOD <https://github.com/DerrickXuNu/OpenCOOD>`_ and ref `installation <https://opencood.readthedocs.io/en/latest/md_files/installation.html>`_ to setup the V2V cooperative 3D object detection framework (based on OpenPCDet) in Newalienware machine (with RTX3090)

.. code-block:: console

  (mycondapy39) lkk68@NEWALIENWARE C:\Users\lkk68\Documents\Developer>git clone https://github.com/DerrickXuNu/OpenCOOD.git
  (mycondapy39) lkk68@NEWALIENWARE C:\Users\lkk68\Documents\Developer\OpenCOOD>python setup.py develop
  #error: scipy 1.5.4 is installed but scipy>=1.8 is required by {'scikit-image'}
  $ pip install scipy -U
    ERROR: pip's dependency resolver does not currently take into account all the packages that are installed. This behaviour is the source of the following dependency conflicts.
  opencood 0.1.0 requires matplotlib~=3.3.3, but you have matplotlib 3.7.1 which is incompatible.
  opencood 0.1.0 requires opencv-python~=4.5.1.48, but you have opencv-python 4.7.0.72 which is incompatible.
  opencood 0.1.0 requires scipy~=1.5.4, but you have scipy 1.10.1 which is incompatible.
  Successfully installed scipy-1.10.1


  


