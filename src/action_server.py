#!/usr/bin/python3

import rospy
import actionlib
from rpr_arm.msg import FibonaciAction, FibonaciResult, FibonaciFeedback

class FibonaciActionServer(object):

    feedback_ = FibonaciFeedback()
    result_ = FibonaciResult()

    def __init__(self, name):
        self.action_name_ = name
        self.as_  = actionlib.SimpleActionServer(self.action_name_, FibonaciAction, execute_cb=self.execute_cb, auto_start=False)
        self.as_.start()
        rospy.loginfo('Server Started Sucessfully')

    def execute_cb(self, goal):
        rospy.loginfo('Goal received %s'%goal.goal)
        r = rospy.Rate(1)
        sucess = True
        self.feedback_.sequence = []
        self.feedback_.sequence.append(1)
        self.feedback_.sequence.append(1)

        for i in range(1, goal.goal-1):

            if self.as_.is_preempt_requested():
                rospy.loginfo('%s Preemented' %self.action_name_)
                self.as_.set_preempted()
                sucess=False
                break
            self.feedback_.sequence.append(self.feedback_.sequence[i] + self.feedback_.sequence[i-1])
            self.as_.publish_feedback(self.feedback_)
            r.sleep()
        
        if sucess:
            self.result_.sequence = self.feedback_.sequence
            rospy.loginfo('%s Succeeded' %self.action_name_)
            self.as_.set_succeeded(self.result_)

if __name__=="__main__":
    rospy.init_node('Fibonaci')
    server = FibonaciActionServer('Fibonaci')
    rospy.spin()


