from irobot_create_msgs.msg import InterfaceButtons, LightringLeds

import rclpy
from rclpy.node import Node
from rclpy.qos import qos_profile_sensor_data

class TurtleBot4FirstNode(Node):
    def __init__(self):
        super().__init__('turtlebot4_first_python_node')


def main(args=None):
    rclpy.init(args=args)
    node = TurtleBot4FirstNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()