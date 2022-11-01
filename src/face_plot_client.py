#!/home/prathamesh/myvenv/py2-cpu/bin/python

import rospy
import actionlib
from forCv.msg import face_detect_actionAction, face_detect_actionGoal, face_detect_actionResult
from rospy.numpy_msg import numpy_msg
from rospy_tutorials.msg import Floats

import numpy as np
import cv2
import sys
sys.path.append('~/ws/temp_ws/src/forCv/')
import scripts.helpers as sh

class FacePlotActionClient:

    def __init__(self):
        rospy.init_node('face_plot_client_node')
        self.sub = rospy.Subscriber('full_img', numpy_msg(Floats), self.face_plot_cb)
        self.client = actionlib.SimpleActionClient('face_detect_server',face_detect_actionAction)
        self.in_cb = False
        self.goal_image = None
        self.x, self.y, self.h, self.w = 0, 0, 0, 0

    def send_goal(self):
        #self.client = actionlib.SimpleActionClient('face_detect_server', face_detect_actionAction)
        self.client.wait_for_server()
        goal = face_detect_actionGoal()
        goal.image = self.goal_image
        self.client.send_goal(goal)

    def plot_cropped(self):

        if self.client.get_state() == 3:
            print("Face Co-ordinates received")
            res = self.client.get_result()
            self.x, self.y, self.w, self.h = res.x, res.y, res.w, res.h
            self.send_goal()
        elif self.client.get_state() == 4:
            print("No face Found")
            self.x, self.y, self.w, self.h = 0, 0, 0, 0
            self.send_goal()

        plt_img = self.goal_image.reshape(sh.SHAPE, order='C').astype(np.uint8)
        #print(self.x, self.y, self.h, self.w)
        cv2.rectangle(plt_img, (self.x, self.y), (self.x+self.w, self.y+self.h), (255, 0, 0), 2)
        cv2.imshow("Face Crop", plt_img)
        cv2.waitKey(1)


    def face_plot_cb(self, data):
        #sh.show_img(data.data, 'Cam Feed', reshape=True)
        self.goal_image = data.data
        if not self.in_cb:
            self.send_goal()
            self.in_cb = True;

        self.plot_cropped()


def main():
    fplotobj = FacePlotActionClient()
    while not rospy.is_shutdown():
        rospy.sleep(1)

if __name__ == '__main__':
    main()
