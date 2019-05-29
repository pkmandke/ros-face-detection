#!/home/prathamesh/myvenv/py2-cpu/bin/python

### This is a server that crops the image and sends the co-ordinates of the face ###

import cv2
import rospy
import numpy as np
import aligndlib as adl
from forCv.srv import *

PRED_PATH = '/home/prathamesh/undergrad/btech_proj/misc/openface/testing/shape_predictor_68_face_landmarks.dat'
al = adl.AlignDlib(PRED_PATH)

def rect_to_bb(rect):
    # take a bounding predicted by dlib and convert it
    # to (x, y, w, h)
    x = rect.left()
    y = rect.top()
    w = rect.right() - x
    h = rect.bottom() - y

    return (x, y, w, h)


def crop_handler(req):
    #print(type(req.img))
    bbx = al.getLargestFaceBoundingBox(np.asarray(req.img).reshape((480, 640, 3), order='C').astype(np.uint8))

    if bbx == None:
        return getCropResponse(-1, -1, -1, -1)
    else:
        (x, y, w, h) = rect_to_bb(bbx)
        if x <= 0 or y <= 0 or w <= 0 or h <= 0:
            return getCropResponse(0, 0, 0, 0)
        print('Found Face!')
        return getCropResponse(x, y, w, h)

def main():
    rospy.init_node('crop_server_node')
    serv = rospy.Service('crop_service', getCrop, crop_handler)
    rospy.spin()

if __name__ == '__main__':
    main()
