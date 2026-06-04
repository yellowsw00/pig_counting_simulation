cmake_minimum_required(VERSION 3.0.2)
project(pig_simulation)

find_package(catkin REQUIRED)

catkin_package()

install(DIRECTORY launch urdf worlds rviz
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
)