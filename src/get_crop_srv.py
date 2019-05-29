#!/home/prathamesh/myvenv/py2-cpu/bin/python

### This is a server that crops the image and sends the co-ordinates of the face ###

import cv2
import rospy
from rospy_tutorials.msg import Floats
from rospy.numpy_msg import numpy_msg
import numpy as np
import pre_proc as pp
import aligndlib as adl

PRED_PATH = '/home/prathamesh/undergrad/btech_proj/misc/openface/testing/shape_predictor_68_face_landmarks.dat'
al = adl.AlignDlib(PRED_PATH)
