# keyboard-emitter

This is ROS node that listens to keyboard and emits `sensor_msgs/Joy` events to `/keyboard` topic when `a-z` key is pressed on keyboard.

The package has several catkin dependencies (described in `package.xml`) and one pip dependency (described in `requirements.txt`). The packages from `requirements.txt` need to be installed system-wide, after which, you can copy the package into your catkin workspace, run `catkin_make`, and after that you'll be able to run the node with `rosrun keyboard_emitter emitter.py`.
