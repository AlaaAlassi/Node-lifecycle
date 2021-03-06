# Copyright 2018 Open Source Robotics Foundation, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from launch import LaunchDescription
from launch_ros.actions import LifecycleNode
from launch_ros.actions import Node


def generate_launch_description():
    return LaunchDescription([
        LifecycleNode(package='lifecycle', node_executable='lifecycle_talker',
                      node_name='lc_talker', output='screen',parameters= ['/home/alaa/ros2_ws/src/ros2/demos/lifecycle/myparams.yaml']),
        Node(package='lifecycle', node_executable='lifecycle_listener', output='screen'),
        Node(package='lifecycle', node_executable='lifecycle_service_client', output='screen')
    ])
#thisdict =	{
# "brand": "Ford",
#  "model": "Mustang",
#  "year": 1964
#}

#['/home/alaa/ros2_ws/src/ros2/demos/lifecycle/myparams.yaml']