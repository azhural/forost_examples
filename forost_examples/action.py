from forost_interfaces.srv import ActionIface

import rclpy
from rclpy.node import Node

class ActionService(Node):
    def __init__(self):
        super().__init__("action_service")
        self.srv = self.create_service(ActionIface, "action", self.cb)

    def cb(self, request, response):
        for x in range(5):
            self.get_logger().info("Doing some work...")
        response.status = ActionIface.Response.SUCCESS;
        return response

def main(args=None):
    rclpy.init(args=args)
    service = ActionService()
    rclpy.spin(service)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
