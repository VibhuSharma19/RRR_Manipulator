#!/usr/bin/python3

import rospy
import actionlib
from rrr_arm.msg import FibonaciAction, FibonaciGoal

def fibonaci_client():
    client = actionlib.SimpleActionClient('Fibonaci', FibonaciAction)
    client.wait_for_server()
    goal = FibonaciGoal(goal=15)
    print("Sending goal %s" %goal.goal)
    client.send_goal(goal)
    client.wait_for_result()
    return client.get_result()
    
if __name__=="__main__":
    rospy.init_node('Fibonaci_client')
    rospy.loginfo("Fibonaci Client Started Successfully")
    result = fibonaci_client()
    print(result)
