#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
import time
import math
from nav_msgs.msg import Odometry
import tf


"""
rosmsg show nav_msgs/Odometry
std_msgs/Header header
  uint32 seq
  time stamp
  string frame_id
string child_frame_id
geometry_msgs/PoseWithCovariance pose
  geometry_msgs/Pose pose
    geometry_msgs/Point position
      float64 x
      float64 y
      float64 z
    geometry_msgs/Quaternion orientation
      float64 x
      float64 y
      float64 z
      float64 w
  float64[36] covariance
geometry_msgs/TwistWithCovariance twist
  geometry_msgs/Twist twist
    geometry_msgs/Vector3 linear
      float64 x
      float64 y
      float64 z
    geometry_msgs/Vector3 angular
      float64 x
      float64 y
      float64 z
  float64[36] covariance
"""

class OdomTools(object):
    def __init__(self):
        self.init_odom()
        self.odom_subscriber = rospy.Subscriber("/odom", Odometry, self.odom_callback)
        
    def init_odom(self):
        self._odometry = None
        while self._odometry is None:
            try:
                self._odometry = rospy.wait_for_message("/odom", Odometry, timeout=1)
            except:
                rospy.loginfo("/odom topic is not ready yet, retrying")
        
        rospy.loginfo("/odom topic READY")
        
    def odom_callback(self, msg):
        self._odometry = msg
        
    def get_odom_position(self):
        return self._odometry.pose.pose.position
        
    def get_odom_orientation(self):
        return self._odometry.pose.pose.orientation
        
    def calculate_distance_change(self, init_point, finish_point):
        delta_x = finish_point.x - init_point.x
        delta_y = finish_point.y - init_point.y
        delta_z = finish_point.z - init_point.z
        
        delta_x2 = pow(delta_x, 2)
        delta_y2 = pow(delta_y, 2)
        delta_z2 = pow(delta_z, 2)
        
        distance = math.sqrt(delta_x2 + delta_y2 + delta_z2)
        
        return distance
        
    def calculate_yaw_angle_change(self, init_orientation, finish_orientation):

        explicit_init_quat = [init_orientation.x, init_orientation.y, init_orientation.z, init_orientation.w]
        explicit_finish_quat = [finish_orientation.x, finish_orientation.y, finish_orientation.z, finish_orientation.w]

        init_euler = tf.transformations.euler_from_quaternion(explicit_init_quat)
        finish_euler = tf.transformations.euler_from_quaternion(explicit_finish_quat)

        delta_yaw=finish_euler[2]- init_euler[2]
        
        return delta_yaw

class MoveBB8Odom():
    
    def __init__(self):
        self.odom_object = OdomTools()
        self.bb8_vel_publisher = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
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
            connections = self.bb8_vel_publisher.get_num_connections()
            if connections > 0:
                self.bb8_vel_publisher.publish(cmd)
                rospy.loginfo("Cmd Published")
                break
            else:
                self.rate.sleep()
                
    def shutdownhook(self):
        # works better than rospy.is_shut_down()
        self.stop_bb8()
        self.ctrl_c = True
        
    def stop_bb8(self):
        rospy.loginfo("Shutdown time! Stop the robot")
        cmd = Twist()
        cmd.linear.x = 0.0
        cmd.angular.z = 0.0
        self.publish_once_in_cmd_vel(cmd)
        
    def move_x_time(self, moving_time, linear_speed=0.2, angular_speed=0.2):
        
        cmd = Twist()
        cmd.linear.x = linear_speed
        cmd.angular.z = angular_speed
        
        rospy.loginfo("Moving Forwards")
        self.publish_once_in_cmd_vel(cmd)
        time.sleep(moving_time)
        self.stop_bb8()
        rospy.loginfo("######## Finished Moving Forwards")
        
    def move_square(self, side=0.2):
        
        i = 0;
        # More speed, more time to stop
        time_magnitude = side / 0.2
        while not self.ctrl_c and i < 4:
            # Move Forwards
            self.move_x_time(moving_time=(2.0*time_magnitude), linear_speed=0.2, angular_speed=0.0)
            # Stop
            self.move_x_time(moving_time=4.0, linear_speed=0.0, angular_speed=0.0)
            # Turn, the turning is not affected by the length of the side we want
            self.move_x_time(moving_time=3.5, linear_speed=0.0, angular_speed=0.2)
            # Stop
            self.move_x_time(moving_time=0.1, linear_speed=0.0, angular_speed=0.0)
            
            i += 1
        rospy.loginfo("######## Finished Moving in a Square")
        
    def move_distance(self, distance_to_move,linear_speed=0.2):
        
        cmd = Twist()
        cmd.linear.x = linear_speed
        cmd.angular.z = 0.0
        
        
        init_position = self.odom_object.get_odom_position()
        final_position = self.odom_object.get_odom_position()
        distance_moved = self.odom_object.calculate_distance_change(init_position,final_position)
        
        while distance_moved < distance_to_move:
            rospy.loginfo("Moving")
            self.publish_once_in_cmd_vel(cmd)
            self.rate.sleep()
            final_position = self.odom_object.get_odom_position()
            distance_moved = self.odom_object.calculate_distance_change(init_position,final_position)
            rospy.loginfo("Distance Moved::>"+str(distance_moved))
        
        rospy.loginfo("Stopping...")
        cmd.linear.x = 0.0
        cmd.angular.z = 0.0
        self.publish_once_in_cmd_vel(cmd)
        
    def move_angle(self, angle_to_turn, angular_speed=0.2):
        
        cmd = Twist()
        cmd.linear.x = 0.0
        cmd.angular.z = angular_speed
        
        init_orientation = self.odom_object.get_odom_orientation()
        finish_orientation = self.odom_object.get_odom_orientation()
        delta_yaw = self.odom_object.calculate_yaw_angle_change(init_orientation, finish_orientation)
        
        while delta_yaw < angle_to_turn:
            rospy.loginfo("Turning")
            self.publish_once_in_cmd_vel(cmd)
            self.rate.sleep()
            finish_orientation = self.odom_object.get_odom_orientation()
            delta_yaw = self.odom_object.calculate_yaw_angle_change(init_orientation, finish_orientation)
            rospy.loginfo("Angle Moved::>"+str(delta_yaw))
        
        rospy.loginfo("Stopping...")
        cmd.linear.x = 0.0
        cmd.angular.z = 0.0
        self.publish_once_in_cmd_vel(cmd)
    
    def calibrate_turning(self):
        
        init_orientation = self.odom_object.get_odom_orientation()
        while not self.ctrl_c:
            
            finish_orientation = self.odom_object.get_odom_orientation()
            delta_yaw = self.odom_object.calculate_yaw_angle_change(init_orientation, finish_orientation)
            rospy.loginfo("Angle Moved::>"+str(delta_yaw))
            self.rate.sleep()   
        
if __name__ == '__main__':
    rospy.init_node('move_bb8_test', anonymous=True)
    movebb8_object = MoveBB8Odom()
    try:
        movebb8_object.move_distance(distance_to_move = 1.0, linear_speed = 0.2)
    except rospy.ROSInterruptException:
        pass
            
        