#! /usr/bin/env python

import rospy
from move_robot.srv import MoveRobotCircleServiceMessage, MoveRobotCircleServiceMessageResponse # you import the service message pythin classes genearted from MoveRobotCircleServiceMessage.srv.
from move_robot_circle import MoveRobotCircle

def my_callback(request):
    rospy.loginfo("The Service move_robot_circle has been called")
    moveRobotCircle_object = MoveRobotCircle()
    
    # We need to add because if we ask 0 repetitions means to execute once, not zero times.
    repetitions_of_circle = request.repetitions + 1
    new_radius = request.radius
    for i in range(repetitions_of_circle):
        rospy.loginfo("Start Movement with radius = "+str(new_radius)+"Repetition = "+str(i))
        moveRobotCircle_object.move_circle(radius=new_radius)
        
    rospy.loginfo("Finished service move_robot_circle that was called")
    response = MoveRobotCircleServiceMessageResponse()
    response.success = True
    return response
    
rospy.init_node('service_move_robot_circle_server')
my_service = rospy.Service('/move_robot_circle', MoveRobotCircleServiceMessage, my_callback) # create the service called move_robot_circle   with the defined callback
rospy.loginfo("Service /move_robot_circle Ready")
rospy.spin() # maintain the service open