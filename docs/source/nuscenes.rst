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

Download Nuscenes data from https://www.nuscenes.org/nuscenes, untar the mini.tgz sample data, it will create four folders: "maps", "samples", "sweeps", and "v1.0-mini"

Install nuScenes development kit

.. code-block:: console

    tar zxvf .\v1.0-mini.tgz
    pip install nuscenes-devkit

Check nuscenes tutorial in mydetector3d/datasets/nuscenes/nuscenes_tutorial.ipynb

.. code-block:: console

    from nuscenes.nuscenes import NuScenes
    nusc = NuScenes(version='v1.0-mini', dataroot='/data/cmpe249-fa22/nuScenes/nuScenesv1.0-mini', verbose=True)
    nusc.scene[0] #each scene is 20s sequence with 'token', 'name', 'first_sample_token', 'last_sample_token'

Untar the full nuScenes dataset in HPC:

.. code-block:: console

    (mycondapy39) [010796032@coe-hpc2 nuScenes]$ tar zxvf v1.0-trainval01_blobs.tgz
    $ tar zxvf v1.0-trainval02_blobs.tgz
    $ tar zxvf v1.0-trainval03_blobs.tgz
    $ tar zxvf v1.0-trainval04_blobs.tgz
    $ tar zxvf v1.0-trainval05_blobs.tgz
    $ tar zxvf v1.0-trainval06_blobs.tgz
    $ tar zxvf v1.0-trainval07_blobs.tgz
    $ tar zxvf v1.0-trainval08_blobs.tgz
    $ tar zxvf v1.0-trainval09_blobs.tgz
    $ tar zxvf v1.0-trainval10_blobs.tgz
    (mycondapy39) [010796032@cs001 nuScenes]$ tar zxvf v1.0-trainval_meta.tgz
    (mycondapy39) [010796032@coe-hpc2 nuScenes]$ ls samples/
    CAM_BACK       CAM_BACK_RIGHT  CAM_FRONT_LEFT   LIDAR_TOP        RADAR_BACK_RIGHT  RADAR_FRONT_LEFT
    CAM_BACK_LEFT  CAM_FRONT       CAM_FRONT_RIGHT  RADAR_BACK_LEFT  RADAR_FRONT       RADAR_FRONT_RIGHT
    (mycondapy39) [010796032@coe-hpc2 nuScenes]$ ls sweeps
    CAM_BACK       CAM_BACK_RIGHT  CAM_FRONT_LEFT   LIDAR_TOP        RADAR_BACK_RIGHT  RADAR_FRONT_LEFT
    CAM_BACK_LEFT  CAM_FRONT       CAM_FRONT_RIGHT  RADAR_BACK_LEFT  RADAR_FRONT       RADAR_FRONT_RIGHT
    (mycondapy39) [010796032@cs001 nuScenes]$ ls maps/
    36092f0b03a857c6a3403e25b4b7aab3.png  53992ee3023e5494b90c316c183be829.png
    37819e65e09e5547b8a3ceaefba56bb2.png  93406b464a165eaba6d9de76ca09f5da.png
    (mycondapy39) [010796032@cs001 nuScenes]$ ls v1.0-trainval
    attribute.json          category.json  instance.json  map.json                sample_data.json  scene.json   visibility.json
    calibrated_sensor.json  ego_pose.json  log.json       sample_annotation.json  sample.json       sensor.json

    sweeps/RADAR_FRONT/n008-2018-08-01-15-52-19-0400__RADAR_FRONT__1533153432872720.pcd
    .v1.0-trainval02_blobs.txt

Put all folders inside the "v1.0-trainval", and run **create_nuscenes_infos** in "/home/010796032/3DObject/3DDepth/mydetector3d/datasets/nuscenes/nuscenes_dataset.py" to generate info.pkl files

.. code-block:: console

    (mycondapy39) [010796032@cs001 nuScenes]$ ls v1.0-trainval
    maps  nuscenes_infos_10sweeps_train.pkl  nuscenes_infos_10sweeps_val.pkl  samples  sweeps  v1.0-trainval

Run "create_groundtruth" in "nuscenes_dataset.py" to generate groundtruth folder:

