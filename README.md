# SOFAR_ASSIGNMENT-4  GROUP-25

## Multi-floor navigation with ROS2, using the Nav2 package.

![turtlebot-3-waffle](https://user-images.githubusercontent.com/81651764/188286808-ea797ca2-dca0-4cbf-b6c7-a79a56358594.jpg)


Multi-floor navigation with ROS2, using the Nav2 package [1].
The idea of this assignment is to construct in simulation a multi-floor environment,
where each floor has a different map layout. The robot knows a priori the individual
maps of each floor but needs some sort of state machine mechanism to dynamically
change the current loaded map for navigation upon entering another floor.




![Screenshot from 2022-09-03 22-19-39](https://user-images.githubusercontent.com/81651764/188286626-f41bbd84-87df-41b7-b8f4-bbcaf08febac.png)
![Screenshot from 2022-09-03 22-20-19](https://user-images.githubusercontent.com/81651764/188286627-e854a4ee-724b-4dba-b40c-acd65d36ddf8.png)
![Screenshot from 2022-09-03 22-20-33](https://user-images.githubusercontent.com/81651764/188286628-a1fcbde7-19ac-4f36-b3eb-91f831677dd1.png)

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


Example Maps in this package:
![Screenshot from 2022-09-02 23-28-22](https://user-images.githubusercontent.com/81651764/188286635-487ae264-848e-4a10-82fb-65ba965cbbd7.png)
![Screenshot from 2022-09-02 23-32-52](https://user-images.githubusercontent.com/81651764/188286636-e80d15e6-37f7-4aff-a08f-4041ba2a4109.png)
![Screenshot from 2022-09-02 23-37-08](https://user-images.githubusercontent.com/81651764/188286637-c14b758d-32eb-46ba-9305-9263288b9d8f.png)
