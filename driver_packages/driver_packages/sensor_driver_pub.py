import rclpy
from rclpy.node import Node
import random
from custom_interface.msg import SensorData

class SensorDataDriver(Node):
    def __init__(self):
        super().__init__('Sensor Driver')
        self.publisher = self.create_publisher(SensorData, "sensor_data", 10)
        timer_period = 0.5
        self.timer = self.create_timer(timer_period, self.timer_callback)

    def rand_int(self):
        return random.randint(10, 200)

    def timer_callback(self):
        msg = SensorData()
        msg.lidar_front = self.rand_int()
        msg.lidar_right = self.rand_int()
        msg.lidar_back = self.rand_int()
        msg.lidar_left = self.rand_int()
        self.publisher.publish(msg)
        self.get_logger().info("Publishing sensor...")

def main(args=None):
    rclpy.init(args=args)

    sensor_driver_pub = SensorDataDriver()

    rclpy.spin(sensor_driver_pub)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    sensor_driver_pub.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
