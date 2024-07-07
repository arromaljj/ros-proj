cmake_minimum_required(VERSION 3.0.2)
project(gazebo_example)

find_package(catkin REQUIRED COMPONENTS
  rospy
  geometry_msgs
  gazebo_ros
)

catkin_package()

include_directories(
  ${catkin_INCLUDE_DIRS}
)

catkin_install_python(PROGRAMS
  scripts/move_robot.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)