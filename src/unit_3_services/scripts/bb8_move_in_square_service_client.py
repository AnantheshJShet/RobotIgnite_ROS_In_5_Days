#! /usr/bin/env python

import rospkg
import rospy
from std_srvs.srv import Empty, EmptyRequest # you import the service message pythin classes genearted from Empty.srv.

rospy.init_node('service_move_bb8_in_square_client') # initialise a ROS node with the name service_client
rospy.wait_for_service('/move_bb8_in_square') # Wait for the service move_bb8_in_square to be running
move_bb8_in_square_service_client = rospy.ServiceProxy('/move_bb8_in_square', Empty) # Create the connection to the service
move_bb8_in_square_request_object = EmptyRequest() # Create an object of type EmptyRequest

result = move_bb8_in_square_service_client(move_bb8_in_square_request_object)
print result