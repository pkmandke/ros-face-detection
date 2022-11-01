# Face detection in ROS

Face Detection using ROS pub/sub.

## ROS Face detector

The package samples images from the webcam and displays a bounding box after detecting the largest face in the frame using [dlib](https://pypi.org/project/dlib/). The code for face detection is inspired by [OpenFace](https://github.com/cmusatyalab/openface).

## TODO

* [x] Add actionlib
* [x] Add launch file (with if syntax)
* [x] Reduce effect of face detect delay

### Details

**Update: 30/05/2019**

Three nodes:

1. Image capture and publish. [Source](https://github.com/pkmandke/ros-face-detection/blob/master/src/img_pub_node.py)
2. Subscribe and plot image. Also, send the image as a (action) goal for face detection. The lag problem is solved by plotting irrespective of whether face co-ordinates are received so that only the face rectangle faces a lag. [Source](https://github.com/pkmandke/ros-face-detection/blob/master/src/face_plot_client.py)
3. The Face detection server. Processes requests and sends back face co-ordinates as results.[Source](https://github.com/pkmandke/ros-face-detection/blob/master/src/detect_action_server.py)

Other updates:

* [x] Object oriented API for actionlib and pub/sub.
* [x] Helper [scripts](https://github.com/pkmandke/ros-face-detection/tree/master/scripts).

## Snapshots

Using actionlib

![Face Detect](https://github.com/pkmandke/ros-face-detection/blob/master/snaps/launch_file_output.png)

* Old Service based

There are 3 nodes. 2 of them are a publish-subscribe pair that transfer np.array images using floats. The subscriber node then calls a service(server) node which returns the face co-ordinates if found. These co-ordinates are used by the subscriber node to draw the bounding box.

Snapshot are in the snaps folder.
