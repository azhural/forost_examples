from forost_interfaces.srv import ConditionIface

import rclpy
from rclpy.node import Node

class ConditionFailureService(Node):
    def __init__(self):
        super().__init__("condition_failure_service")
        self.srv = self.create_service(ConditionIface, "cond_fail", self.cb)

    def cb(self, request, response):
        self.get_logger().info("Condition Failure")
        response.status = ConditionIface.Response.FAILURE;
        return response

def main(args=None):
    rclpy.init(args=args)
    service = ConditionFailureService()
    rclpy.spin(service)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
