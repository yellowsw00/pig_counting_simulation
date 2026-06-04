#!/usr/bin/env python3
import rospy
from sensor_msgs.msg import PointCloud, PointCloud2
import sensor_msgs.point_cloud2 as pc2
from std_msgs.msg import Header

def cb(msg: PointCloud):
    header = Header(stamp=msg.header.stamp, frame_id=msg.header.frame_id)
    pts = [(p.x, p.y, p.z) for p in msg.points]
    pc2_msg = pc2.create_cloud_xyz32(header, pts)
    pub.publish(pc2_msg)

if __name__ == "__main__":
    rospy.init_node("pointcloud_to_pointcloud2")
    pub = rospy.Publisher("/person_lidar/points", PointCloud2, queue_size=1)
    rospy.Subscriber("/person_lidar/scan", PointCloud, cb, queue_size=1)
    rospy.spin()
