#! /usr/bin/env python

import rospy
from unit_3_services.srv import BB8OdomServiceMessage, BB8OdomServiceMessageResponse # you import the service message pythin classes genearted from Empty.srv.
from move_bb8_odometer import MoveBB8Odom

def my_callback(request):
    rospy.loginfo("The Service move_bb8_odom has been called")
    movebb8_object = MoveBB8Odom()
    
    rospy.loginfo("Start Movement with odometer")
    movebb8_object.move_distance(distance_to_move = 1.0, linear_speed = 0.2)
        
    rospy.loginfo("Finished service move_bb8_odom that was called")
    response = BB8OdomServiceMessageResponse()
    response.success = True
    return response
    
rospy.init_node('service_move_bb8_odom_server')
my_service = rospy.Service('/move_bb8_odom', BB8OdomServiceMessage, my_callback) # create the Service called move_bb8_in_square with the defined callback
rospy.loginfo("Service /move_bb8_odom Ready")
rospy.spin() # maintain the service open