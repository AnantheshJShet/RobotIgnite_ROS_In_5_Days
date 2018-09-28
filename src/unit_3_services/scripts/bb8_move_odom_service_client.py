#! /usr/bin/env python

import rospkg
import rospy
from unit_3_services.srv import BB8OdomServiceMessage, BB8OdomServiceMessageRequest # you import the service message pythin classes genearted from Empty.srv.

rospy.init_node('service_move_bb8_odom_client') # initialise a ROS node with the name service_client
rospy.wait_for_service('/move_bb8_odom') # Wait for the service move_bb8_in_square to be running
move_bb8_odom_service_client = rospy.ServiceProxy('/move_bb8_odom', BB8OdomServiceMessage) # Create the connection to the service
move_bb8_odom_request_object = BB8OdomServiceMessageRequest() # Create an object of type EmptyRequest


"""
# BB8OdomServiceMessage
float64 distance       # The distance to move
---
bool success         # Did it achieve it?
"""

move_bb8_odom_request_object.distance = 1
rospy.loginfo("Start Moving...")
result = move_bb8_odom_service_client(move_bb8_odom_request_object)
rospy.loginfo(str(result))

rospy.loginfo("End of Service call...")