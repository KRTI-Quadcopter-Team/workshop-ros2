import rclpy
from rclpy.node import Node

from custom_interface.msg import NaviVel, SensorData

class AvoidenceProcess(Node):
    def __init__(self):
        super().__init__('Avoid Process')
        self.publisher = self.create_publisher(NaviVel, "/cmd_vel", 10)
        self.subscriber = self.create_subscription(SensorData, "/sensor_data", self.sensor_cb, 10)
        timer_period = 0.5
        self.timer = self.create_timer(timer_period, self.timer_cb)
    
    def sensor_cb(self, msg):
        self.get_logger().info(f"get Data: [{msg.lidar_front}, {msg.lidar_right}, {msg.lidar_back}, {msg.lidar_left}]")
    
    def timer_cb(self):
        msg = NaviVel()
        msg.avoid = True
        msg.avoid_vel = "roll pitch yaw"
        self.publisher.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    avoid_process = AvoidenceProcess()
    rclpy.spin(avoid_process)
    avoid_process.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()