from launch import LaunchDescription
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    return LaunchDescription([
        Node(
            namespace='jt16_front',
            package='hesai_ros_driver',
            executable='hesai_ros_driver_node',
            name='hesai_ros_driver_node',
            output='screen',
            parameters=[{'config_path': 'config/JT16_front_config.yaml'}]
        ),
        Node(
            namespace='jt16_rear',
            package='hesai_ros_driver',
            executable='hesai_ros_driver_node',
            name='hesai_ros_driver_node',
            output='screen',
            parameters=[{'config_path': 'config/JT16_rear_config.yaml'}]
        ),
        Node(
            namespace='ot128',
            package='hesai_ros_driver',
            executable='hesai_ros_driver_node',
            name='hesai_ros_driver_node',
            output='screen',
            parameters=[{'config_path': 'config/OT128_config.yaml'}]
        ),
        Node(
            package='rviz2',
            executable='rviz2',
            name='rviz2',
            output='screen',
            arguments=['-d', get_package_share_directory('hesai_ros_driver') + '/rviz/rviz2.rviz']
        )
    ]) 
