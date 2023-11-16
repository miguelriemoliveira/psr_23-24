#!/usr/bin/env python3
import argparse

from psr_aula8_ex4_aula.msg import Dog
import rospy
from std_msgs.msg import String


def callback(message_received):

    print('Received Dog message with name ' + message_received.name + ' color ' + message_received.color +
          ' age ' + str(message_received.age) + ' brothers ' + str(message_received.brothers))


def main():

    # -------------------------------------------
    # Initialization
    # -------------------------------------------

    # Setup ROS
    rospy.init_node('subscriber', anonymous=True)
    rospy.Subscriber('topic', Dog, callback)

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
