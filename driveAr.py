#/usr/bin/env python
​
import rospy
import time
import numpy as np
from ackermann_msgs.msg import AckermannDriveStamped
from sensor_msgs.msg import LaserScan, Joy, Image
from ar_track_alvar_msgs.msg import AlvarMarkers
from std_msgs.msg import String
​
​
DRIVE_TOPIC = "/drive"
SCAN_TOPIC = "/scan"
AR_TOPIC = "/ar_pose_marker"
​
class ARDrive(object):
    def __init__(self):
        rospy.init_node("ar")
        #initialize publishers and subscribers
        self.drive_pub = rospy.Publisher(DRIVE_TOPIC, AckermannDriveStamped, queue_size = 1)
        self.scan_sub = rospy.Subscriber(SCAN_TOPIC, LaserScan, self.driveCallback)
        self.ar_sub = rospy.Subscriber(AR_TOPIC, AlvarMarkers, self.arCallback)
        self.sound_pub = rospy.Publisher("state", String, queue_size=1)
        
        #initialize cmd object
        self.cmd = AckermannDriveStamped()
        self.cmd.drive.speed = 0
        self.cmd.drive.steering_angle = 0
​
    def driveCallback(self, data):
        '''LIDAR callback, sets drive commands'''
        #TODO: Set drive commands according to the current state
        
        pass
​
    def arCallback(self, tags):
        '''Callback when an AR tag is detected'''
        #TODO: Write your state changes here
        speed = 0
        angle = 0
        for i in tags.markers:
            if tags.markers[i].id == 0:
                speed == 1
            elif tags.markers[i].id == 1:
                speed == -1
            elif tags.markers[i].id == 2:
                speed == 0
            elif tags.markers[i].id == 3:
                angle -= 0.1
            elif tags.markers[i].id == 4:
                angle += 0.1
            elif tags.markers[i].id == 5:
                speed == 1
                angle == 0
        self.cmd.drive.speed = speed
        self.cmd.drive.steering_angle = angle
        pass
​
def main():
    try:
        ic = ARDrive()
        rospy.Rate(100)
        while not rospy.is_shutdown():
            ic.drive_pub.publish(ic.cmd)         
    except rospy.ROSInterruptException:
        exit()
​
if __name__ == "__main__":
    main()r
