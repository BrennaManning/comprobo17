#!/usr/bin/env python

""" This script is our first ROS node. We'll publish some messages """

from geometry_msgs.msg import PointStamped, PointStamped
from mstd_msgs.msg import Header
import rospy

rospy.init_node('test_message')

r = rospy.Rate(2)
loop_count = 0;

publisher - rospy.Publisher('/my_topic', PointStamped, queue_size=10)

while not rospy.is_shutdown():
	print "looping", loop_count
	loop_count += 1
	my_header = Header(loop_count, rospy.Time.now(), "odom")
	my_point = Point(3.2, 5.4, 0.0)
	my_point_stamped = PointStamped(my_header, my_point)
	publisher.pub(my_point_stamped)
	r.sleep()


print "Node is finished" 