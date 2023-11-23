#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from subprocess import call


class InstructionsNode(Node):
    def init(self):
        super().__init__("node_inst_pub")
        self.cmd_inst_pub = self.create_publisher(Twist, "", 10) #La utlima es una queue size
        self.timer = self.create_timer(0.5, self.send_info) #Se llama a la funcion cada 0.5 seg
        self.get_logger().info("Node_inst_pub has been opened")

    def send_info(self):
        msg = Twist()
        msg.something = ""
        self.cmd_inst_pub.publish(msg)


def open_file():
    call(["python", "name.py"])



def main(args=None):
    rclpy.init(args=args)
    open_file()
    node = InstructionsNode
    rclpy.spin(node)
    rclpy.shutdown()