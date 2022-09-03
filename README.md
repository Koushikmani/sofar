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

  This package is developed with the ROS2 Humble to install this follow the official documentation [Github Pages](https://docs.ros.org/en/humble/index.html)

 OS Version:Ubuntu22.04
 
## Packages to be installed   

       sudo apt install ros-humble-nav2* ros-humble-turtlebot3*
       
   Use this command for installing the packages needed for the assignment and clone the package from the [Github Pages](https://github.com/Koushikmani/sofar.git) .After installing the packages needed build the package with the command.
        
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
[Github Pages](https://automaticaddison.com/how-to-load-a-new-map-for-multi-floor-navigation-using-ros-2/)
[Github Pages](https://navigation.ros.org/)
[Github Pages](Gazebo Elevator Plugin: https://osrf-distributions.s3.amazonaws.com/gazebo/api/6.1.0/classgazebo_1_1ElevatorPlugin.html)
[Github Pages](Simple Nav2 API (including methods to plan navigation, change active map and other utilities): https://navigation.ros.org/commander_api/index.html)

Maps_Gazebo: file:///home/charlie/Pictures/Screenshots/Screenshot%20from%202022-09-02%2023-28-22.png
file:///home/charlie/Pictures/Screenshots/Screenshot%20from%202022-09-02%2023-32-52.png
file:///home/charlie/Pictures/Screenshots/Screenshot%20from%202022-09-02%2023-37-08.png

And Rviz: file:///home/charlie/colcon_ws/src/sofar_assignment/maps/cafe_world.pgm
-300:-94:36:85
file:///home/charlie/colcon_ws/src/sofar_assignment/maps/car_world.pgm
-61:-93:85:84
file:///home/charlie/colcon_ws/src/sofar_assignment/maps/office_world.pgm
-61:238:85:39

