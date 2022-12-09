import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    bt_xml = os.path.join(get_package_share_directory("forost_examples"), "trees", "example.xml")

    return LaunchDescription([
        Node(
            package="forost",
            executable="btros_main",
            parameters=[{"bt_xml" : bt_xml}],
            output="screen"
        )
    ])



