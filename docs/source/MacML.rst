Mac Machine Learning
====================
In Mac with Apple silicon, if want to install Rosetta 2 manually from the command line, run the following command:

.. code-block:: console

  softwareupdate --install-rosetta

Install https://www.xquartz.org/releases/ for X11 window forwarding.

Conda Installation
------------------

.. code-block:: console

  kaikailiu@kaikais-mbp Developer % curl -O https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-arm64.sh
  kaikailiu@kaikais-mbp Developer % sh Miniconda3-latest-MacOSX-arm64.sh
  #install to /Users/kaikailiu/miniconda3
  (base) kaikailiu@kaikais-mbp ~ % python3 -V
  Python 3.10.10
  (base) kaikailiu@kaikais-mbp ~ % conda --version
  conda 23.3.1
  (base) kaikailiu@kaikais-mbp ~ % conda update conda

Option1: Create a conda environment based on system's python:

.. code-block:: console

  (base) kaikailiu@kaikais-mbp ~ % conda create --name mycondapy310
  (base) kaikailiu@kaikais-mbp ~ % conda activate mycondapy310
  (mycondapy310) kaikailiu@kaikais-mbp ~ % conda info --envs
  % which pip3              
  /usr/bin/pip3
  % which python3
  /usr/bin/python3
  % python3 --version
  Python 3.9.6

Option2 (recommended): Create a conda environment and install python in this environment: 

.. code-block:: console

  (base) kaikailiu@kaikais-mbp docs % conda create --name mypy310 python=3.10 
  (base) kaikailiu@kaikais-mbp docs % conda activate mypy310
  (mypy310) kaikailiu@kaikais-mbp docs % python3 --version
  Python 3.10.11
  (mypy310) kaikailiu@kaikais-mbp docs % which python3
  /Users/kaikailiu/miniconda3/envs/mypy310/bin/python3
  (mypy310) kaikailiu@kaikais-mbp docs % which pip3
  /Users/kaikailiu/miniconda3/envs/mypy310/bin/pip3

Install Mytutorial
------------------

