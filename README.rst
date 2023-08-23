Collection of My tutorials from Kaikai Liu
=======================================

This GitHub repository includes multiple tutorials
with some basic Sphinx docs.

Read the tutorial here: https://mytutorial-lkk.readthedocs.io/en/latest/

Activate python virtual environment, build the document under the docs folder via 'make' or 'sphinx-build -b html source build'

.. code-block:: console

  sudo apt install make
  (mycondapy310) PS D:\Developer\mytutorial> pip install -r requirements.txt
    mytutorial/docs$ make html

If in Mac environment, make does not work, you can use 'sphinx-build' command to build the document

.. code-block:: console

  (mypy310) kaikailiu@kaikais-mbp docs % sphinx-build -b html source build

The generated html files are in the folder of "build"