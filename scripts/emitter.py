#!/usr/bin/env python
import rospy
from pynput import keyboard
from std_msgs.msg import String
from std_msgs.msg import Header
from sensor_msgs.msg import Joy

def talker():
    pub = rospy.Publisher('chatter', String, queue_size=10)
    pub2 = rospy.Publisher('keyboard', Joy, queue_size=10)
    rospy.init_node('emitter', anonymous=True)
    rate = rospy.Rate(20)
    cur_id = 0
    while not rospy.is_shutdown():
        now = rospy.get_rostime()
        hd = Header(seq=cur_id, stamp=now, frame_id="0")
        j = Joy(header=hd, axes=[], buttons=[1,2,3])
        pub2.publish(j)
        cur_id += 1

        hello_str = "hello world %s" % rospy.get_time()
        rospy.loginfo(hello_str)
        pub.publish(hello_str)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
