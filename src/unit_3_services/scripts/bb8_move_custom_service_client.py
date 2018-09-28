#! /usr/bin/env python

import rospkg
import rospy
from unit_3_services.srv import BB8CustomServiceMessage, BB8CustomServiceMessageRequest # you import the service message pythin classes genearted from Empty.srv.

rospy.init_node('service_move_bb8_in_square_custom_client') # initialise a ROS node with the name service_client
rospy.wait_for_service('/move_bb8_in_square_custom') # Wait for the service move_bb8_in_square to be running
move_bb8_in_square_service_client = rospy.ServiceProxy('/move_bb8_in_square_custom', BB8CustomServiceMessage) # Create the connection to the service
move_bb8_in_square_request_object = BB8CustomServiceMessageRequest() # Create an object of type EmptyRequest


"""
# BB8CustomServiceMessage
float64 side       # The distance of each side of the square
int32 repetitions    # The number of times BB-8 has to execute the square movement when the service is called
---
bool success         # Did it achieve it?
"""

move_bb8_in_square_request_object.side = 0.1
move_bb8_in_square_request_object.repetitions = 1
rospy.loginfo("Start Two Small Squares...")
result = move_bb8_in_square_service_client(move_bb8_in_square_request_object)
rospy.loginfo(str(result))

move_bb8_in_square_request_object.side = 0.6
move_bb8_in_square_request_object.repetitions = 0
rospy.loginfo("Start One Big Square...")
result = move_bb8_in_square_service_client(move_bb8_in_square_request_object)
rospy.loginfo(str(result))

rospy.loginfo("End of Service call...")