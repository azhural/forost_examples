from forost_interfaces.srv import ConditionIface

import rclpy
from rclpy.node import Node

class ConditionSuccessService(Node):
    def __init__(self):
        super().__init__("condition_success_service")
        self.srv = self.create_service(ConditionIface, "cond_success", self.cb)

    def cb(self, request, response):
        self.get_logger().info("Condition Success")
        response.status = ConditionIface.Response.SUCCESS
        return response

def main(args=None):
    rclpy.init(args=args)
    service = ConditionSuccessService()
    rclpy.spin(service)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
