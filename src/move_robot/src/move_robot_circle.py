#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
import time

class MoveRobotCircle():
    
    def __init__(self):
        self.robot_vel_publisher = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
        self.ctrl_c = False
        rospy.on_shutdown(self.shutdownhook)
        self.rate = rospy.Rate(10) # 10 Hz
        
    def publish_once_in_cmd_vel(self, cmd):
        """
        This is because publishing in topics sometimes fails the first time you publish.
        In continuous publishing systems there is no big deal but in systems that publish only
        once it is very important.
        """
        while not self.ctrl_c:
            connections = self.robot_vel_publisher.get_num_connections()
            if connections > 0:
                self.robot_vel_publisher.publish(cmd)
                rospy.loginfo("Cmd Published")
                break
            else:
                self.rate.sleep()
                
    def shutdownhook(self):
        # works better than rospy.is_shut_down()
        self.stop_robot()
        self.ctrl_c = True
        
    def stop_robot(self):
        rospy.loginfo("Shutdown time! Stop the robot")
        cmd = Twist()
        cmd.linear.x = 0.0
        cmd.angular.z = 0.0
        self.publish_once_in_cmd_vel(cmd)
        
    def move_circle(self, radius=1.0):
        
        cmd = Twist()
        cmd.linear.x = 0.2
        cmd.angular.z = 0.2
        
        rospy.loginfo("Moving... ")
        self.publish_once_in_cmd_vel(cmd)
        time.sleep(15)
        self.stop_robot()
        rospy.loginfo("######## Finished Moving")
        
        
if __name__ == '__main__':
    rospy.init_node('move_robot_circle_test', anonymous=True)
    moveRobotCircle_object = MoveRobotCircle()
    try:
        moveRobotCircle_object.move_circle()
    except rospy.ROSInterruptException:
        pass
            
        