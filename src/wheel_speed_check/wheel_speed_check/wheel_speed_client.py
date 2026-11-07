import rclpy
from rclpy.node import Node
from robot_interfaces.msg import WheelSpeeds
from robot_interfaces.srv import WheelSpeedCheck

class WheelSpeedClient(Node):
    def __init__(self):
        super().__init__("wheel_speed_client")
        self.client=self.create_client(WheelSpeedCheck,"SpeedCheck")
        self.create_subscription(WheelSpeeds,"wheels_speed",self.received,10)
    def received(self,msg):
        Check=WheelSpeedCheck.Request()
        Check.right_wheel=msg.right_wheel
        Check.left_wheel=msg.left_wheel
        Check.speed_limit=5.0
        future=self.client.call_async(Check)
        self.get_logger().info("Request has been sent!")
        future.add_done_callback(self.done)
    def done(self,future):
        response=future.result()
        if response.limit_exceeded==False:
            if(response.speed_margin==0):
                self.get_logger().info("You are on the egde! It's preferable to slow down a bit.")
            else:
                self.get_logger().info("You are within the limit.")
        else:
            self.get_logger().info("You are exceeding the speed limit!")
def main():
    rclpy.init()
    Client=WheelSpeedClient()
    Client.client.wait_for_service()
    rclpy.spin(Client)
    Client.destroy_node()
    rclpy.shutdown()
if __name__=="__main__":
    main()