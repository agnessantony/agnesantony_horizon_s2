#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32

class Node2(Node):

    def __init__(self):
        super().__init__("subscriber_node")
        self.subscription = self.create_subscription(Int32,'distance',self.receiving_distance,10)

    def receiving_distance(self,msg):
        self.get_logger().info(f'Received distance:{msg.data}')

def main(args=None):
    rclpy.init(args=args)
    node = Node2()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ =='__main__':
    main()
