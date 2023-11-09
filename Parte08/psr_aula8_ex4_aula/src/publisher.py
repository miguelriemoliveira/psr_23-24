#!/usr/bin/env python3

import argparse
import rospy
from std_msgs.msg import String
from psr_aula8_ex4_aula.msg import Dog

def main():

    # -------------------------------------------
    # Initialization
    # -------------------------------------------

    # Setup of argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--topic', type=str, help='Topic name to subscribe to.',
        default='canine_stuff')
    parser.add_argument('-f', '--frequency', type=int, help='Publication frequency.', default=1)
    parser.add_argument('-c', '--content', type=str, help='Content to publish.',
                        default='silencio absoluto ...')
    args = vars(parser.parse_args())

    # Setup ROS
    pub = rospy.Publisher(args['topic'], Dog, queue_size=10)

    rospy.init_node('publisher', anonymous=True)


    rate = rospy.Rate(args['frequency'])
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