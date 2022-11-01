#!/home/prathamesh/myvenv/py2-cpu/bin/python

#from cv_bridge import CvBridge, CvBridgeError
import cv2
import rospy
from rospy_tutorials.msg import Floats
from rospy.numpy_msg import numpy_msg
import numpy as np
import sys
sys.path.append('~/ws/temp_ws/src/forCv/')
import scripts.helpers as sh

def getFrame(cam):

    bl, _ = cam.read()
    if bl:
        cv2.imshow('full_image', _)
        if cv2.waitKey(1) == 0:
            print('esc')
        return True, _
    else:
        return False, _

def main(camType=0):
    cam = cv2.VideoCapture(camType);
    rospy.init_node('img_pub_node', anonymous=True)
    pub1 = rospy.Publisher('full_img', numpy_msg(Floats), queue_size=1)
    r = rospy.Rate(5)
    while not rospy.is_shutdown():
        _, img = sh.getFrame(cam)
        '''cv2.imshow('full_image', img)
        if cv2.waitKey(1) == 0:
            print('esc')'''

        if _:
            pub1.publish(img.flatten(order='C').astype(np.float32))
        else:
            continue
        r.sleep()
    cam.release()

if __name__ == '__main__':
    main()
