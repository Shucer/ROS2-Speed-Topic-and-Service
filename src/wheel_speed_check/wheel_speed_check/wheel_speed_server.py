import rclpy
from rclpy.node import Node
from robot_interfaces.srv import WheelSpeedCheck

class WheelSpeedServer(Node):
    def __init__(self):
        super().__init__("wheel_speed_server")
        self.create_service(WheelSpeedCheck,"SpeedCheck",self.action)
    def action(self,request,response):
        m=max(abs(request.left_wheel),abs(request.right_wheel))
        response.speed_margin=request.speed_limit-m
        if(response.speed_margin>=0):
            response.limit_exceeded=False
        else:
            response.limit_exceeded=True
        return response
def main():
    rclpy.init()
    Server=WheelSpeedServer()
    rclpy.spin(Server)
    Server.destroy_node()
    rclpy.shutdown()
if __name__=="__main__":
    main()