import rclpy
from rclpy.node import Node

from sensor_msgs.msg import CompressedImage
from custom_interface.msg import NaviVel
from cv_bridge import CvBridge
import cv2
import numpy as np

class VisionProcess(Node):
    def __init__(self):
        super().__init__('Vision_Process')
        self.subscriber = self.create_subscription(CompressedImage, "/image_raw", self.image_cb, 10)
        self.publisher_img = self.create_publisher(CompressedImage, "/detected_img", 10)
        self.publisher_nav = self.create_publisher(NaviVel, "/cmd_vel", 10)
        timer_period = 0.5
        self.timer = self.create_timer(timer_period, self.timer_cb)
        self.br = CvBridge()
        # self.procces_img = np.zeros(shape=(512,512,3), dtype=np.int16)
        self.verify = False
    
    def image_cb(self, msg):
        self.get_logger().info("Receive frame")
        cur_frame = self.br.compressed_imgmsg_to_cv2(msg)
        # cur_frame = np.array(msg.data)
        # image prccessing
        # now not yet
        # cv2.imshow("cam", cur_frame)
        # cv2.waitKey(1)
        procces_img = cur_frame # change this
        self.procces_img = procces_img
        self.verify = True
    
    def timer_cb(self):
        msg_cmd = NaviVel()
        msg_cmd.mission_vel = "roll pitch yaw" # output after process
        if self.verify:
            self.publisher_img.publish(self.br.cv2_to_compressed_imgmsg(self.procces_img))
        self.publisher_nav.publish(msg_cmd)


def main(args=None):
    rclpy.init(args=args)
    visiom_process = VisionProcess()
    rclpy.spin(visiom_process)
    visiom_process.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()