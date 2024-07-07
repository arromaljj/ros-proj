#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist

def move_turtle():
    # Initialize the node
    rospy.init_node('move_turtle', anonymous=True)
    # Create a publisher to the topic /turtle1/cmd_vel
    pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    # Set the loop rate
    rate = rospy.Rate(1)
    # Create a Twist message
    move_cmd = Twist()
    move_cmd.linear.x = 2.0
    move_cmd.angular.z = 1.0

    while not rospy.is_shutdown():
        # Publish the Twist message
        pub.publish(move_cmd)
        # Sleep for a while before publishing again
        rate.sleep()

if __name__ == '__main__':
    try:
        move_turtle()
    except rospy.ROSInterruptException:
        print("ERROR")
        pass