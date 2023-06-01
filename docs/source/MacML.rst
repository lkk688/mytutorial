Mac Machine Learning
====================

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

Pytorch on Mac
--------------
Reference links:
  * https://developer.apple.com/metal/
  * https://developer.apple.com/metal/pytorch/
  * https://mac.install.guide/homebrew/index.html
