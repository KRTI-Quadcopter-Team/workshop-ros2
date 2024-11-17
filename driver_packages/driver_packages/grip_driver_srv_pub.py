import rclpy
from rclpy.node import Node

from std_msgs.msg import Bool
from custom_interface.srv import Grip

class GripDriver(Node):
    def __init__(self):
        super().__init__('Grip Driver')
        self.publisher = self.create_publisher(Bool, "status_pwr", 10)
        self.servis = self.create_service(Grip, "grip_power", self.servis_callback)
        timer_period = 0.5
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.power_on = False
    
    def servis_callback(self, req, res):
        self.power_on = req.power
        res.status = self.power_on
        self.get_logger().info(f"Grip Power changed to: {self.power_on}")

    def timer_callback(self):
        msg = Bool()
        msg.data = self.power_on
        

def main(args=None):
    rclpy.init(args=args)
    grip_driver = GripDriver()
    rclpy.spin(grip_driver)
    grip_driver.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()