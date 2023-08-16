NVIDIA TensorRT
===============

Installation
--------------

Ref: https://docs.nvidia.com/deeplearning/tensorrt/install-guide/index.html

Tested in Alienware WSL2 Linux via Tar File Installation

add the following two lines into "~/.bashrc"

.. code-block:: console

    export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:~/Developer/TensorRT-8.6.0.12/lib
    export PATH=$PATH:~/Developer/TensorRT-8.6.0.12/bin

DEEPDATAMINGLEARNING/pytorch/tensorrt.ipynb

INSTALLING C++ DISTRIBUTIONS OF PYTORCH: https://pytorch.org/cppdocs/installing.html

.. code-block:: console

    (mypy310) lkk@Alienware-LKKi7G8:~/Developer$ sudo apt install unzip
    (mypy310) lkk@Alienware-LKKi7G8:~/Developer$ wget https://download.pytorch.org/libtorch/nightly/cpu/libtorch-shared-with-deps-latest.zip
    unzip libtorch-shared-with-deps-latest.zip

    (mypy310) lkk@Alienware-LKKi7G8:~/Developer/libtorch$ ls
    bin  build-hash  build-version  include  lib  share
    (mypy310) lkk@Alienware-LKKi7G8:~/Developer/libtorch$ pwd
    /home/lkk/Developer/libtorch

Download https://github.com/NVIDIA/TensorRT/tree/main to "~/Developer/TensorRT"


.. code-block:: console

    export TensorRT_LIBRARY=~/Developer/TensorRT-8.6.0.12/lib
    export TensorRT_INCLUDE_DIR=~/Developer/TensorRT-8.6.0.12/include
    (mypy310) lkk@Alienware-LKKi7G8:~/Developer/TensorRT/build$ echo $TRT_LIBPATH
    /home/lkk/Developer/TensorRT-8.6.0.12
    (mypy310) lkk@Alienware-LKKi7G8:~/Developer/TensorRT/build$ echo TRT_LIB_DIR=/home/lkk/Developer/TensorRT-8.6.0.12
    TRT_LIB_DIR=/home/lkk/Developer/TensorRT-8.6.0.12
    (mypy310) lkk@Alienware-LKKi7G8:~/Developer/TensorRT/build$ cmake .. -DTRT_LIB_DIR=$TRT_LIBPATH -DTensorRT_LIBRARY=$TensorRT_LIBRARY -DTensorRT_INCLUDE_DIR=$TensorRT_INCLUDE_DIR -DCMAKE_PREFIX_PATH=/home/lkk/Developer/libtorch -DTRT_OUT_DIR=`pwd`/out
    (mypy310) lkk@Alienware-LKKi7G8:~/Developer/TensorRT/build$ cmake -DCMAKE_PREFIX_PATH=/home/lkk/Developer/libtorch -DTRT_LIB_DIR=$TRT_LIBPATH/lib/ -DTensorRT_LIBRARY=$TensorRT_LIBRARY ..
    -- Generating done
    -- Build files have been written to: /home/lkk/Developer/TensorRT/build
    (mypy310) lkk@Alienware-LKKi7G8:~/Developer/TensorRT/build$ make -j4
    (mypy310) lkk@Alienware-LKKi7G8:~/Developer/TensorRT/build$ ls samples
    (mypy310) lkk@Alienware-LKKi7G8:~/Developer/TensorRT/build$ ./sample_onnx_mnist -d ~/Developer/TensorRT-8.6.0.12/data/mnist/
    &&&& PASSED TensorRT.sample_onnx_mnist [TensorRT v8600] # ./sample_onnx_mnist -d /home/lkk/Developer/TensorRT-8.6.0.12/data/mnist/
    (mypy310) lkk@Alienware-LKKi7G8:~/Developer/TensorRT/build$ cp /home/lkk/Developer/TensorRT-8.6.0.12/data/mnist/*.pgm ./
    mymodels/
    (mypy310) lkk@Alienware-LKKi7G8:~/Developer/TensorRT/build$ ./sample_onnx_mnist -d /home/lkk/Developer/TensorRT/build/mymodels
    &&&& PASSED TensorRT.sample_onnx_mnist [TensorRT v8600] # ./sample_onnx_mnist -d /home/lkk/Developer/TensorRT/build/mymodels

Our own "TRTdetector" repo:

.. code-block:: console

    (mypy310) lkk@Alienware-LKKi7G8:~/Developer/TRTdetector/libtorchexample/build$ cmake -DCMAKE_PREFIX_PATH=/home/lkk/Developer/libtorch ..
    (mypy310) lkk@Alienware-LKKi7G8:~/Developer/TRTdetector/libtorchexample/build$ cmake --build . --config Release
    (mypy310) lkk@Alienware-LKKi7G8:~/Developer/TRTdetector/libtorchexample/build$ cmake -DCMAKE_PREFIX_PATH=`python -c 'import torch;print(torch.utils.cmake_prefix_path)'` ..
    (mypy310) lkk@Alienware-LKKi7G8:~/Developer/TRTdetector/libtorchexample/build$ ./example-app
    0.3184  0.8318  0.8634
    0.5522  0.2695  0.4220
    [ CPUFloatType{2,3} ]



https://developer.nvidia.com/tensorrt-getting-started

https://docs.nvidia.com/deeplearning/tensorrt/sample-support-guide/index.html

https://github.com/NVIDIA/TensorRT/tree/main/samples