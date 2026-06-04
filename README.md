# Pig Farm Inspection Simulation (养猪场巡检仿真项目)

[![ROS Noetic](https://img.shields.io/badge/ROS-Noetic-blue.svg)](http://wiki.ros.org/noetic)
[![Gazebo 11](https://img.shields.io/badge/Gazebo-11-orange.svg)](http://gazebosim.org/)
[![Platform](https://img.shields.io/badge/Platform-WSL2--Ubuntu20.04-lightgrey.svg)](https://learn.microsoft.com/en-us/windows/wsl/install)

本项目是一个基于 ROS (Noetic) 和 Gazebo 的养猪场自动巡检机器人仿真平台，专门针对 **WSL2 (Ubuntu 20.04)** 环境进行了配置和优化。它模拟了一个搭载高精度传感器的移动巡检平台，能够在 3D 仿真的养猪场环境中进行数据采集、环境监测和算法验证。

## 🌟 项目亮点 (Highlights)
- **环境兼容性**：完美适配 WSL2 + Ubuntu 20.04 + ROS Noetic 环境。
- **高精度传感器仿真**：集成了 Livox Avia 固态激光雷达和海康威视风格的深度相机。
- **真实参数还原**：传感器外参和内参完全参照实际部署场景进行配置。
- **多场景数据支持**：包含佛山（白天）、清远（夜晚）等不同环境下的采集数据示例。

## 🛠 硬件与传感器配置 (Sensor Configuration)

### 1. 激光雷达 (Livox Avia LiDAR)
- **扫描模式**：固态非重复扫描 (Livox Avia Pattern)
- **视野范围 (FOV)**：70.4° (H) x 77.2° (V)
- **安装位置**：位于平台前方 3m，高度 1.7m，下俯角约 30°。

### 2. 深度相机 (RGB-D Camera)
- **分辨率**：1280 x 720 (720p)
- **视野范围 (FOV)**：约 80° (H)
- **安装位置**：位于激光雷达正上方 0.2m。

## 📂 项目结构 (Repository Structure)
```text
.
├── src
│   ├── pig_simulation          # 核心仿真包（包含环境模型、机器人描述及启动配置）
│   └── livox_laser_simulation   # Livox 激光雷达 Gazebo 插件
├── 佛山白天/                   # 实测/仿真数据示例 (Daytime)
├── 清远夜晚/                   # 实测/仿真数据示例 (Nighttime)
└── README_joshua.md            # 本说明文档
```

## 🚀 快速开始 (Getting Started - WSL2/Ubuntu 20.04)

### 环境依赖
- **系统**: Windows 11/10 (WSL2) + Ubuntu 20.04
- **ROS**: Noetic
- **Gazebo**: 11
- **GUI 转发**: 建议使用 WSLg (Windows 11 自带) 或 VcXsrv / MobaXterm (Windows 10)。

### 安装步骤
1. **创建工作空间并克隆代码**：
   ```bash
   mkdir -p ~/pig_ws/src
   cd ~/pig_ws/src
   # 将项目代码解压/放入 src 目录下
   ```

2. **安装必要的依赖**：
   ```bash
   sudo apt-get update
   sudo apt-get install ros-noetic-gazebo-ros-pkgs ros-noetic-gazebo-ros-control ros-noetic-tf2-sensor-msgs
   ```

3. **编译项目**：
   ```bash
   cd ~/pig_ws
   catkin_make
   source devel/setup.bash
   ```

### 运行示例
1. **启动养猪场仿真环境**：
   这将加载养猪场 3D 模型并生成巡检平台及传感器。
   ```bash
   roslaunch pig_simulation start_pig_world.launch
   ```

2. **仅启动激光雷达仿真演示**：
   如果你只想查看 Livox 雷达的扫描效果：
   ```bash
   roslaunch livox_laser_simulation livox_simulation.launch
   ```

3. **查看传感器数据**：
   在另一个终端打开 Rviz：
   ```bash
   rosrun rviz rviz
   ```

## 📊 数据采集 (Data Collection)
你可以使用以下命令记录仿真过程中的关键数据：

```bash
rosbag record -O pig_simulation_data.bag \
/tf /tf_static \
/person_lidar/points \
/scan \
/hikrobot_camera/rgb/image_raw \
/hikrobot_camera/rgb/camera_info \
/hikrobot_camera/depth/image_raw \
/hikrobot_camera/depth/camera_info \
/hikrobot_camera/depth/points
```

## ⚠️ WSL2 特别提示
- **显卡加速**：WSL2 默认支持 GPU 加速。如果遇到 Gazebo 运行卡顿，请确保 Windows 已安装最新的 GPU 驱动。
- **IP 地址**：如果需要在 Windows 端查看数据，请注意 WSL2 的 IP 与宿主机不同。

## 📜 许可证 (License)
本项目遵循 MIT 许可证。
