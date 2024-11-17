import rclpy
from rclpy.node import Node

from std_msgs.msg import String

class MavrosSimulation(Node):
    def __init__(self):
        super().__init__('Mavros Simulation')
        self.subscriber = self.create_subscription(String, "/telem_msg", self.telem_cb, 10)
    
    def telem_cb(self, msg):
        self.get_logger().info(f"Get msg: {msg.data}")

def main(args=None):
    rclpy.init(args=args)
    mavros_sim = MavrosSimulation()
    rclpy.spin(mavros_sim)
    mavros_sim.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()