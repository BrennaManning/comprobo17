#!/usr/bin/env python

""" This script is our first ROS node. We'll publish some messages """

from geometry_msgs.msg import PointStamped
import rospy

rospy.init_node('test_message')

r = rospy.Rate(2)
loop_count = 0;
while not rospy.is_shutdown():
	print "looping", loop_count
	loop_count += 1
	r.sleep()


print "Node is finished" 