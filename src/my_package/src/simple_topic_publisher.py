#! /usr/bin/env python

import rospy     
from geometry_msgs.msg import Twist

rospy.init_node('MoveRobot')         # Initiate a Node named 'topic_publisher'
pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)    # Create a Publisher object, that will publish on the /counter topic
                                           #  messages of type Int32

rate = rospy.Rate(2)                       # Set a publish rate of 2 Hz
var = Twist()                            # Create a var of type Int32
var.linear.x = 0.5                             # Initialize 'count' variable
var.angular.z = 0.5 

while not rospy.is_shutdown():             # Create a loop that will go until someone stops the program execution
  pub.publish(var)                        # Increment 'count' variable
  rate.sleep()  