import os
from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch_ros.actions import Node

from launch.actions import IncludeLaunchDescription

from launch.launch_description_sources import PythonLaunchDescriptionSource



def generate_launch_description():

    tbot_sim_path = get_package_share_directory('tbot_sim')
    launch_file_dir = os.path.join(tbot_sim_path, 'launch','includes')

    return LaunchDescription([
        
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource([launch_file_dir, '/challenge.launch.py']),
            launch_arguments={'world': 'challenge-1'}.items(),
            ),

        #Node(package='rviz2',namespace='', executable='rviz2', arguments=['-d', os.path.join('/home/bot/ros2_ws/larm_thibault_lemoigne/tuto_sim/launch/launch_config.rviz')]),
        
        Node(package='rviz2',namespace='', executable='rviz2'),
        

        Node(package='teleop_twist_keyboard', namespace='', executable='teleop_twist_keyboard', prefix='gnome-terminal -x', remappings=[('cmd_vel', '/multi/cmd_teleop')]),
    
    ])
