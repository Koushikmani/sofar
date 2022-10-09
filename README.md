# SOFAR_ASSIGNMENT-4  GROUP-25

## Multi-floor navigation with ROS2, by using the Nav2 package.
### Developed by Koushikmani Maskalmatti Lakshman and Santhosh Sadhanandham under the guidance of professors  Simone Macciò. 
The idea of this assignment is to construct in simulation a multi-floor environment,
where each floor has a different map layout. The robot knows a priori the individual
maps of each floor but needs some sort of state machine mechanism to dynamically
change the current loaded map for navigation upon entering another floor.
![turtlebot-3-waffle](https://user-images.githubusercontent.com/81651764/188286808-ea797ca2-dca0-4cbf-b6c7-a79a56358594.jpg)
![WhatsApp Image 2022-10-09 at 6 31 27 PM](https://user-images.githubusercontent.com/81651764/194768565-9a267e62-92b0-49b5-b935-38ec3bb0cc98.jpeg)
![WhatsApp Image 2022-10-09 at 6 31 40 PM](https://user-images.githubusercontent.com/81651764/194768569-d0dbabc6-a9f6-426d-808c-4e7008731808.jpeg)
![WhatsApp Image 2022-10-09 at 6 31 53 PM](https://user-images.githubusercontent.com/81651764/194768572-8e25321e-be51-4c92-8967-445ccfec507f.jpeg)
![WhatsApp Image 2022-10-09 at 6 32 15 PM](https://user-images.githubusercontent.com/81651764/194768577-e759a366-f073-43db-98a7-ed00cc3c0a57.jpeg)


## Working
  In this task robot will move starting with one story then onto the next subsequent to finishing its task.The proposed arrangement is basic and proficient and works impeccably. The arrangement comprises of a few situations when the robot needs to finish a specific order. The proposed arrangement functions as follows, at first the robot is put on the primary floor, and afterward moves to the laborer to pick something from him. After that robot moves to a unique lift zone. When the robot arrives at the unique zone and stays there for a while, the robot has a chance to move to another floor and powerfully changes the as of now stacked map for route. It is critical to take note of that on each floor there is an exceptional development zone, arriving at which the robot has the potential chance to arrive at another floor. Hence, the primary objective of the assignment, to change the guide after entering another floor, was accomplished. 
## Installation Setup

  This package is developed with the ROS2 Humble and Nav2 package to install this follow the official documentation [Ros2](https://docs.ros.org/en/humble/index.html)

 OS Version:Ubuntu22.04
 
## Packages to be installed(Nav2)  

       sudo apt install ros-humble-nav2* ros-humble-turtlebot3*
       
   Use this command for installing the packages needed for the assignment and clone the package from the [Main Package](https://github.com/Koushikmani/sofar.git) .After installing the packages needed build the package with the command.
        
      '''
         colcon build
         
      '''
## Process to execute the Assignment:

Testing Process:
Terminal1(Gazebo)

    '''
        ros2 launch sofar_assignment tb3_gazebo_stage1.py headless:=False
    '''
Terminal2(Rviz)

    '''
          ros2 launch sofar_assignment multi_floor_navigation_launch.py
    '''
Terminal3(main scripts)

    '''
           python3 state_machine.py
    '''

## References
- [Ros2 Reference](https://automaticaddison.com/how-to-load-a-new-map-for-multi-floor-navigation-using-ros-2/) 
- [Nav2](https://navigation.ros.org/) 

## Presentation of this project

[Project Presentation Group 25](https://unigeit-my.sharepoint.com/:p:/g/personal/s5053566_studenti_unige_it/Eb4GXvMZjCZPkAOPl3CgukEBOmp50PicJvCANtFj14zN7w?e=cdHbTJ)
