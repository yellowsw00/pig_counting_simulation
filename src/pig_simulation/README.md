# 养猪场仿真项目 - 传感器参数说明文档

本文件记录了该仿真环境中所有传感器的安装参数（外参）及配置信息（内参）。

## 1. 激光雷达 (Livox Avia LiDAR)

### 1.1 安装外参 (Extrinsics)
*   **父坐标系**: `barrier_link` (移动巡检平台)
*   **子坐标系**: `livox_base`
*   **平移 (x, y, z)**: `[3.0, 0.0, 1.7]` (米)
*   **旋转 (roll, pitch, yaw)**: `[0.0, 0.52, -3.14159]` (弧度)
    *   *说明：雷达安装在平台中心前方 3 米，高度 1.7 米，带有约 30 度的下俯角，且水平方向旋转了 180 度。*

### 1.2 性能参数 (Intrinsics)
*   **扫描模式**: 固态非重复扫描 (Livox Avia 模式)
*   **视野范围 (FOV)**: 水平 70.4°, 垂直 77.2°
*   **量程**: 0.1m - 200m

---

## 2. 深度相机 (Hikrobot Style RGB-D)

### 2.1 安装外参 (Extrinsics)
*   **父坐标系**: `livox_base` (LiDAR 基座)
*   **子坐标系**: `camera_base_link`
*   **平移 (x, y, z)**: `[0.0, 0.0, 0.2]` (米)
*   **旋转 (roll, pitch, yaw)**: `[0.0, 0.0, 0.0]` (弧度)
    *   *说明：相机安装在 LiDAR 正上方 0.2 米处。*

### 2.2 相机内参 (Intrinsics)
*   **分辨率**: 1280 x 720 (720p)
*   **水平 FOV**: 1.3962634 弧度 (约 80°)
*   **焦距 (f)**: 约 762.72 像素 (根据 $f = \frac{width}{2 \cdot 	an(hfov/2)}$ 计算)
*   **主点 (cx, cy)**: `[640.0, 360.0]`
*   **畸变 (Distortion)**: `[0, 0, 0, 0, 0]` (仿真理想无畸变)

### 2.3 光学坐标系转换 (Optical Frame)
为了符合 ROS 的相机坐标系约定（Z轴向前），定义了 `camera_optical_link`：
*   **相对于 `camera_base_link` 的旋转**: `rpy="-1.5708 0 -1.5708"`

---

## 3. 传感器数据采集命令

录制包含所有关键数据（TF、雷达点云、相机 RGB-D 及彩色点云）的命令：

```bash
rosbag record -O pig_simulation_data.bag 
/tf 
/tf_static 
/person_lidar/points 
/scan 
/hikrobot_camera/rgb/image_raw 
/hikrobot_camera/rgb/camera_info 
/hikrobot_camera/depth/image_raw 
/hikrobot_camera/depth/camera_info 
/hikrobot_camera/depth/points
```

---

## 4. 坐标系说明 (Coordinate Conventions)
*   **机器人/平台坐标系**: X 向前, Y 向左, Z 向上。
*   **LiDAR 坐标系**: X 向前, Y 向左, Z 向上。
*   **相机光学坐标系**: Z 向前, X 向右, Y 向下。
