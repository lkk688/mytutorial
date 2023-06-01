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
  (base) kaikailiu@kaikais-mbp ~ % conda create --name mycondapy310
  (base) kaikailiu@kaikais-mbp ~ % conda activate mycondapy310
  (mycondapy310) kaikailiu@kaikais-mbp ~ % conda info --envs
  

Pytorch on Mac
--------------
Reference links:
  * https://developer.apple.com/metal/
  * https://developer.apple.com/metal/pytorch/
  * https://mac.install.guide/homebrew/index.html
