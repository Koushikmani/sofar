#! /usr/bin/env python3

import time  # Time library
import os
from geometry_msgs.msg import PoseStamped, PoseWithCovarianceStamped # Pose with ref frame and timestamp
from rclpy.duration import Duration # Handles time for ROS 2
import rclpy # Python client library for ROS 2

from nav2_simple_commander.robot_navigator import BasicNavigator, TaskResult # Helper module
from launch_ros.substitutions import FindPackageShare


# Start the ROS 2 Python Client Library
rclpy.init()
package_name = 'sofar_assignment'
pkg_share = FindPackageShare(package=package_name).find(package_name)

# Launch the ROS 2 Navigation Stack
navigator = BasicNavigator()

map_file_path_warehouse = 'maps/cafe_world.yaml'
map_file_path_car = 'maps/car_world.yaml'
map_file_path_hospital = 'maps/office_world.yaml'

cafe_map = os.path.join(pkg_share, map_file_path_cafe)
car_map = os.path.join(pkg_share, map_file_path_car)
office_map = os.path.join(pkg_share, map_file_path_office)

initial_pose = PoseStamped()

initial_pose.header.frame_id = 'map'
initial_pose.header.stamp = navigator.get_clock().now().to_msg()
initial_pose.pose.position.x = 0.0
initial_pose.pose.position.y = 1.0
initial_pose.pose.position.z = 0.0

def moveTo(x, y, name):
    goal_pose = PoseStamped()
    goal_pose.header.frame_id = 'map'
    goal_pose.header.stamp = navigator.get_clock().now().to_msg()
    goal_pose.pose.position.x = x
    goal_pose.pose.position.y = y
    goal_pose.pose.position.z = 0.0
    goal_pose.pose.orientation.x = 0.0
    goal_pose.pose.orientation.y = 0.0
    goal_pose.pose.orientation.z = 0.0
    goal_pose.pose.orientation.w = 1.0
    done = False
    print('[Robot]   Going to ' + name)
    navigator.goToPose(goal_pose)
    while not navigator.isTaskComplete():  
      feedback = navigator.getFeedback()
      if feedback:
        if Duration.from_msg(feedback.navigation_time) > Duration(seconds=180.0):
          navigator.cancelTask()

    result = navigator.getResult()
    if result == TaskResult.SUCCEEDED:
        print('[Robot] Goal status ' + name)
        done = True
    elif result == TaskResult.FAILED:
        print('[Robot]   not reached goal ' + name)
    else:
        print('no status!')
        
    return done

def main():
  goals = ["Runner", 
           "elevator",
           "room1_office" 
           "Snacks1"]
  
  goals_coordinates = [[-0.94, 20.01], 
                       [18.76, 14.50], 
                       [25.19, -25.24], 
                       [16.34, 28.42]]
  i = 0
  have_task = 0
  snacks1_picked = 0
  snacks1_delivered = 0
  
  to_elevator = 0
  done = False 
  floor = 1
  current_goal = goals[0]
  print('[Robot]   Okay, I heard I have a task')
  
 
  while not done:
      if have_task == 0: 
          floor = 1
          current_goal = goals[0]
          navigator.clearAllCostmaps()
          navigator.changeMap(cafe_map)
          isDone = moveTo(goals_coordinates[0][0], goals_coordinates[0][1], current_goal)
          if isDone:
              have_task = 1
              print("[Robot]   So, I need to go via car parking area to reach the office to deliver snacks for the employess")
              to_elevator = 1
              floor = 0
          else:
              print("[Robot]   Trying again")
      elif have_task == 1:
          navigator.clearAllCostmaps()
          navigator.changeMap(car_map)
          isDone = moveTo(goals_coordinates[3][0], goals_coordinates[3][1], "Package")
          if isDone:
              time.sleep(2.0)
              print('[Robot]   I have some snacks , need to go to deliver it in the office...')
              have_task = 2
              floor = 2
              to_elevator = 1
      elif have_task == 2:
          navigator.clearAllCostmaps()
          navigator.changeMap(office_map)
          
          isDone = moveTo(goals_coordinates[2][0], goals_coordinates[2][1], "Office Room 2")
          print('[Robot]   Here you go, sir')
          done = True
      if to_elevator:
          moveTo(goals_coordinates[1][0], goals_coordinates[1][1], "Elevator")
          print('[Robot]   In elevator moving to ' + str(floor) + ' floor')
          time.sleep(3.0)
          to_elevator = 0
  # Shut down the ROS 2 Navigation Stack
  navigator.lifecycleShutdown()

  exit(0)

if __name__ == '__main__':
  main()
