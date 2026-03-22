#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32
import random

class Node1(Node):
    

    def __init__(self):
        super().__init__("publisher_node")
        self.publisher_ = self.create_publisher(Int32, 'distance', 10)
        self.create_timer(1.0, self.send_distance)

    def send_distance(self):
        msg = Int32()
        msg.data = random.randint(1,100)
        self.publisher_.publish(msg)
        self.get_logger().info(f'Publishing distance:{msg.data}')
    

def main(args=None):
    rclpy.init(args=args)
    node = Node1() 
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()