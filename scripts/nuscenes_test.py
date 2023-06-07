
from nuscenes.nuscenes import NuScenes

if __name__ == '__main__':
    import yaml
    import argparse
    from pathlib import Path

    parser = argparse.ArgumentParser(description='arg parser')
    parser.add_argument('--datapath', type=str, default='/Volumes/Samsung_T5/Datasets/Nuscenes/nuScenesv1.0-mini', help='specify the path of dataset')
    #parser.add_argument('--func', type=str, default='create_groundtruth', help='')
    parser.add_argument('--version', type=str, default='v1.0-trainval', help='')
    parser.add_argument('--with_cam', default=True, help='use camera or not')
    args = parser.parse_args()
    
    nusc = NuScenes(version='v1.0-mini', dataroot=args.datapath, verbose=True)
    nusc.list_scenes() #1000 scenes, 20s each; 10 scenes in mini

    #get one scene
    my_scene = nusc.scene[0]
    #sample (annotated keyframe) is annotated 2Hz
    first_sample_token = my_scene['first_sample_token'] #'ca9a282c9e77460f8360f564131a8af5'
    #rendering
    nusc.render_sample(first_sample_token, out_path='./firstsample.png')

    #get sample's metadata
    my_sample = nusc.get('sample', first_sample_token) #dict

    #list all related sample_data keyframes and sample_annotation associated with a sample
    nusc.list_sample(my_sample['token'])
    #sample_annotation_token: 49f76277d07541c5a584aa14c9d28754, category: vehicle.car
    #sample_annotation_token: 15a3b4d60b514db5a3468e2aef72a90c, category: movable_object.barrier

    #use data key to access full sensor data
    print(my_sample['data'])
    #{'RADAR_FRONT': '37091c75b9704e0daa829ba56dfa0906', 'RADAR_FRONT_LEFT': '11946c1461d14016a322916157da3c7d', 'RADAR_FRONT_RIGHT': '491209956ee3435a9ec173dad3aaf58b', 'RADAR_BACK_LEFT': '312aa38d0e3e4f01b3124c523e6f9776', 'RADAR_BACK_RIGHT': '07b30d5eb6104e79be58eadf94382bc1', 'LIDAR_TOP': '9d9bf11fb0e144c8b446d54a8a00184f', 'CAM_FRONT': 'e3d495d4ac534d54b321f50006683844', 'CAM_FRONT_RIGHT': 'aac7867ebf4f446395d29fbd60b63b3b', 'CAM_BACK_RIGHT': '79dbb4460a6b40f49f9c150cb118247e', 'CAM_BACK': '03bea5763f0f4722933508d5999c5fd8', 'CAM_BACK_LEFT': '43893a033f9c46d4a51b5e08a67a1eb7', 'CAM_FRONT_LEFT': 'fe5422747a7d4268a4b07fc396707b23'}
    
    #check the metadata of a sample_data from CAM_FRONT
    sensor = 'CAM_FRONT'
    cam_front_data = nusc.get('sample_data', my_sample['data'][sensor])
    print(cam_front_data)
    #{'token': 'e3d495d4ac534d54b321f50006683844', 'sample_token': 'ca9a282c9e77460f8360f564131a8af5', 'ego_pose_token': 'e3d495d4ac534d54b321f50006683844', 'calibrated_sensor_token': '1d31c729b073425e8e0202c5c6e66ee1', 'timestamp': 1532402927612460, 'fileformat': 'jpg', 'is_key_frame': True, 'height': 900, 'width': 1600, 'filename': 'samples/CAM_FRONT/n015-2018-07-24-11-22-45+0800__CAM_FRONT__1532402927612460.jpg', 'prev': '', 'next': '68e8e98cf7b0487baa139df808641db7', 'sensor_modality': 'camera', 'channel': 'CAM_FRONT'}

    nusc.render_sample_data(cam_front_data['token'])#get 3D box on front image

    #sample_annotation is the boundin gbox defining the object position in global coordinate system
    my_annotation_token = my_sample['anns'][18]
    my_annotation_metadata =  nusc.get('sample_annotation', my_annotation_token)
    print(my_annotation_metadata)
    
    nusc.render_annotation(my_annotation_token) #camera and lidar bbox annotation

    #check instance (i.e., the object)
    my_instance = nusc.instance[599]
    print(my_instance)
    instance_token = my_instance['token']
    nusc.render_instance(instance_token)
    print("First annotated sample of this instance:")
    nusc.render_annotation(my_instance['first_annotation_token'])
    print("Last annotated sample of this instance")
    nusc.render_annotation(my_instance['last_annotation_token'])

    #category
    nusc.list_categories()
    print(nusc.category[9])

    #sensors: 1 Lidar, 5 Radar, 6 camera
    print(nusc.sensor)
    print(nusc.sample_data[10]) #'channel' shows the sensor
    #`calibrated_sensor` consists of the definition of a particular sensor (lidar/radar/camera) as calibrated on a particular vehicle
    print(nusc.calibrated_sensor[0]) #get translation and the rotation with respect to the ego vehicle body frame
    #ego_pose` contains information about the location (encoded in `translation`) and the orientation (encoded in `rotation`) of the ego vehicle, with respect to the global coordinate system.
    print(nusc.ego_pose[0]) #ego_pose to sample_data record are one-to-one 

    #map is binary semantic masks
    print("There are {} maps masks in the loaded dataset".format(len(nusc.map)))
    nusc.map[0]

    my_sample = nusc.sample[10]
    nusc.render_pointcloud_in_image(my_sample['token'], pointsensor_channel='LIDAR_TOP')
    nusc.render_pointcloud_in_image(my_sample['token'], pointsensor_channel='LIDAR_TOP', render_intensity=True)
    #Radar data
    nusc.render_pointcloud_in_image(my_sample['token'], pointsensor_channel='RADAR_FRONT')

    my_sample = nusc.sample[20]
    nusc.render_sample(my_sample['token'], out_path='./anothersample.png') #another complete visualization example

    for i in range(len(nusc.sample)):
        my_sample = nusc.sample[i]
        filename='./complete_'+str(i)+'.png'
        nusc.render_sample(my_sample['token'], out_path=filename)
        filename='./radarfront_'+str(i)+'.png'
        nusc.render_pointcloud_in_image(my_sample['token'], pointsensor_channel='RADAR_FRONT',out_path=filename)


    #get a particular sensor
    nusc.render_sample_data(my_sample['data']['CAM_FRONT'])

    #aggregate multiple sweeps of point cloud
    nusc.render_sample_data(my_sample['data']['LIDAR_TOP'], nsweeps=5, underlay_map=True)
    nusc.render_sample_data(my_sample['data']['RADAR_FRONT'], nsweeps=5, underlay_map=True)

    from nuscenes.utils.data_classes import RadarPointCloud
    RadarPointCloud.disable_filters()
    nusc.render_sample_data(my_sample['data']['RADAR_FRONT'], nsweeps=5, underlay_map=True)
    RadarPointCloud.default_filters()

    nusc.render_annotation(my_sample['anns'][22])

    my_scene_token = nusc.field2token('scene', 'name', 'scene-0061')[0]
    #render video for front camera
    nusc.render_scene_channel(my_scene_token, 'CAM_FRONT')
    #render video for all camera
    nusc.render_scene(my_scene_token)

    #my added: error: Error: nuScenes-lidarseg not installed
    #nusc.render_scene_channel_lidarseg(my_scene_token, channel='CAM_FRONT', out_folder='./', render_mode='video', with_anns=True)

    #visualize all scenes on the map for a particular location
    nusc.render_egoposes_on_map(log_location='singapore-onenorth')

    print('Done')