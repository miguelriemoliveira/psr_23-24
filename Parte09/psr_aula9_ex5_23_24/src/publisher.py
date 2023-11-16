#!/usr/bin/env python3

import argparse
import rospy
from std_msgs.msg import String
from psr_aula8_ex4_aula.msg import Dog


def main():

    # -------------------------------------------
    # Initialization
    # -------------------------------------------

    # Setup ROS
    pub = rospy.Publisher('topic', Dog, queue_size=10)

    rospy.init_node('publisher', anonymous=True)

    frequency = rospy.get_param('~frequency', 50)

    rate = rospy.Rate(frequency)
    while not rospy.is_shutdown():

        # Construct the message to send
        message_to_send = Dog()
        message_to_send.name = 'Nono'
        message_to_send.color = 'Black'
        message_to_send.age = 9
        message_to_send.brothers.append('Bobi')
        message_to_send.brothers.append('Lassie')

        rospy.loginfo(message_to_send)
        pub.publish(message_to_send)
        rate.sleep()


if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass
