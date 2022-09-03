# SOFAR_ASSIGNMENT-4_GROUP-25

## Multi-floor navigation with ROS2, using the Nav2 package.

Multi-floor navigation with ROS2, using the Nav2 package [1].
The idea of this assignment is to construct in simulation a multi-floor environment,
where each floor has a different map layout. The robot knows a priori the individual
maps of each floor but needs some sort of state machine mechanism to dynamically
change the current loaded map for navigation upon entering another floor.

## Working
   In this assignment social robot in a cafe serving the foods to the customer whom ordered the food from the office.Tee main goal is the multifloor robot movement function.  

## Installation Setup

  This package is developed with the ROS2 Humble to install this follow the official documentation [Ros2](https://docs.ros.org/en/humble/index.html)

 OS Version:Ubuntu22.04
 
## Packages to be installed   

       sudo apt install ros-humble-nav2* ros-humble-turtlebot3*
       
   Use this command for installing the packages needed for the assignment and clone the package from the [Main Package](https://github.com/Koushikmani/sofar.git) .After installing the packages needed build the package with the command.
        
      '''
         colcon build
         
      '''
## Process to execute the Assignment:

Testing Process:
Terminal1
        ros2 launch sofar_assignment tb3_gazebo_stage1.py headless:=False

Terminal2
          ros2 launch sofar_assignment multi_floor_navigation_launch.py

Terminal3
           python3 statemachine.py

Updated Final:
Terminal1:
            ros2 launch sofar_assignment sofar_robot.launch.py 
            
## References
[ros2 Examples](https://automaticaddison.com/how-to-load-a-new-map-for-multi-floor-navigation-using-ros-2/) /
[Nav2](https://navigation.ros.org/) /
[Gazebo Elevator Plugin](Gazebo Elevator Plugin: https://osrf-distributions.s3.amazonaws.com/gazebo/api/6.1.0/classgazebo_1_1ElevatorPlugin.html) /
[Navmap](Simple Nav2 API (including methods to plan navigation, change active map and other utilities) / https://navigation.ros.org/commander_api/index.html) /


