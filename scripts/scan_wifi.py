#!/usr/bin/env python
#encoding: utf8

import rospy
from pimouse_search_wifi.msg import WiFiStatus


if __name__ == '__main__':
    status_file = '/proc/net/wireless'
    rospy.init_node('scan_wifi')
    pub = rospy.Publisher('wifi_status', WiFiStatus, queue_size=5)

    rate = rospy.Rate(30)
    while not rospy.is_shutdown():
        try:
            with open(status_file, 'r') as f:
                status = WiFiStatus()

                lines = f.readlines()

                target_line = lines[2].split()

                status.link = float(target_line[2])
                status.level = float(target_line[3])

                pub.publish(status)
        except IOError:
            rospy.logerr("cannot read from " + status_file)

        rate.sleep()
