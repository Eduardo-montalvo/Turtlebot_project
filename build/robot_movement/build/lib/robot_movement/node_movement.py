#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class MyNode(Node):
    def __init__(self):
        super().__init__("Movement_publisher")
        self.publisher =self.create_publisher(Twist,'/cmd_vel', 10)
        timer_period = 2 # 0.5 hz
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.counter = 0
      
    def timer_callback(self):
        msg=Twist()
        msg.linear.x = -50 #Aqui va el valor al que vamos a meter
        msg.linear.y = 0 #Aqui va el valor al que vamos a meter
        msg.linear.z = 0 #Aqui va el valor al que vamos a meter

        msg.angular.x = 0 #Aqui va el valor al que vamos a meter
        msg.angular.y = 0 #Aqui va el valor al que vamos a meter
        msg.angular.z = 0 #Aqui va el valor al que vamos a meter
        self.publisher.publish(msg) #We publish the distance with this command


def main(args=None):
    rclpy.init(args=args)#First line 
    #Here comes the code
    node = MyNode()
    rclpy.spin(node)
    rclpy.shutdown() #Last line 
if __name__ == "__main__":
    main()