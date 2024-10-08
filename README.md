<div align="center">

# RRR Manipulator 
Simulaton of 3-Dof RRR manipulator using ROS, Gazebo and MoveIt

![Static Badge](https://img.shields.io/badge/Ubuntu-20.04_(Focal_Fossa)-orange)
![Static Badge](https://img.shields.io/badge/ROS-Noetic_Ninjemys-lightgreen)
![Static Badge](https://img.shields.io/badge/Python-3.8.10-red)
![Static Badge](https://img.shields.io/badge/Gazebo-11+-blue)
![Static Badge](https://img.shields.io/badge/CAD-SolidWorks-yellow)
![Static Badge](https://img.shields.io/badge/Cloud_Gateway-Ngrok-lightblue)
![Static Badge](https://img.shields.io/badge/LICENSE-MIT-violet)

<br/>

![image](https://github.com/VibhuSharma19/RRR_Manipulator/blob/master/images/Manipulator.png)
</div>

## Table of Contents
* [RRR Manipulator](#rrr-manipulator)
  * [Table of Contents](#table-of-contents)
  * [Overview](#overview)
    * [Features](#features)
  * [Getting Stated](#getting-stated)
    * [Prerequists](#prerequists)
    * [Installation and Build](#installation-and-build)
  * [Usage](#usage)
    * [Individual Joint Control](#individual-joint-control)
    * [MoveIt based control](#moveit-based-control)
  * [Project Visuals](#project-visuals)
  * [Contributing](#contributing)
  * [Contact](#contact)
  * [License](#license)
  * [Acknowledgements](#acknowledgements)



## Overview
This project simulates a custom build 3-dof serial manipulator of RRR (Revolute-Revolute-Revolute) configuration. The simulation and motion planing is achieved using Gazebo and Moveit respectively. This project also features additional integration of Alexa voice command control and custom-created task server control for the manipulator. 

### Features
* __Gazebo Simulation__: The manipulator is simulated in gazebo using custom made controller and can be controlled using Joint State GUI as well as joint commands. The simulation can also be visualized using Rviz.
* __MoveIt Intercative Control__: The manipulator can be controlled and moved to a specific position using the Rviz-MoveIt interactive motion planning. The simulation of the same can also be visualized in Gazebo.
* __Task Server Commander__: A Task server is created using MoveIt API for predefined manipulator positions and used to give target goals using the custom string commands.
* __Alexa Voice Command__: The manipulator can also be commanded to move to a specific pre-defined position using Alexa voice interaction and Task server.
  
## Getting Stated
The overall project is divided into two repositories. A main repository as [RRR_Manipulator](https://github.com/VibhuSharma19/RRR_Manipulator.git) and a secondary (required) repository of MoveIt interfacing [RRR_MoveIt](https://github.com/VibhuSharma19/RRR_Moveit.git). Both the repositories are required to use all the features of the project.

### Prerequists
* __Ubuntu__: 20.04 (_Focal Fossa_)
* __Robot Operating System (ROS)__: Noetic Ninjems
* __Gazebo__: 11 or higher (_Classic_)
* __Python__: 3.8 or higher
* __MoveIt__
* __Ngrok__ and __Amazon Alexa__

[Ngrok](https://ngrok.com/download) is a free tool that is used for cloud gateway for many cloud-based services and uses.  
[Amazon Alexa](https://developer.amazon.com/en-US/alexa/alexa-skills-kit) can be assecced by creating an accunt in Amazon and refer to the tutorials.

### Installation and Build
1. Clone and build the repository along with the MoveIt package:
```sh
$ cd ~/catkin_ws/src  
$ git clone --recurse-submodules https://github.com/VibhuSharma19/RRR_Manipulator.git  
$ cd ~/catkin_ws && rosdep install -r --ignore-src --from-paths src 
$ catkin_make
```

2. Clone and build the repository separately for Gazebo and MoveIt package:
```sh
$ cd ~/catkin_ws/src  
$ git clone https://github.com/VibhuSharma19/RRR_Manipulator.git  
$ git clone https://github.com/VibhuSharma19/RRR_Moveit.git
$ cd ~/catkin_ws && rosdep install -r --ignore-src --from-paths src 
$ catkin_make
```

## Usage

### Individual Joint Control

1. Manipulator simulation using Rviz and Joint State GUI:
```sh
$ roslaunch rrr_arm display.launch
```

1. Gazebo simulation with controller:
```sh
$ roslaunch rrr_arm gazebo.launch

# In another terminal
$ roslaunch rrr_arm controller.launch
```
### MoveIt based control

1. Manipulator control using MoveIt and Rviz:
```sh
$ roslaunch rrr_arm gazebo.launch

# new terminal
$ roslaunch rrr_arm controller.launch

# new terminal
$ roslaunch rrr_moveit move_group.launch

# new terminal
$ roslaunch rrr_moveit moveit_rviz.launch
```

Config file for Rviz is in `rrr_moveit/launch/moveit.rviz`

2. Manipulator control using Task server:
```sh
# all launch as in control using MoveIt and Rviz

# new terminal
$ rosrun rrr_arm rrr_arm_server.py

# commanding using task server
$ rostopic pub /task_server/goal task_number:=(0-4)
```

3. Manipulator control using Alexa Voice Command:
`
```sh
$ roslaunch rrr_arm sim_complete.launch

# new terminal
$ ngrok http 5000
```
Paste the _'Forwarding'_ link of Ngrok to __Alexa Developer Console__ and command the manipulator with the custom based voice commands.

## Project Visuals

* Manipulator in Gazebo World
<p align="center">
<img src="https://github.com/VibhuSharma19/RRR_Manipulator/blob/master/images/gazebo.jpg">
</p>

* Manipulator in Rviz plateform
<p align="center">
<img src="https://github.com/VibhuSharma19/RRR_Manipulator/blob/master/images/display_rviz.png">
</p>

* MoveIt and Rviz interactive Simulation
<p align="center">
<img src="https://github.com/VibhuSharma19/RRR_Manipulator/blob/master/images/moveit_rviz_interface.png">
</p>

* RQT graph for complete simulation, including Alexa, Task Server and MoveIt tool
<p align="center">   
<img src="https://github.com/VibhuSharma19/RRR_Manipulator/blob/master/images/rosgraph_node_only.png">
</p>

* Manipulator Motion Planning using Rviz-MoveIt interactive tool

https://github.com/user-attachments/assets/2d0d7444-7543-48f7-9c52-da2303824ecb

* Task server based motion planning 

https://github.com/user-attachments/assets/fb9dd42c-8fa0-4701-80c2-55c63b1a3d83

## Contributing

Pull requests and issues are always welcome. You can add additional new features by creating branches and commit changes. Please submit your contribution and report any bugs or issues.


1. Fork the Project
2. Create your New_Feature branch `git checkout -b feature/New_Feature`
3. Commit your changes `git commit -m 'Add some New_Feature'`
4. Push to the branch `git push origin feature/New_Feature`
5. Open a Pull Request

## Contact
__*VIBHU SHARMA*__  
_M.Tech (Gold Medalist :1st_place_medal: ) - Automation and Robotics_ <br/>
[![Static Badge](https://img.shields.io/badge/LinkedIn-Vibhu_Sharma-blue)](www.linkedin.com/in/-vibhu-sharma) 
[![Static Badge](https://img.shields.io/badge/Github-VibhuSharma19-white)](https://github.com/VibhuSharma19)

## License
[MIT LICENSE](https://github.com/VibhuSharma19/RRR_Manipulator/blob/master/LICENSE)

## Acknowledgements

* [Robotics and ROS](https://www.udemy.com/course/robotics-and-ros-learn-by-doing-manipulators/?couponCode=KEEPLEARNING) course in __Udemy__


