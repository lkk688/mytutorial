Nuscenes
=============


Nuscenes Data
---------------------
Full nuScenes dataset has 1,000 scenes (20s duration each) includes approximately 1.4M camera images, 390k LIDAR sweeps, 1.4M RADAR sweeps and 1.4M object bounding boxes in 40k keyframes. Annotation instruction: https://github.com/nutonomy/nuscenes-devkit/blob/master/docs/instructions_nuscenes.md. It provide data from the entire sensor suite of an autonomous vehicle
    * 6 cameras (Basler acA1600-60gc): 12Hz capture frequency, 1600x900 ROI, surround view, one camera facing back
    * 1 LIDAR: Velodyne HDL32E, 20Hz capture frequency, 32 beams, 1080 (+-10) points per ring, Usable returns up to 70 meters, ± 2 cm accuracy, Up to ~1.39 Million Points per Second
    * 5 RADAR (Continental ARS 408-21): 13Hz capture frequency, 77GHz, Up to 250m distance, Independently measures distance and velocity in one cycle using Frequency Modulated Continuous Wave
    * GPS and IMU (https://www.advancednavigation.com/inertial-navigation-systems/mems-gnss-ins/spatial/) Position accuracy of 20mm

Extrinsic coordinates are expressed relative to the **ego frame**, i.e. the midpoint of the rear vehicle axle. The cameras run at 12Hz while the LIDAR runs at 20Hz. The 12 camera exposures are spread as evenly as possible across the 20 LIDAR scans, so not all LIDAR scans have a corresponding camera frame. All annotations and meta data (including calibration, maps, vehicle coordinates etc.) are covered in a relational database.

In nuScenes-lidarseg, each lidar point from a keyframe in nuScenes with one of 32 possible semantic labels (i.e. lidar semantic segmentation). nuScenes-lidarseg contains 1.4 billion annotated points across 40,000 pointclouds and 1000 scenes (850 scenes for training and validation, and 150 scenes for testing).

Download Nuscenes data from https://www.nuscenes.org/nuscenes, 

untar the mini.tgz sample data, it will create four folders: "maps", "samples", "sweeps", and "v1.0-mini"
.. code-block:: console

    D:\Data\Nuscenes> tar zxvf .\v1.0-mini.tgz