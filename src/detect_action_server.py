#!/home/prathamesh/myvenv/py2-cpu/bin/python

import rospy
import actionlib
from forCv.msg import face_detect_actionAction, face_detect_actionGoal, face_detect_actionResult

import numpy as np
import sys
sys.path.append('~/ws/temp_ws/src/forCv/')
from scripts.helpers import FaceDetector


class FaceDetectActionServer:

    def __init__(self):
        rospy.init_node('detect_action_node')
        self.server = actionlib.SimpleActionServer('face_detect_server', face_detect_actionAction, self.face_detect_cb, False)
        self.fd_obj = FaceDetector()

    def face_detect_cb(self, goal):
        #print(np.asarray(list(goal.image)).shape)

        img = np.asarray(list(goal.image)).reshape((480, 640, 3), order="C").astype(np.uint8)
        (x, y, w, h) = self.fd_obj.getLargestCropCoords(img)
        result = face_detect_actionResult()
        result.x, result.y, result.w, result.h = x, y, w, h
        if x == -1 and y == -1 and w == -1 and h == -1:
            print("No face")
            self.server.set_aborted(result, "No Face Found")
            return
        print("Found Face")
        self.server.set_succeeded(result)

    def start_server(self, spin=False):
        self.server.start()
        if spin:
            rospy.spin()

def main():
    rospy.init_node('detect_action_node')
    fd_server = FaceDetectActionServer()
    fd_server.start_server(spin=True)

if __name__ == '__main__':
    main()
