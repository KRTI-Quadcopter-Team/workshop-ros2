import rclpy
from rclpy.node import Node

from sensor_msgs.msg import Image
from custom_interface.msg import NaviVel, SensorData
from std_msgs.msg import Bool

class GUIStatus(Node):
    def __init__(self):
        super().__init__('GUI_Status')
        self.subscriber_img = self.create_subscription(Image, "/detected_img", self.image_cb, 10)
        self.subscriber_vel = self.create_subscription(NaviVel, "/cmd_vel", self.navi_cb, 10)
        self.subscriber_sensor = self.create_subscription(SensorData, "/sensor_data", self.sensor_cb, 10)
        self.subscriber_grip = self.create_subscription(Bool, "/status_pwr", self.grip_cb, 10)
        
    def grip_cb(self, msg):
        pass
        
    def sensor_cb(self, msg):
        pass
        
    def navi_cb(self, msg):
        pass
    
    def image_cb(self):
        pass

def main(args=None):
    rclpy.init(args=args)
    gui_status = GUIStatus()
    rclpy.spin(gui_status)
    gui_status.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()