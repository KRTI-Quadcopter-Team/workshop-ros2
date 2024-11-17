import rclpy
from rclpy.node import Node

from sensor_msgs.msg import Image
from custom_interface.msg import NaviVel
from cv_bridge import CvBridge
import cv2
import numpy as np

class VisionProcess(Node):
    def __init__(self):
        super().__init__('Vision Process')
        self.subscriber = self.create_subscription(Image, "/image_raw", self.image_cb, 10)
        self.publisher_img = self.create_publisher(Image, "/detected_image", 10)
        self.publisher_nav = self.create_publisher(NaviVel, "/cmd_vel", 10)
        timer_period = 0.5
        self.timer = self.create_timer(timer_period, self.timer_cb)
        self.br = CvBridge()
        self.procces_img = np.zeros((100,100,3), dtype=np.uint8)
    
    def image_cb(self, data):
        self.get_logger().info("Receive frame")
        cur_frame = self.br.imgmsg_to_cv2(data)
        # image prccessing
        # now not yet
        procces_img = cur_frame # change this
        self.procces_img = procces_img
    
    def timer_cb(self):
        msg_img = Image()
        msg_cmd = NaviVel()
        msg_img.data = self.br.cv2_to_imgmsg(self.procces_img)
        msg_cmd.mission_vel = "roll pitch yaw" # output after process
        self.publisher_img.publish(msg_img)


def main(args=None):
    rclpy.init(args=args)
    visiom_process = VisionProcess()
    rclpy.spin(visiom_process)
    visiom_process.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()