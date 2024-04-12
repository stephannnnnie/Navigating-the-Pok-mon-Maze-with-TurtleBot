#!/usr/bin/env python

'''
This script makes Gazebo less fail by translating gazebo status messages to odometry data.
Since Gazebo also publishes data faster than normal odom data, this script caps the update to 20hz.
Winter Guerra
'''

import rospy
import cv2 as cv
from cv_bridge.core import CvBridge
from sensor_msgs.msg import Image
import os


def callback(data):
    print(data)

def SubscribeAndPublish():
    print("start")
    rospy.init_node('get_depth', anonymous=True)
    rospy.Subscriber('/real_sense/depth/image_raw', Image, callback,queue_size=1)
    #rospy.Subscriber('cmd_vel', Twist, callback,queue_size=1,buff_size=52428800)
    rospy.spin()


if __name__ == '__main__':
    try:
        SubscribeAndPublish()
    except rospy.ROSInterruptException:
        pass
