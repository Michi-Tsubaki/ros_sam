cmake_minimum_required(VERSION 3.0.2)
project(ros_sam)

## Compile as C++11, supported in ROS Kinetic and newer
# add_compile_options(-std=c++11)

find_package(catkin REQUIRED COMPONENTS
  rospy
  cv_bridge
  ros_sam_msgs
)

find_package(Python3 COMPONENTS Interpreter REQUIRED)

execute_process(
  COMMAND ${Python3_EXECUTABLE} -m pip install --upgrade pip
)

execute_process(
  COMMAND ${Python3_EXECUTABLE} -m pip install git+https://github.com/facebookresearch/segment-anything.git
)

## Use this if the package has a setup.py. This macro ensures
catkin_python_setup()

catkin_package(
  CATKIN_DEPENDS rospy cv_bridge ros_sam_msgs
)

#############
## Install ##
#############
catkin_install_python(PROGRAMS
  scripts/sam_node.py
  scripts/sam_test.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)

install(DIRECTORY launch
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
)
