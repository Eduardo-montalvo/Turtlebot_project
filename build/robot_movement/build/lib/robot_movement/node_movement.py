#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from example_interfaces.msg import String

class MyNode(Node):
    def __init__(self):
        super().__init__("Movement_publisher")
        self.publisher =self.create_publisher(Twist,'/cmd_vel', 10)
        self.inst_subscriber = self.create_subscription(String, "instruction_topic", self.timer_callback, 10)
        self.timer_ = self.create_timer(1.0, self.timer_callback)
      
    def timer_callback(self, msg: String):
        msg=Twist()
        msg2 = String() 
        if (msg2.data == "Foward"):
            msg.linear.x = 1.0 #Aqui va el valor al que vamos a meter
            msg.linear.y = 0.0 #Aqui va el valor al que vamos a meter
            msg.linear.z = 0.0 #Aqui va el valor al que vamos a meter

            msg.angular.x = 0.0 #Aqui va el valor al que vamos a meter
            msg.angular.y = 0.0 #Aqui va el valor al que vamos a meter
            msg.angular.z = 0.0 #Aqui va el valor al que vamos a meter
        elif(msg2.data == "Backward"):
            msg.linear.x = -1.0 #Aqui va el valor al que vamos a meter
            msg.linear.y = 0.0 #Aqui va el valor al que vamos a meter
            msg.linear.z = 0.0 #Aqui va el valor al que vamos a meter

            msg.angular.x = 0.0 #Aqui va el valor al que vamos a meter
            msg.angular.y = 0.0 #Aqui va el valor al que vamos a meter
            msg.angular.z = 0.0 #Aqui va el valor al que vamos a meter
        else:
            msg.linear.x = 0.0 #Aqui va el valor al que vamos a meter
            msg.linear.y = 0.0 #Aqui va el valor al que vamos a meter
            msg.linear.z = 0.0 #Aqui va el valor al que vamos a meter

            msg.angular.x = 0.0 #Aqui va el valor al que vamos a meter
            msg.angular.y = 0.0 #Aqui va el valor al que vamos a meter
            msg.angular.z = 0.0 #Aqui va el valor al que vamos a meter
        self.publisher.publish(msg) #We publish the distance with this command
        self.get_logger().info('Publicar velocidad: {}'.format(msg))
        
    



def main(args=None):
    rclpy.init(args=args)#First line 
    #Here comes the code
    node = MyNode()
    try:
        rclpy.spin(node)
    finally:
        node.destroy_node()
        rclpy.shutdown()
if __name__ == "__main__":
    main()