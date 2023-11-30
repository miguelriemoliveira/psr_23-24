#!/usr/bin/env python3

import math
import turtlesim.msg
import tf
import rospy
import roslib


def main():

    # -------------------------------
    # Initialization
    # -------------------------------
    rospy.init_node('circular_frame')

    br = tf.TransformBroadcaster()

    # -------------------------------
    # Execution
    # -------------------------------

    rate = rospy.Rate(10)
    theta = 0
    radius = rospy.get_param("~radius", 2)
    velocity = rospy.get_param("~velocity", 0.1)
    while not rospy.is_shutdown():

        x = radius * math.cos(theta)
        y = radius * math.sin(theta)

        br.sendTransform((x, y, 0),
                         tf.transformations.quaternion_from_euler(0, 0, 0),
                         rospy.Time.now(),
                         rospy.remap_name("child"), rospy.remap_name("parent"))

        print('Published the transformations')
        rate.sleep()

        theta += velocity


if __name__ == '__main__':
    main()
