#! /usr/bin/env python

import rospkg
import rospy
from move_robot.srv import MoveRobotCircleServiceMessage, MoveRobotCircleServiceMessageRequest # you import the service message python classes genearted from MoveRobotCircleServiceMessage.srv.

rospy.init_node('service_move_robot_circle_client') # initialise a ROS node with the name service_move_robot_circle_client
rospy.wait_for_service('/move_robot_circle') # Wait for the service move_robot_circle to be running
move_robot_circle_service_client = rospy.ServiceProxy('/move_robot_circle', MoveRobotCircleServiceMessage) # Create the connection to the service
move_robot_circle_request_object = MoveRobotCircleServiceMessageRequest() # Create an object of type MoveRobotCircleServiceMessageRequest


"""
# MoveRobotCircleServiceMessage
float64 radius       # The radius of the circle whose circumference the robot has to trace
int32 repetitions    # The number of times BB-8 has to execute the square movement when the service is called
---
bool success         # Did it achieve it?
"""

move_robot_circle_request_object.radius = 1
move_robot_circle_request_object.repetitions = 0
rospy.loginfo("Start A Circle...")
result = move_robot_circle_service_client(move_robot_circle_request_object)
rospy.loginfo(str(result))
rospy.loginfo("End of Service call...")