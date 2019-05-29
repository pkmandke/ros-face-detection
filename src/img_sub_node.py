#!/home/prathamesh/myvenv/py2-cpu/bin/python

### This node plots the given image by subscribing to a topic ###
## When an image is posted to a topic, this node displays the image as a continous feed
from cv_bridge import CvBridge, CvBridgeError
import cv2
import rospy
from rospy_tutorials.msg import Floats
from rospy.numpy_msg import numpy_msg
from forCv.srv import *
import numpy as np

def getCropCoords(myimg):
    try:
        rospy.wait_for_service('crop_service')
        getCropFunc = rospy.ServiceProxy('crop_service', getCrop)
        resp1 = getCropFunc(myimg.flatten(order='C').astype(np.float32))
        return resp1.x, resp1.y, resp1.w, resp1.h
    except rospy.ServiceException, e:
        print("Service call failed")


def handle_img(data):
    #print(data.data.dtype)
    #print(data.data.reshape((480, 640, 3), order='C').astype(np.uint8)[:10, 0, 0])
    myimg = data.data.reshape((480, 640, 3), order='C').astype(np.uint8)
    (x, y, w, h) = getCropCoords(myimg)
    print(x, y, w, h)
    if x == -1 and y == -1 and w == -1 and h == -1:
        print('No face')
    else:
        cv2.rectangle(myimg, (x, y), (x+w, y+h), (255, 0, 0), 2)
    cv2.imshow('full_image', myimg)
    if cv2.waitKey(1) == 27:
        rospy.signal_shutdown('Exited')


def main():
    rospy.init_node('img_sub_node', anonymous=True)
    sub1 = rospy.Subscriber('full_img', numpy_msg(Floats), handle_img)
    #rospy.spin()
    while not rospy.is_shutdown():
        rospy.sleep(1)

if __name__ == '__main__':
    main()
    cv2.destroyAllWindows()