Install in mycondapy310 (use system's python3)
.. code-block:: console

  (mycondapy310) kaikailiu@kaikais-mbp MyRepo % pwd
  /Users/kaikailiu/Documents/MyRepo
  (mycondapy310) kaikailiu@kaikais-mbp MyRepo % git clone https://github.com/lkk688/mytutorial.git
  (mycondapy310) kaikailiu@kaikais-mbp mytutorial % pip3 install -r requirements.txt
  WARNING: The scripts myst-anchors, myst-docutils-demo, myst-docutils-html, myst-docutils-html5, myst-docutils-latex, myst-docutils-pseudoxml, myst-docutils-xml and myst-inv are installed in '/Users/kaikailiu/Library/Python/3.9/bin' which is not on PATH.
  (mycondapy310) kaikailiu@kaikais-mbp docs % /Users/kaikailiu/Library/Python/3.9/bin/sphinx-build -b html source build
  Running Sphinx v6.2.1

  Extension error:
  Could not import extension sphinx.builders.linkcheck (exception: urllib3 v2.0 only supports OpenSSL 1.1.1+, currently the 'ssl' module is compiled with LibreSSL 2.8.3. See: https://github.com/urllib3/urllib3/issues/2168)
  #urllib3                       2.0.2
  (mycondapy310) kaikailiu@kaikais-mbp docs % pip3 uninstall urllib3
  Found existing installation: urllib3 2.0.2
  (mycondapy310) kaikailiu@kaikais-mbp docs % python3 -m pip install urllib3==1.26.6
  % /Users/kaikailiu/Library/Python/3.9/bin/sphinx-build -b html source build
  build succeeded

Install in mypy310 (python3 in conda): 

.. code-block:: console

  (mypy310) kaikailiu@kaikais-mbp mytutorial % pip3 install -r requirements.txt
  (mypy310) kaikailiu@kaikais-mbp mytutorial % cd docs                         
  (mypy310) kaikailiu@kaikais-mbp docs % sphinx-build -b html source build

Git configure
-------------

.. code-block:: console

  (base) kaikailiu@kaikais-mbp mytutorial % git config --global user.email "kaikai.liu@sjsu.edu"
  (base) kaikailiu@kaikais-mbp mytutorial % git config --global user.name "Kaikai Liu"

Pytorch on Mac
--------------
Reference links:
  * https://developer.apple.com/metal/
  * https://developer.apple.com/metal/pytorch/
  * https://mac.install.guide/homebrew/index.html

Install pytorch 2.0 and perform pytorch test

.. code-block:: console

  (mypy310) kaikailiu@kaikais-mbp docs % conda install pytorch::pytorch torchvision torchaudio -c pytorch
  (mypy310) kaikailiu@kaikais-mbp mytutorial % python ./scripts/testmacpytorch.py 

Streamlit
---------
Ref: https://docs.streamlit.io/library/get-started/installation

.. code-block:: console

  pip install streamlit
  (mypy310) kaikailiu@kaikais-mbp MyRepo % streamlit hello
  2023-06-01 14:37:25.741 cannot import name 'COMMON_SAFE_ASCII_CHARACTERS' from 'charset_normalizer.constant' (/Users/kaikailiu/miniconda3/envs/mypy310/lib/python3.10/site-packages/charset_normalizer/constant.py)
  % pip install chardet #solve the previous problem
  % streamlit hello 
  # streamlit run your_script.py [-- script args]

NuScenes
---------
.. code-block:: console

  % pip install nuscenes-devkit
  from nuscenes.nuscenes import NuScenes

Install Docker Desktop on Mac
------------------------------
Docker: https://docs.docker.com

Download Docker.dmg from: https://docs.docker.com/desktop/install/mac-install/, double click to install.

Open the Docker app in Applications, select Use recommended settings (Requires password) to finish setup. 

In Docker app, select ubuntu image, or pull ubuntu image in command line:

.. code-block:: console

  % docker pull ubuntu:22.04
  % docker images
  REPOSITORY   TAG       IMAGE ID       CREATED       SIZE
  ubuntu       22.04     2767693332e5   10 days ago   69.2MB
  (base) kaikailiu@kaikais-mbp Developer % docker run -it --rm -v /Users/kaikailiu/Documents/:/Documents --privileged --network host ubuntu:22.04 /bin/bash
  root@docker-desktop:/# ls 
  Documents  boot  etc   lib    mnt  proc  run   srv  tmp  var
  bin        dev   home  media  opt  root  sbin  sys  usr
  root@docker-desktop:/# cat /etc/os-release 
  PRETTY_NAME="Ubuntu 22.04.2 LTS"
  NAME="Ubuntu"
  VERSION_ID="22.04"
  VERSION="22.04.2 LTS (Jammy Jellyfish)"

Build own docker image based on Dockerfile (under scripts):

.. code-block:: console

  (base) kaikailiu@kaikais-mbp scripts % docker build -t myubuntu22 .
  Building 510.4s (14/14) FINISHED
  => naming to docker.io/library/myubuntu22
  (base) kaikailiu@kaikais-mbp scripts % docker images               
  REPOSITORY   TAG       IMAGE ID       CREATED          SIZE
  myubuntu22   latest    490661a304a9   23 minutes ago   1.09GB
  ubuntu       22.04     2767693332e5   10 days ago      69.2MB
  (base) kaikailiu@kaikais-mbp scripts % docker run -it --rm -v /Users/kaikailiu/Documents/:/Documents --privileged --network host myubuntu22 /bin/bash
  root@docker-desktop:/# python -V
  Python 3.10.6

If you docker pull an image from the registry, it will again default to your native architecture (if available), unless you specify --platform=linux/amd64.

https://www.docker.com/products/telepresence-for-docker/

open3d
------

.. code-block:: console

  (mypy310) kaikailiu@kaikais-mbp MyRepo % pip install open3d  
  Collecting open3d
    Downloading open3d-0.17.0-cp310-cp310-macosx_13_0_arm64.whl (39.9 MB)
  % python -c "import open3d; print(open3d.__version__)"
  from open3d.cpu.pybind import (core, camera, data, geometry, io, pipelines,
  ImportError: dlopen(/Users/kaikailiu/miniconda3/envs/mypy310/lib/python3.10/site-packages/open3d/cpu/pybind.cpython-310-darwin.so, 0x0002): Library not loaded: /opt/homebrew/opt/libomp/lib/libomp.dylib
  % pip uninstall open3d

One possible solution: https://github.com/isl-org/open3d_downloads/releases/tag/apple-silicon

(mypy310) kaikailiu@kaikais-mbp Developer % git clone https://github.com/isl-org/Open3D

http://www.open3d.org/docs/release/arm.html

Packages cannot be installed
----------------------------
.. code-block:: console

  pip install mayavi #VTK error
 
 Try conda installation

.. code-block:: console

  % conda install -c conda-forge vtk #https://anaconda.org/conda-forge/vtk
  % conda install -c anaconda mayavi #does not work
  #python version problem python[version='>=3.8,<3.9.0a0|>=3.9,<3.10.0a0']
  % conda install -c conda-forge mayavi #works
  (mypy310) kaikailiu@kaikais-mbp scripts % python testmayavi.py