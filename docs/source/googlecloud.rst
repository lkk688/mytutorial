GoogleCloud
============

.. _googlecloud:

Gcloud CLI
-----------
https://cloud.google.com/sdk/gcloud

Install the gcloud CLI: 

.. code-block:: console

    % xhost +localhost
    % docker run -e DISPLAY=docker.for.mac.host.internal:0 -it --rm -v /Users/kaikailiu/Documents/:/Documents --privileged --network host myubuntu22 /bin/bash
    root@docker-desktop:/# sudo apt-get update
    root@docker-desktop:/# sudo apt-get install apt-transport-https ca-certificates gnupg curl sudo
    root@docker-desktop:/# echo "deb [signed-by=/usr/share/keyrings/cloud.google.gpg] https://packages.cloud.google.com/apt cloud-sdk main" | sudo tee -a /etc/apt/sources.list.d/google-cloud-sdk.list
    root@docker-desktop:/# curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key --keyring /usr/share/keyrings/cloud.google.gpg add -
    root@docker-desktop:/# sudo apt-get update && sudo apt-get install google-cloud-cli
    root@docker-desktop:/# gcloud --version
    Google Cloud SDK 436.0.0
    alpha 2023.06.16
    beta 2023.06.16
    bq 2.0.93
    bundled-python3-unix 3.9.16
    core 2023.06.16
    gcloud-crc32c 1.0.0
    gsutil 5.24

Install any of the following additional components:

.. code-block:: console

    root@docker-desktop:/# sudo apt-get install google-cloud-cli google-cloud-cli-app-engine-python

Run gcloud init to authorizes the gcloud CLI to use your user account credentials to access Google Cloud and select the project:

.. code-block:: console

    root@docker-desktop:/# gcloud init
    root@docker-desktop:/# gcloud config list 
    [core]
    account = kaikai.liu@sjsu.edu
    disable_usage_reporting = True
    project = sjsu-rf-ohana

    Your active configuration is: [default]

https://cloud.google.com/compute/docs/gcloud-compute#set_default_zone_and_region_in_your_local_client

.. code-block:: console

    root@docker-desktop:/# gcloud compute project-info describe --project sjsu-rf-ohana
    root@docker-desktop:/# gcloud config get-value compute/region
    root@docker-desktop:/# gcloud config get-value compute/zone
    root@docker-desktop:/# gcloud compute regions list
    root@docker-desktop:/# gcloud compute zones list
    root@docker-desktop:/# gcloud compute project-info add-metadata \
    --metadata google-compute-default-region=us-west1,google-compute-default-zone=us-west1-a
    Updated [https://www.googleapis.com/compute/v1/projects/sjsu-rf-ohana].
    root@docker-desktop:/# gcloud init
    root@docker-desktop:/# gcloud config get-value compute/region
    us-west1
    root@docker-desktop:/# gcloud config get-value compute/zone
    us-west1-a
    gcloud config set compute/region REGION
    gcloud config set compute/zone ZONE

Compute Engine
---------------

https://cloud.google.com/compute/docs

Create and start a VM instance: https://cloud.google.com/compute/docs/instances/create-start-instance

.. code-block:: console

    gcloud compute images list

    NAME PROJECT FAMILY
    ubuntu-minimal-2204-jammy-v20230617                   

    gcloud compute images describe ubuntu-minimal-2204-jammy-v20230617  \
        --project=ubuntu-os-cloud


    root@docker-desktop:/# gcloud compute instances create myubuntu22 \
        --image=ubuntu-minimal-2204-jammy-v20230617 \
        --image-project=ubuntu-os-cloud

    Created [https://www.googleapis.com/compute/v1/projects/sjsu-rf-ohana/zones/us-west1-a/instances/myubuntu22].
    NAME        ZONE        MACHINE_TYPE   PREEMPTIBLE  INTERNAL_IP  EXTERNAL_IP    STATUS
    myubuntu22  us-west1-a  n1-standard-1               10.138.0.2   34.145.90.176  RUNNING

    root@docker-desktop:/# gcloud compute instances describe myubuntu22

You use the gcloud compute ssh command to connect to your VM.

.. code-block:: console

    # gcloud compute ssh myubuntu22 --project=sjsu-rf-ohana --zone=us-west1-a --troubleshoot
    root@docker-desktop:~/.ssh# ssh -i google_compute_engine kaikai_liu@34.145.90.176
    kaikai_liu@34.145.90.176: Permission denied (publickey).

Add keys to VMs that use OS Login: https://cloud.google.com/compute/docs/connect/add-ssh-keys#os-login

.. code-block:: console

    root@docker-desktop:~/.ssh# pwd
    /root/.ssh
    root@docker-desktop:~/.ssh# gcloud compute os-login ssh-keys add --key-file=/root/.ssh/google_compute_engine.pub

    #Add SSH keys to instance metadata during VM creation
    gcloud compute instances create VM_NAME \
    --metadata=ssh-keys=PUBLIC_KEY

    #Add SSH keys to instance metadata after VM creation
    root@docker-desktop:~/.ssh# gcloud compute instances describe myubuntu22

    #https://cloud.google.com/compute/docs/connect/create-ssh-keys
    root@docker-desktop:~/.ssh# ssh-keygen -t rsa -f google_compute -C kaikai_liu -b 2048

    root@docker-desktop:~/.ssh# gcloud compute os-login ssh-keys add --key-file=google_compute.pub 

    root@docker-desktop:~/.ssh# gcloud compute ssh myubuntu22

    root@docker-desktop:/# gcloud compute machine-types list --zones us-west1-a
    NAME              ZONE        CPUS  MEMORY_GB
    c2-standard-4     us-west1-a  4     16.00

    gcloud compute instances create myubuntu22 \
        --image=ubuntu-minimal-2204-jammy-v20230617 \
        --image-project=ubuntu-os-cloud
        --machine-type=c2-standard-4