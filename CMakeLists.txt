cmake_minimum_required(VERSION 2.8.3)

project(rrr_arm)

find_package(catkin REQUIRED COMPONENTS
  roscpp
  rospy
  std_msgs
  message_generation
  actionlib
  moveit_ros_planning_interface
)

add_action_files(
  FILES
  Fibonaci.action
  RrrTask.action
)

generate_messages(
  DEPENDENCIES
  std_msgs
  actionlib_msgs
)



catkin_package()

find_package(roslaunch)

foreach(dir config launch meshes urdf action)
	install(DIRECTORY ${dir}/
		DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}/${dir})
endforeach(dir)
