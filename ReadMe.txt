Instructions on how to clone the repo

1. git clone "https://github.com/Eduardo-montalvo/Turtlebot_project.git"
2. git commit -m "Commit message"
3. git push origin develop
4. git add -A
5. git pull
6. ros2 launch turtlebot4_ignition_bringup ignition.launch.py

Launch the simulation with the launch file
1. source install/setup.bash
2. ros2 launch inicialization demo.launch.xml

How to launch the nodes
1. source ~/.bashrc 
2. ros2 run robot_movement Movement_exec
3. ros2 run robot_movement Messager
