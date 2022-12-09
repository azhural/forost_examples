import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package="forost_examples",
            executable="condition_failure",
            output="screen"
        ),
        Node(
            package="forost_examples",
            executable="condition_success",
            output="screen"
        ),
        Node(
            package="forost_examples",
            executable="action",
            output="screen"
        ),
    ])



