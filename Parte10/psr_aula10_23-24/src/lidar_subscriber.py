#!/usr/bin/env python3

# --------------------------------------------------
# Miguel Riem Oliveira.
# PSR, September 2020.
# Adapted from http://wiki.ros.org/ROS/Tutorials/WritingPublisherSubscriber%28python%29
# -------------------------------------------------
import argparse
from colorama import Fore
from functools import partial
from math import cos, sin

import rospy
from std_msgs.msg import String, Header
from sensor_msgs.msg import LaserScan, PointCloud2, PointField
from sensor_msgs import point_cloud2
from visualization_msgs.msg import Marker, MarkerArray
from geometry_msgs.msg import Point

highlight_text_color = 'RED'


def laserscanMessageReceivedCallback(msg, publisher):
    rospy.loginfo('Received LaserScan msg')

    clusters = []
    delta = 0.5
    # Clustering
    for idx, r in enumerate(msg.ranges):
        theta = msg.angle_min + msg.angle_increment * idx  # compute value of theta
        x, y, z = r * cos(theta), r * sin(theta), 0  # polar to cartesian

        if not clusters:  # Create a new cluster at the beginning
            cluster = {'xs': [x], 'ys': [y], 'zs': [z], 'thetas': [theta], 'rs': [r]}
            clusters.append(cluster)
            continue

        # Get the last r measurement in the list of rs of the last cluster in the list of clusters
        prev_r = clusters[-1]['rs'][-1]

        if r > prev_r + delta or r < prev_r - delta:  # r measurements are different enough, create new cluster
            cluster = {'xs': [x], 'ys': [y], 'zs': [z], 'thetas': [theta], 'rs': [r]}
            clusters.append(cluster)
        else:  # r measurements are simular enough, add point to existing last cluster
            clusters[-1]['xs'].append(x)
            clusters[-1]['ys'].append(y)
            clusters[-1]['zs'].append(z)
            clusters[-1]['thetas'].append(theta)
            clusters[-1]['rs'].append(r)

    # Publish a marker with a list of spheres per cluster

    ma = MarkerArray()

    for cluster_idx, cluster in enumerate(clusters):

        # Create the cluster marker
        marker = Marker(header=Header(stamp=rospy.Time.now(), frame_id="left_laser"),
                        ns="my_namespace", id=cluster_idx, type=Marker.SPHERE_LIST, action=Marker.ADD)

        marker.pose.orientation.w = 1.0

        marker.scale.x = 0.4
        marker.scale.y = 0.4
        marker.scale.z = 0.4
        marker.color.a = 0.3
        import random
        marker.color.r = random.random()
        marker.color.g = random.random()
        marker.color.b = random.random()

        for x, y, z in zip(cluster['xs'], cluster['ys'], cluster['zs']):
            marker.points.append(Point(x=x, y=y, z=z))

        ma.markers.append(marker)

    # Publish marker array
    publisher.publish(ma)


def main():
    # initialize the ros node
    rospy.init_node('lidar_subscriber', anonymous=True)

    # setup the point cloud subscriber
    publisher = rospy.Publisher('/marker_array', MarkerArray, queue_size=1)

    # setup the laserscan subscriber
    rospy.Subscriber('/left_laser/laserscan', LaserScan, partial(laserscanMessageReceivedCallback, publisher=publisher))

    rospy.spin()


if __name__ == '__main__':
    main()
