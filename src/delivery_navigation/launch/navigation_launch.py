from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    return LaunchDescription([
        Node(
            package='delivery_navigation',
            executable='nav_publisher',
            name='nav_publisher'
        ),
        Node(
            package='delivery_navigation',
            executable='nav_service_server',
            name='nav_service_server'
        ),
        Node(
            package='delivery_navigation',
            executable='nav_subscriber',
            name='nav_subscriber'
        )
    ])
