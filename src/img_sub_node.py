#!/home/prathamesh/myvenv/py2-cpu/bin/python

### This node plots the given image by subscribing to a topic ###
## When an image is posted to a topic, this node displays the image as a continous feed
from cv_bridge import CvBridge, CvBridgeError
import cv2
import rospy
from rospy_tutorials.msg import Floats
from rospy.numpy_msg import numpy_msg
import numpy as np
import pre_proc as pp
import aligndlib as adl

PRED_PATH = '/home/prathamesh/undergrad/btech_proj/misc/openface/testing/shape_predictor_68_face_landmarks.dat'
al = adl.AlignDlib(PRED_PATH)


def handle_img(data):
    #print(data.data.dtype)
    #print(data.data.reshape((480, 640, 3), order='C').astype(np.uint8)[:10, 0, 0])
    myimg = data.data.reshape((480, 640, 3), order='C').astype(np.uint8)
    _, fcrop = pp.face_crop(myimg, pred_path=al)
    if _:
        cv2.imshow('full_image', fcrop)
        if cv2.waitKey(1) == 27:
            rospy.signal_shutdown('Exited')
    else:
        print('No face')

def main():
    rospy.init_node('img_sub_node', anonymous=True)
    sub1 = rospy.Subscriber('full_img', numpy_msg(Floats), handle_img)
    #rospy.spin()
    while not rospy.is_shutdown():
        rospy.sleep(1)

if __name__ == '__main__':
    main()
    cv2.destroyAllWindows()
