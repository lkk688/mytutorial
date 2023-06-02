# docker build -t myros2ubuntu22cuda117 .

ARG BASE_IMAGE=ubuntu:22.04
FROM ${BASE_IMAGE}

# disable terminal interaction for apt
ENV DEBIAN_FRONTEND=noninteractive
ENV SHELL /bin/bash
SHELL ["/bin/bash", "-c"] 

# Fundamentals
RUN apt-get update && apt-get install -y \
        apt-transport-https \
        bash-completion \
        build-essential \
        ca-certificates \
        clang-format \
        cmake \
        curl \
        git \
        gnupg2 \
        locales \
        lsb-release \
        rsync \
        software-properties-common \
        wget \
        vim \
        unzip \
        mlocate \
	libgoogle-glog-dev \
        x11-apps \
&& rm -rf /var/lib/apt/lists/* \
&& apt-get clean

# Set Python3 as default
RUN update-alternatives --install /usr/bin/python python /usr/bin/python3 1

# Python basics
RUN apt-get update && apt-get install -y \
        python3-pip \
        python3-pybind11 \
        python3-pytest-cov \
        python3-setuptools \
&& rm -rf /var/lib/apt/lists/* \
&& apt-get clean

        
# Python3 (PIP)
RUN python3 -m pip install -U \
        argcomplete \
        autopep8 \
        flake8==4.0.1 \
        flake8-blind-except \
        flake8-builtins \
        flake8-class-newline \
        flake8-comprehensions \
        flake8-deprecated \
        flake8-docstrings \
        flake8-import-order \
        flake8-quotes \
        onnx \
        pytest-repeat \
        pytest-rerunfailures \
        pytest \
        pydocstyle \
        scikit-learn

# Install Git-LFS
RUN curl -s https://packagecloud.io/install/repositories/github/git-lfs/script.deb.sh | bash && \
        apt-get update && apt-get install -y \
        git-lfs \
&& rm -rf /var/lib/apt/lists/* \
&& apt-get clean


# User setting --------------------------
# Setup non-root admin user
ARG USERNAME=admin
ARG USER_UID=1000
ARG USER_GID=1000

# Install prerequisites
RUN apt-get update && apt-get install -y \
        sudo \
&& rm -rf /var/lib/apt/lists/* \
&& apt-get clean

# Create the 'admin' user if not already exists
RUN if [ ! $(getent passwd ${USERNAME}) ]; then \
        groupadd --gid ${USER_GID} ${USERNAME} ; \
        useradd --uid ${USER_UID} --gid ${USER_GID} -m ${USERNAME} ; \
    fi

# Update 'admin' user
RUN echo ${USERNAME} ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/${USERNAME} \
    && chmod 0440 /etc/sudoers.d/${USERNAME} \
    && adduser ${USERNAME} video && adduser ${USERNAME} sudo

# Copy scripts
RUN mkdir -p /usr/local/bin/scripts
# COPY scripts/*entrypoint.sh /usr/local/bin/scripts/
# RUN  chmod +x /usr/local/bin/scripts/*.sh

ENV USERNAME=${USERNAME}
ENV USER_GID=${USER_GID}
ENV USER_UID=${USER_UID}