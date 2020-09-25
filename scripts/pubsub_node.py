#!/usr/bin/python

import rospy
from class_pubsub_polling import LIDAR_RYCSV

# Init of program
if __name__ == '__main__':

    rospy.init_node('nodo_rycsv', anonymous=True)

    rospy.loginfo("Node init")

    objeto = LIDAR_RYCSV()

    # Polling con callback
    rate = rospy.Rate(20) # 20 Hz

    while (not rospy.is_shutdown()):

        objeto.pub.publish(objeto.newMsg)
        rate.sleep()

    rospy.spin()