.. code-block:: console

    3DDepth/mydetector3d/datasets/nuscenes/nuscenes_dataset.py 
    ======
    Loading NuScenes tables for version v1.0-trainval...
    23 category,
    8 attribute,
    4 visibility,
    64386 instance,
    12 sensor,
    10200 calibrated_sensor,
    2631083 ego_pose,
    68 log,
    850 scene,
    34149 sample,
    2631083 sample_data,
    1166187 sample_annotation,
    4 map,
    Done loading in 25.048 seconds.
    2023-05-21 08:46:41,467   INFO  Total samples for NuScenes dataset: 28130
    Database traffic_cone: 62964
    Database truck: 65262
    Database car: 339949
    Database pedestrian: 161928
    Database ignore: 26297
    Database construction_vehicle: 11050
    Database barrier: 107507
    Database motorcycle: 8846
    Database bicycle: 8185
    Database bus: 12286
    Database trailer: 19202

Each dbinfo is 

.. code-block:: console

    gt_points.tofile(f) #saved 
    db_info = {'name': gt_names[i], 'path': db_path, 'image_idx': sample_idx, 'gt_idx': i,
                                'box3d_lidar': gt_boxes[i], 'num_points_in_gt': gt_points.shape[0]}

After untar, "samples" folder is created for sensor data for keyframes (annotated images), "sweeps" folder is created for sensor data for intermediate frames (unannotated images), .v1.0-trainvalxx_blobs.txt (01-10) files are JSON tables that include all the meta data and annotation. 

Training
---------------------

'mydetector3d/tools/cfgs/nuscenes_models/bevfusion.yaml'

'mydetector3d/tools/cfgs/nuscenes_models/cbgs_pp_multihead.yaml'

BEVFusion
---------------------
Add bevfusion

Model forward process

MeanVFE
  * Input: voxel_features([600911, 10, 5]), voxel_num_points([600911]) = batch_dict['voxels'], batch_dict['voxel_num_points']
  * Output; batch_dict['voxel_features'] = points_mean.contiguous() #[600911, 5]

VoxelResBackBone8x
  * Input: voxel_features([600911, 5]), voxel_coords([600911, 4]) = batch_dict['voxel_features'], batch_dict['voxel_coords']
  * Output: batch_dict: 'encoded_spconv_tensor': out([2, 180, 180]), 'encoded_spconv_tensor_stride': 8, 'multi_scale_3d_features'

HeightCompression
  * Input: encoded_spconv_tensor = batch_dict['encoded_spconv_tensor'] #Sparse [2, 180, 180]
  * Output: batch_dict['spatial_features'] = spatial_features #[6, 256, 180, 180], batch_dict['spatial_features_stride']=8

SwinTransformer
  * Input: x = batch_dict['camera_imgs'] #[6, 6, 3, 256, 704]
  * Out: batch_dict['image_features'] = outs #3 items: [36, 192, 32, 88], [36, 384, 16, 44], [36, 768, 8, 22] 

GeneralizedLSSFPN
  * inputs = batch_dict['image_features']
  * Output: batch_dict['image_fpn'] = tuple(outs) #2 items: [36, 256, 32, 88], [36, 256, 16, 44]

DepthLSSTransform (lists images into 3D and then splats onto bev features, from https://github.com/mit-han-lab/bevfusion/)
  * x = batch_dict['image_fpn']  #img=[6, 6, 256, 32, 88] 
  * points = batch_dict['points'] # [1456967, 6]
  * Output: batch_dict['spatial_features_img'] = x #[6, 80, 180, 180]

ConvFuser
  * Input: img_bev = batch_dict['spatial_features_img']#[6, 80, 180, 180], lidar_bev = batch_dict['spatial_features']#[6, 256, 180, 180]
  * cat_bev = torch.cat([img_bev,lidar_bev],dim=1)
  * Output: batch_dict['spatial_features'] = mm_bev #[6, 256, 180, 180]

BaseBEVBackbone
  * Input: spatial_features = data_dict['spatial_features'] #[6, 256, 180, 180]
  * data_dict['spatial_features_2d'] = x #[6, 512, 180, 180]

TransFusionHead
  * Input: feats = batch_dict['spatial_features_2d'] #[6, 512, 180, 180]
  * res = self.predict(feats) #'center' [6, 2, 200]; 'height' [6, 1, 200]; 'dim' [6, 3, 200]; 'rot' [6, 2, 200]; 'vel' [6, 2, 200]; 'heatmap' [6, 10, 200]; 'query_heatmap_score' [6, 10, 200]; 'dense_heatmap' [6, 10, 180, 180]
  * loss, tb_dict = self.loss(gt_bboxes_3d [6, 51, 9], gt_labels_3d [6, 51], res)