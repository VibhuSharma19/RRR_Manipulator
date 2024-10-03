#!/usr/bin/python3

import rospy

def timerCallback(event=None):
    rospy.loginfo("Called Callback function")

if __name__=="__main__":
    rospy.init_node("timer_ros",anonymous=True)
    timer_dur = rospy.Duration(1)
    rospy.Timer(timer_dur,timerCallback)
    rospy.spin()