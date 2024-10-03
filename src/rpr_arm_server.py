#!/usr/bin/python3

import rospy
import actionlib
from rpr_arm.msg import RprTaskAction, RprTaskResult
import sys
import moveit_commander

class TaskServer(object):
    result_ = RprTaskResult()
    arm_goal_ = []
    gripper_goal_ = []

    def __init__(self, name):
        self.action_name_ = name
        moveit_commander.roscpp_initialize(sys.argv)
        self.arm_move_group_ = moveit_commander.MoveGroupCommander('rpr_arm')
        self.gripper_move_group_ = moveit_commander.MoveGroupCommander('rpr_gripper')
        
        self.as_ = actionlib.SimpleActionServer(self.action_name_, RprTaskAction, execute_cb=self.execute_cb, auto_start=False)
        self.as_.start()

    def execute_cb(self, goal):
        success = True
        
        if goal.task_number == 0:
            self.arm_goal_ = [0.0, 0.0, 0.0]
            self.gripper_goal_ = [0.0, 0.0]
        elif goal.task_number == 1:
            self.arm_goal_ = [0.0, -1.57, 0.86]
            self.gripper_goal_ = [0.0, 0.0] 
        elif goal.task_number == 2:
            self.arm_goal_ = [0.0, -1.57, 0.86]
            self.gripper_goal_ = [0.07, 0.07]
        elif goal.task_number == 3:
            self.arm_goal_ = [-1.4, -1.0, 1.0]
            self.gripper_goal_ = [0.03, 0.03]
        elif goal.task_number == 4:
            self.arm_goal_ = [1.4, -1.0, 1.0]
            self.gripper_goal_ = [0.03, 0.03]
        else:
            rospy.logerr('Invalid Goal')
            return

        self.arm_move_group_.go(self.arm_goal_, wait=True)
        self.gripper_move_group_.go(self.gripper_goal_, wait=True)

        self.arm_move_group_.stop()
        self.gripper_move_group_.stop()

        if self.as_.is_preempt_requested():
            rospy.loginfo('%s Preempted' %self.action_name_)
            self.as_.set_preempted()
            success=False
        
        if success:
            self.result_.success=True
            rospy.loginfo('%s Succeeded' %self.action_name_)
            self.as_.set_succeeded(self.result_)

if __name__ == '__main__':
    rospy.init_node('task_server')
    server = TaskServer(rospy.get_name())
    rospy.spin()