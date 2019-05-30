#!/home/prathamesh/myvenv/py2-cpu/bin/python

import numpy as np
import aligndlib as adl
import cv2

PRED_PATH = '/home/prathamesh/undergrad/btech_proj/misc/openface/testing/shape_predictor_68_face_landmarks.dat'
SHAPE = (480, 640, 3)

def getFrame(cam):

    bl, _ = cam.read()
    if bl:
        return True, _
    else:
        return False, _

def show_img(img, msg, reshape=False):
    if reshape:
        cv2.imshow(msg, img.reshape(SHAPE, order='C').astype(np.uint8))
        if cv2.waitKey(1) == 27:
            print("Esc")
    else:
        cv2.imshow(msg, img)
        if cv2.waitKey(1) == 27:
            print("Esc")

def rect_to_bb(rect):
    # take a bounding predicted by dlib and convert it
    # to (x, y, w, h)
    x = rect.left()
    y = rect.top()
    w = rect.right() - x
    h = rect.bottom() - y

    return (x, y, w, h)

class FaceDetector:
    """Class to initiate face detection object"""
    def __init__(self, pred_path=PRED_PATH):
        self.al = adl.AlignDlib(PRED_PATH)

    def getLargestCropCoords(self, img):
        bbx = self.al.getLargestFaceBoundingBox(img)

        if bbx == None:
            return (-1, -1, -1, -1)
        else:
            (x, y, w, h) = rect_to_bb(bbx)
            if x <= 0 or y <= 0 or w <= 0 or h <= 0:
                return (0, 0, 0, 0)
            return (x, y, w, h)
