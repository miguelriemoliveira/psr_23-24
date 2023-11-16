#!/usr/bin/env python3

import argparse

from colorama import Fore, Style
import rospy
from std_msgs.msg import String


def main():

    # -------------------------------------------
    # Initialization
    # -------------------------------------------

    # Setup ROS
    pub = rospy.Publisher('topic_name', String, queue_size=10)

    rospy.init_node('publisher', anonymous=True)

    # read a private parameter in ros
    frequency = rospy.get_param('/publisher/frequency', 1.0)
    if frequency == 1:
        rospy.logwarn('Could not read param frequency')
    # -------------------------------------------
    # Execution
    # -------------------------------------------

    rate = rospy.Rate(frequency)
    while not rospy.is_shutdown():

        message_to_send = 'some content'

        # read highlight_text_color parameter to know which color to use in prints
        print_color = rospy.get_param('/highlight_text_color', 'MAGENTA')

        rospy.loginfo(getattr(Fore, print_color) + message_to_send + Style.RESET_ALL)

        # rospy.logerr('Something went very wrong')

        pub.publish(message_to_send)
        rate.sleep()


if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass
