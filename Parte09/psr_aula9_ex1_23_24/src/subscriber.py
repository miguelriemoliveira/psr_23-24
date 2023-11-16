#!/usr/bin/env python3
import argparse
from functools import partial

from colorama import Fore, Style
import rospy
from std_msgs.msg import String


def callback(message_received):

    # read highlight_text_color parameter to know which color to use in prints
    print_color = rospy.get_param('/highlight_text_color', 'MAGENTA')

    rospy.loginfo(getattr(Fore, print_color) + message_received.data + Style.RESET_ALL)


def main():

    # -------------------------------------------
    # Initialization
    # -------------------------------------------

    # Setup ROS
    rospy.init_node('subscriber', anonymous=True)

    rospy.Subscriber('topic_name', String, callback)

    # -------------------------------------------
    # Execution
    # -------------------------------------------
    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

    # -------------------------------------------
    # Termination
    # -------------------------------------------


if __name__ == '__main__':
    main()
