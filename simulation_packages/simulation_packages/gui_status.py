import rclpy
from rclpy.node import Node
import http.server
import socketserver
from functools import partial

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
        # error to run server not found directory
        # self.web_server() 
        
    def web_server(self):
        port = 5050
        root = "../web"

        handler = partial(http.server.SimpleHTTPRequestHandler, directory=root)

        with socketserver.TCPServer(("", port), handler) as httpd:
            self.get_logger().info(f"Running server on http://127.0.0.1:{port}")
            httpd.serve_forever()

    def grip_cb(self, msg):
        pass
        
    def sensor_cb(self, msg):
        pass
        
    def navi_cb(self, msg):
        pass
    
    def image_cb(self, msg):
        pass

def main(args=None):
    rclpy.init(args=args)
    gui_status = GUIStatus()
    rclpy.spin(gui_status)
    gui_status.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()