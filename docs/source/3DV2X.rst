3D V2X Data
=============
DAIR-V2X Cooperative Dataset (DAIR-V2X-C) (from https://thudair.baai.ac.cn/cooptest) contains 18330 frames of infrastructure multi-modality data (point cloud & image), 20515 frames of vehicle multi-modality data (point cloud & image), 2D & 3D joint annotation files of raw data, calibration files, and timestamp files. DAIR-V2X-C can be used for Vehicle-Infrastructure Cooperative (VIC) 3D object detection to improve environmental perception performance in autonomous driving.

2D and 3D bounding boxes of the obstacle objects are provided as well as their category attributes, occlusion states, and truncated states in the annotation. There are total 10 object classes: Car, Truck, Van, Bus, Pedestrian, Cyclist, Tricyclist, Motorcyclist, Barrowlist, TrafficCone. 3D bounding box in the Lidar/Virtual Lidar coordinate system including height, width, length, x_loc, y_loc, z_loc, rotation.

DAIR-V2X Dependencies
---------------------
Use `DAIR-V2X <https://github.com/AIR-THU/DAIR-V2X/tree/main>`_ to read the Lidar pcd file in cooperative sensing dataset. Install the following required packages

.. code-block:: console

  (mypy310) lkk@Alienware-LKKi7G8:~/Developer$ git clone https://github.com/klintan/pypcd.git
  (mypy310) lkk@Alienware-LKKi7G8:~/Developer/pypcd$ python setup.py install

Create a new folder named "dairv2x" under "mydetector3d/datasets/dairv2x"


DAIR V2X Dataset Process
------------------------
DAIR V2X dataset is saved in '/data/cmpe249-fa22/DAIR-C' folder. Based on 'https://github.com/AIR-THU/DAIR-V2X/blob/main/docs/get_started.md', 
  * 'cooperative-vehicle-infrastructure' folder as the follow three sub-folders: cooperative  infrastructure-side  vehicle-side
  * 'infrastructure-side' and 'vehicle-side' has 'image', 'velodyne', 'calib', and 'label', and data_info.json as follows. 
  * 'vehicle-side' label is in **Vehicle LiDAR Coordinate System**, while 'infrastructure-side' label is in **Infrastructure Virtual LiDAR Coordinate System**

    ├── infrastructure-side             # DAIR-V2X-C-I
        ├── image		    
            ├── {id}.jpg
        ├── velodyne                
            ├── {id}.pcd           
        ├── calib                 
            ├── camera_intrinsic            
                ├── {id}.json     
            ├── virtuallidar_to_world   
                ├── {id}.json      
            ├── virtuallidar_to_camera  
                ├── {id}.json      
        ├── label	
            ├── camera                  # Labeled data in Infrastructure Virtual LiDAR Coordinate System fitting objects in image based on image frame time
                ├── {id}.json
            ├── virtuallidar            # Labeled data in Infrastructure Virtual LiDAR Coordinate System fitting objects in point cloud based on point cloud frame time
                ├── {id}.json
        ├── data_info.json              # Relevant index information of Infrastructure data


 * The 'cooperative' folder contains the following files
    ├── cooperative                     # Coopetative Files
        ├── label_world                 # Vehicle-Infrastructure Cooperative (VIC) Annotation files
            ├── {id}.json           
        ├── data_info.json              # Relevant index information combined the Infrastructure data and the Vehicle data


There are four data folders under root '/data/cmpe249-fa22/DAIR-C':
 * 'cooperative-vehicle-infrastructure-vehicle-side-image' folder contains all images (6digit_id.jpg) in vehicle side.
 * 'cooperative-vehicle-infrastructure-vehicle-side-velodyne' folder contains all lidar files (6digit_id.pcd) in vehicle side.
 * 'cooperative-vehicle-infrastructure-infrastructure-side-image' folder contains all images (6digit_id.jpg) in infrastructure side.
 * 'cooperative-vehicle-infrastructure-infrastructure-side-velodyne' folder contains all lidar files (6digit_id.pcd) in infrastructure side.
 
 
Copy the split data (json files in 'https://github.com/AIR-THU/DAIR-V2X/tree/main/data/split_datas') to the data folder ('/data/cmpe249-fa22/DAIR-C')

Use 'mydetector3d/tools/visual_utils/v2xvisualize.py' to visualize the DAIR-C dataset. The vehicle Lidar view is

.. image:: imgs/3D/vehicleview.png
  :width: 900
  :alt: colormap

The color of the points is related to the height based on the following color map

.. image:: imgs/3D/colormap.png
  :width: 400
  :alt: colormap

The top view of the Lidar from the Infrastructure is

.. image:: imgs/3D/infraview1.png
  :width: 900
  :alt: infraview1

The 3D view of the Lidar from the Infrastructure is

.. image:: imgs/3D/infraview2.png
  :width: 900
  :alt: infraview2

The fusion top view of the Lidar from the Infrastructure and Lidar from the vehicle is

.. image:: imgs/3D/fusiontop.png
  :width: 900
  :alt: fusiontop

The fusion 3D view of the Lidar from the Infrastructure and Lidar from the vehicle is

.. image:: imgs/3D/fusionview1.png
  :width: 900
  :alt: fusionview1

Convert the dataset to KITTI format 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In 'mydetector3d/datasets/dairv2x/dair2kitti.py', convert the vehicle-side data to Kitti format, set: 
 * 'source-root=/data/cmpe249-fa22/DAIR-C/cooperative-vehicle-infrastructure/vehicle-side/'
 * 'target-root=/data/cmpe249-fa22/DAIR-C/single-vehicle-side-point-cloud-kitti'
 * 'sourcelidarfolder=/data/cmpe249-fa22/DAIR-C/cooperative-vehicle-infrastructure-vehicle-side-velodyne'
 * 'split-path=/data/cmpe249-fa22/DAIR-C/split_datas/single-vehicle-split-data.json'
 * 'sensor_view=vehicle'

The conversion process involve the following major steps:
 * First create kitti folder, then call **rawdata_copy** to copy images from source to target (kitti folder).
 * 'mykitti_pcd2bin': created new folder '/data/cmpe249-fa22/DAIR-C/single-vehicle-side-point-cloud-kitti/training/velodyne', convert pcd files in 'cooperative-vehicle-infrastructure-vehicle-side-velodyne' to bin files in Kitti 'velodyne' folder. Get xyz and intensity from pcd file, divide intensity/255, save xyz and new intensity to kitti velodyne bin file.
 * 'gen_lidar2cam', data_info=read_json(source_root/data_info.json), for each data in data_info, 
    * read 'calib/lidar_to_camera/id.json' and get Tr_velo_to_cam (3,4) 
    * read labels_path 'label/lidar/id.json', for each label in labels, 
       * get 'h, w, l, x, y, z, yaw_lidar', perform 'z = z - h / 2' get bottom_center
       * convert bottom_center to camera coordinate, get 'alpha, yaw' from **get_camera_3d_8points** 
       * use **convert_point** to get 'cam_x, cam_y, cam_z', and **set_label**
    * Write labels to 'tmp_file/label/lidar/id.json', get 'path_camera_intrinsic' and 'path_lidar_to_camera' under calib folder, call **gen_calib2kitti** get kitti calibration
 * use **json2kitti** to convert json label to kitti_label_root (/data/cmpe249-fa22/DAIR-C/single-vehicle-side-point-cloud-kitti/training/label_2/000000.txt)
    * change code in write_kitti_in_txt, save txt to '/data/cmpe249-fa22/DAIR-C/single-vehicle-side-point-cloud-kitti/training/label_2'
 * Generate calibration files, 
 * The converted kitti folder is '/data/cmpe249-fa22/DAIR-C/single-vehicle-side-point-cloud-kitti'. The 'testing folder is empty', the image folder is not available in training, need to copy the images to training folder:
 
 .. code-block:: console
 
  (mycondapy39) [010796032@coe-hpc2 training]$ ls
  calib  label_2  velodyne
  (mycondapy39) [010796032@coe-hpc2 training]$ mkdir image_2
  (mycondapy39) [010796032@coe-hpc2 training]$ cd image_2/
  (mycondapy39) [010796032@coe-hpc2 image_2]$ cp /data/cmpe249-fa22/DAIR-C/cooperative-vehicle-infrastructure-vehicle-side-image/* .

Using 'mydetector3d/tools/visual_utils/v2xvisualize.py' to visualize the converted kitti-format lidar

.. image:: imgs/3D/v2xvehiclekittitop.png
  :width: 900
  :alt: v2xvehiclekittitop

Using 'VisUtils/waymokittiallvis2.py', the visualization of the vehicle-side Lidar with 3D bounding boxes is shown here

.. image:: imgs/3D/V2XConvertedtoKittiwithboxes.png
  :width: 900
  :alt: V2XConvertedtoKittiwithboxes

The camera view and the projected Lidar to camera is shown here

.. image:: imgs/3D/V2Xkittiimage.png
  :width: 900
  :alt: V2Xkitti image

In 'mydetector3d/datasets/dairv2x/dair2kitti.py', convert the infrastructure-side data to Kitti format, set: 
 * 'source-root=/data/cmpe249-fa22/DAIR-C/cooperative-vehicle-infrastructure/infrastructure-side/'
 * 'target-root=/data/cmpe249-fa22/DAIR-C/infrastructure-side-point-cloud-kitti'
 * 'sourcelidarfolder=/data/cmpe249-fa22/DAIR-C/cooperative-vehicle-infrastructure-infrastructure-side-velodyne'
 * 'split-path=/data/cmpe249-fa22/DAIR-C/split_datas/single-infrastructure-split-data.json'
 * 'sensor_view=infrastructure'

Created kitti folder "/data/cmpe249-fa22/DAIR-C/infrastructure-side-point-cloud-kitti"

.. code-block:: console

 (mycondapy39) [010796032@coe-hpc2 DAIR-C]$ cd infrastructure-side-point-cloud-kitti/
 (mycondapy39) [010796032@coe-hpc2 infrastructure-side-point-cloud-kitti]$ ls
 ImageSets  testing  training
 (mycondapy39) [010796032@coe-hpc2 infrastructure-side-point-cloud-kitti]$ cd training/
 (mycondapy39) [010796032@coe-hpc2 training]$ ls
 calib  label_2  velodyne
 (mycondapy39) [010796032@coe-hpc2 training]$ mkdir image_2 && cd image_2
 (mycondapy39) [010796032@coe-hpc2 image_2]$ cp /data/cmpe249-fa22/DAIR-C/cooperative-vehicle-infrastructure-infrastructure-side-image/* .

.. note::
    During the **dair2kitti** conversion process, classes of ["Truck","Van","Bus","Car"] has been converted to 'Car' in **rewrite_label** function. There are 7 classes left in the converted kitti data: Car, Pedestrian, Cyclist, Tricyclist, Motorcyclist, Barrowlist, TrafficCone.
    The current mydetector3d training will only pick the classes in the class_names list, i.e., other classes are ignored.

Use **checklabelfiles** function in dairkitti_dataset to see the class names in label

.. code-block:: console

  #single vehicle side total: 15285
  {'Car': 133189, 'Motorcyclist': 18738, 'Cyclist': 11113, 'Tricyclist': 4173, 'Trafficcone': 106764, 'Pedestrian': 11434}
  #infrastructure side total: 12424
  {'Car': 160048, 'Motorcyclist': 28986, 'Trafficcone': 233529, 'Cyclist': 13228, 'Pedestrian': 24789, 'Barrowlist': 108}

Run **replacelabelnames** in dairkitti_dataset, to replace some of the class names, the final output contains four classes

.. code-block:: console

  (mycondapy39) [ 3DDepth]$ python mydetector3d/datasets/kitti/dairkitti_dataset.py
  #single vihicle side
  {'Car': 133189, 'Cyclist': 34024, 'Other': 106764, 'Pedestrian': 11434}
  #infrastructure side
  {'Car': 160048, 'Cyclist': 42214, 'Other': 233637, 'Pedestrian': 24789}

Infrastructure to Vehicle Transform 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Code 'mydetector3d/datasets/dairv2x/point_cloud_i2v.py' is used to transform the Lidar data from the Infrastructure view to the vehicle view.
  * Read data_info from cooperative/data_info.json, which contains the vehicle-side image/Lidar data path (e.g., 000289) and infrastructure-side image/Lidar data path (e.g., 007489)
  * Find the matched i_data (infrastructure) and v_data (vehicle) dict
  * Get infrastructure-side virtuallidar2world path, get vehicle-side novatel2world, and lidar2novatel path; destination file name from infrastructure (007489)
  * call **trans_pcd_i2v**, read infrastructure lidar pcd, to virtuallidar to world transform, then world to novatel transform, then do novatel to lidar transform
  * save points to bin files in '/data/cmpe249-fa22/DAIR-C/'

.. image:: imgs/3D/fusionpoints1-big.png
  :width: 600
  :alt: fusion big image

We can also check the details of the fusion

.. image:: imgs/3D/fusionpoints1.png
  :width: 600
  :alt: fusion details

I2V Fusion
~~~~~~~~~~~
After the Lidar from the Infrastructure is converted to the vehicle view, we can perform raw data fusion. One example of the fusion result is shown here


Prepare the dataset 
~~~~~~~~~~~~~~~~~~~

Run dairkitti_dataset.py to generate the split files, infos, and gt_database forthe vehicle side data.
 * run **create_split** option in dairkitti_dataset.py to create the split files (trainval.txt, train.txt, and val.txt) in 'ImageSets'
 * run **create_infos** to generate 'kitti_infos_xx.pkl' and call **create_groundtruth_database** to generate the gt_database
 
.. code-block:: console
 
  $ dairkitti_dataset.py
  gt_database sample: 12228/12228
  Database Car: 106628
  Database Motorcyclist: 14916
  Database Cyclist: 8845
  Database Trafficcone: 85790
  Database Pedestrian: 9060
  Database Tricyclist: 3286
  $ dairkitti_dataset.py # after replacelabelnames
  gt_database sample: 12228/12228
  Database Car: 106628
  Database Cyclist: 27047
  Database Other: 85790
  Database Pedestrian: 9060
  ---------------Data preparation Done---------------
  $ ls /data/cmpe249-fa22/DAIR-C/single-vehicle-side-point-cloud-kitti/
  gt_database  kitti_dbinfos_train.pkl  kitti_infos_train.pkl     kitti_infos_val.pkl  training
  ImageSets    kitti_infos_test.pkl     kitti_infos_trainval.pkl  testing

Use **checkinfopklfiles** to check the pkl file

.. code-block:: console

 info['point_cloud'] = {'num_features': 4, 'lidar_idx': sample_idx}
 info['image'] = {'image_idx': sample_idx, 'image_shape': self.get_image_shape(sample_idx)}
 info['calib'] = calib_info
 info['annos'] = annotations #['name'], ['truncated'], ['occluded'], ['alpha'], ['bbox']: (N,4), ['dimensions']: lhw(camera) format (N,3), ['location']: (N,3), ['rotation_y'], ['score'], ['difficulty'], ['index'], ['gt_boxes_lidar']: (N,7), ['num_points_in_gt']

Run dairkitti_dataset.py again to generate the split file, infos, and gt_database for the infrastructure data

.. code-block:: console
  gt_database sample: 9939/9939
  Database Car: 127726
  Database Motorcyclist: 23287
  Database Cyclist: 10555
  Database Trafficcone: 187382
  Database Pedestrian: 19794
  Database Barrowlist: 81
  ---------------Data preparation Done---------------
  $ dairkitti_dataset.py # after replacelabelnames
  gt_database sample: 9939/9939
  Database Car: 127726
  Database Cyclist: 33842
  Database Other: 187463
  Database Pedestrian: 19794
  ---------------Data preparation Done---------------
  $ ls /data/cmpe249-fa22/DAIR-C/infrastructure-side-point-cloud-kitti/
  gt_database  kitti_dbinfos_train.pkl  kitti_infos_train.pkl     kitti_infos_val.pkl  training
  ImageSets    kitti_infos_test.pkl     kitti_infos_trainval.pkl  testing

In the **__getitem__** of dairkitti_dataset.py, gt_boxes_lidar is from 'location', 'dimensions', and 'rotation_y'

.. code-block:: console

  loc, dims, rots = annos['location'], annos['dimensions'], annos['rotation_y']
  gt_names = annos['name']
  #create label [n,7] in camera coordinate boxes3d_camera: (N, 7) [x, y, z, l, h, w, r] in rect camera coords
  gt_boxes_camera = np.concatenate([loc, dims, rots[..., np.newaxis]], axis=1).astype(np.float32)
  gt_boxes_lidar = box_utils.boxes3d_kitti_camera_to_lidar(gt_boxes_camera, calib)

If this frame has no object, set gt_boxes_lidar empty:

.. code-block:: console

  if len(gt_names)==0:
       gt_boxes_lidar = np.zeros((0, 7))

Training and Evaluation 
~~~~~~~~~~~~~~~~~~~~~~~
Train the vehicle side data in mydetector3d
  * cfg_dataset='mydetector3d/tools/cfgs/dairkitti_models/my3dmodel.yaml', model is saved in '/data/cmpe249-fa22/Mymodels/dairkitti_models/my3dmodel/0511/ckpt/checkpoint_epoch_120.pth'/latest_model.pth
  * Evaluation results (filter out empty frame and classes not in the kittclasses) saved in /data/cmpe249-fa22/Mymodels/eval/dairkitti_models_my3dmodel_epochmodel/txtresults

.. code-block:: console

  Car AP@0.70, 0.70, 0.70:
  bbox AP:22.9647, 20.1308, 19.5203
  bev  AP:64.3469, 65.0784, 65.2450
  3d   AP:56.6919, 52.6843, 51.5003
  aos  AP:11.50, 10.21, 9.93
  Pedestrian AP@0.50, 0.50, 0.50:
  bbox AP:13.2223, 11.7845, 11.7958
  bev  AP:53.5280, 48.6861, 47.9500
  3d   AP:50.1386, 43.0288, 42.3967
  aos  AP:11.34, 10.48, 10.48
  Cyclist AP@0.50, 0.50, 0.50:
  bbox AP:11.4549, 13.7494, 13.9884
  bev  AP:22.5282, 30.7371, 30.5679
  3d   AP:20.9868, 26.8777, 26.7182
  aos  AP:5.08, 6.16, 6.28

Run the evaluation and Lidar detection result is

.. image:: imgs/3D/dairvehiclesidepred.png
  :width: 900
  :alt: detection results

Train the infrastructure side data in mydetector3d
  * cfg_dataset='mydetector3d/tools/cfgs/dairkitti_models/my3dmodel_infra.yaml', model is saved in '/data/cmpe249-fa22/Mymodels/dairkitti_models/my3dmodel_infra/0512infra/ckpt/checkpoint_epoch_120.pth'/latest_model.pth
  * Evaluation results (filter out empty frame and classes not in the kittclasses) is 0


Train the vehicle side data in mydetector3d after **replacelabelnames**, data_tag='0513' in GPU3
  * cfg_dataset='mydetector3d/tools/cfgs/dairkitti_models/my3dmodel.yaml', model is saved in '/data/cmpe249-fa22/Mymodels/dairkitti_models/my3dmodel/0513/ckpt/checkpoint_epoch_128.pth'
  * Evaluation results (filter out empty frame and classes not in the kittclasses) result is saved to /data/cmpe249-fa22/Mymodels/eval/dairkitti_models_my3dmodel_epochmodel/txtresults

.. code-block:: console

  Average predicted number of objects(3057 samples): 140.240
  Finished detection: {'recall/roi_0.3': 0.0, 'recall/rcnn_0.3': 0.8291671061421088, 'recall/roi_0.5': 0.0, 'recall/rcnn_0.5': 0.671465738494533, 'recall/roi_0.7': 0.0, 'recall/rcnn_0.7': 0.31039271525507156, 'infer_time': 64.6671114404217, 'total_pred_objects': 428715, 'total_annos': 3057}
  Car AP@0.70, 0.70, 0.70:
  bbox AP:22.1671, 20.0946, 19.4177
  bev  AP:67.3517, 68.4604, 68.3072
  3d   AP:59.0924, 55.3433, 54.4236
  aos  AP:10.59, 9.66, 9.35
  Pedestrian AP@0.50, 0.50, 0.50:
  bbox AP:12.6278, 12.0752, 12.0567
  bev  AP:54.4139, 48.7479, 48.4298
  3d   AP:51.6765, 43.4523, 43.0454
  aos  AP:11.05, 10.60, 10.59
  Cyclist AP@0.50, 0.50, 0.50:
  bbox AP:22.8686, 22.5770, 22.6723
  bev  AP:57.5935, 58.9456, 58.0578
  3d   AP:54.5871, 53.7105, 52.8249
  aos  AP:10.90, 10.70, 10.76

Train the infrastructure side data in mydetector3d after **replacelabelnames**, data_tag='0513infra' in GPU2
  * cfg_dataset='mydetector3d/tools/cfgs/dairkitti_models/my3dmodel_infra.yaml', model is saved in '/data/cmpe249-fa22/Mymodels/dairkitti_models/my3dmodel_infra/0513infra/ckpt/checkpoint_epoch_128.pth'
  * Evaluation results (filter out empty frame and classes not in the kittclasses)

.. code-block:: console

  Average predicted number of objects(2485 samples): 85.658
  Finished detection: {'recall/roi_0.3': 0.0, 'recall/rcnn_0.3': 0.626487269085486, 'recall/roi_0.5': 0.0, 'recall/rcnn_0.5': 0.5321511381078345, 'recall/roi_0.7': 0.0, 'recall/rcnn_0.7': 0.30276607556905394, 'infer_time': 68.14103801150797, 'total_pred_objects': 212861, 'total_annos': 2485}
  Car AP@0.70, 0.70, 0.70:
  bbox AP:23.7721, 18.4526, 18.3909
  bev  AP:72.1776, 54.1334, 54.0990
  3d   AP:70.9812, 53.2164, 53.0006
  aos  AP:12.27, 9.49, 9.46
  Pedestrian AP@0.50, 0.50, 0.50:
  bbox AP:34.0897, 33.7425, 33.8436
  bev  AP:36.2813, 34.1492, 34.2634
  3d   AP:33.5470, 31.4709, 31.5814
  aos  AP:17.07, 17.10, 17.16
  Cyclist AP@0.50, 0.50, 0.50:
  bbox AP:45.7644, 40.9651, 41.1427
  bev  AP:63.7247, 52.2808, 52.0245
  3d   AP:61.5907, 51.3137, 50.9824
  aos  AP:23.37, 21.38, 21.48

Train 'mydetector3d/tools/cfgs/dairkitti_models/myvoxelnext.yaml' in GPU2

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

opv2v dataset is downloaded in '/data/cmpe249-fa22/OpenCOOD/opv2v_data_dumping', but there are errors in the dataset: "unzip:  cannot find zipfile directory in one of train.zip"
  
