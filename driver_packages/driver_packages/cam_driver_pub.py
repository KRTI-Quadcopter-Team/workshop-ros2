import rclpy
from rclpy.node import Node

from sensor_msgs.msg import Image
import cv2

class CamDriverPub(Node):
    def __init__(self):
        super().__init__('Camera Driver')
        self.publisher = 