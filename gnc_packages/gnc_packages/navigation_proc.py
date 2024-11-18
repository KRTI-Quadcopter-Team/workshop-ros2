import rclpy
from rclpy.node import Node

from custom_interface.msg import NaviVel
from std_msgs.msg import String

class NavigationProcess(Node):
    def __init__(self):
        super().__init__('Navugation_Process')
        self.subscriber = self.create_subscription(NaviVel, "/cmd_vel", self.navi_cb, 10)
        self.publisher = self.create_publisher(String, "/telem_msg", 10)
        timer_period = 0.3
        self.timer = self.create_timer(timer_period, self.timer_cb)
    
    def navi_cb(self, msg):
        self.get_logger().info(f"Get command: [{msg.avoid}, {msg.avoid_vel}, {msg.mission_vel}]")
        #process navigation here

    def timer_cb(self):
        msg = String
        msg.data = "All param to lower"
        self.publisher.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    navigation_process = NavigationProcess()
    rclpy.spin(navigation_process)
    navigation_process.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()