#!/usr/bin/env python
import rospy
from pynput import keyboard
from std_msgs.msg import String
from std_msgs.msg import Header
from sensor_msgs.msg import Joy


TERMINATE = False
buttons = [0] * 26


def talker():
    pub = rospy.Publisher('keyboard', Joy, queue_size=10)
    rospy.init_node('emitter', anonymous=True)
    rate = rospy.Rate(20)
    cur_id = 0
    while not rospy.is_shutdown():
        now = rospy.get_rostime()
        hd = Header(seq=cur_id, stamp=now, frame_id="0")
        j = Joy(header=hd, axes=[], buttons=buttons)
        pub.publish(j)
        cur_id += 1
        rate.sleep()


def on_press(key):
    global buttons
    try:
        if ord(key.char)-ord('a') >= 0 and ord(key.char)-ord('a') < 26:
            buttons[ord(key.char)-ord('a')] = 1
    except AttributeError:
        pass
    if TERMINATE:
        return False


def on_release(key):
    global buttons
    try:
        if ord(key.char)-ord('a') >= 0 and ord(key.char)-ord('a') < 26:
            buttons[ord(key.char)-ord('a')] = 0
    except AttributeError:
        pass
    if TERMINATE:
        return False
    if key == keyboard.Key.esc:
        # Stop listener
        return False


if __name__ == '__main__':
    with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
        try:
            talker()
        except rospy.ROSInterruptException:
            TERMINATE = True
        listener.join()

