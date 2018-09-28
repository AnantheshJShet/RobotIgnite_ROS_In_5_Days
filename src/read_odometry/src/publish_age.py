#! /usr/bin/env python

import rospy     
from read_odometry.msg import Age

rospy.init_node('publish_age_node')
pub =  rospy.Publisher('/age_info', Age, queue_size=1)
rate = rospy.Rate(2)
age = Age()
age.years = 5
age.months = 10
age.days = 21

while not rospy.is_shutdown():
    pub.publish(age)
    rate.sleep()