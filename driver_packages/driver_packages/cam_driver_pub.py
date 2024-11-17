import rclpy
from rclpy.node import Node

from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2

class CamDriverPub(Node):
    def __init__(self):
        super().__init__('Camera Driver')
        self.publisher = self.create_publisher(Image, 'image_raw', 10)
        timer_period = 0.5
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.cap = cv2.VideCapture(0)
        self.br = CvBridge()
    
    def timer_callback(self):
        ret, frame = self.cap.read()

        if ret:
            self.publisher.publish(self.br.cv2_to_imgmsg(frame)) 
            self.get_logger().info('Publishing video frame')

def main(args=None):
   
  # Initialize the rclpy library
  rclpy.init(args=args)
   
  # Create the node
  cam_driver_pub = CamDriverPub()
   
  # Spin the node so the callback function is called.
  rclpy.spin(cam_driver_pub)
   
  # Destroy the node explicitly
  # (optional - otherwise it will be done automatically
  # when the garbage collector destroys the node object)
  cam_driver_pub.destroy_node()
   
  # Shutdown the ROS client library for Python
  rclpy.shutdown()
   
if __name__ == '__main__':
  main()