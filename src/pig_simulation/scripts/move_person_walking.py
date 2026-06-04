#!/usr/bin/env python3
import math
import rospy
from gazebo_msgs.srv import SetModelState
from gazebo_msgs.msg import ModelState
from geometry_msgs.msg import Twist

def main():
    rospy.init_node("move_person_walking")

    model_name = rospy.get_param("~model_name", "barrier_with_lidar")
    amplitude = rospy.get_param("~amplitude", 2.0)   # y range ±amplitude
    period = rospy.get_param("~period", 25.0)        # seconds per cycle (larger = slower)
    x = rospy.get_param("~x", -0.265)
    z = rospy.get_param("~z", 0.1)
    yaw = rospy.get_param("~yaw", 0.0)
    rate_hz = rospy.get_param("~rate", 30.0)

    rospy.wait_for_service("/gazebo/set_model_state")
    set_state = rospy.ServiceProxy("/gazebo/set_model_state", SetModelState)

    rate = rospy.Rate(rate_hz)
    t0 = rospy.Time.now().to_sec()
    omega = 2.0 * math.pi / max(period, 0.1)

    last_t = t0
    last_y = 0.0

    rospy.loginfo("Moving model [%s] along Y in [-%.2f, %.2f]", model_name, amplitude, amplitude)

    while not rospy.is_shutdown():
        t = rospy.Time.now().to_sec()
        dt = max(t - last_t, 1e-3)

        y = amplitude * math.sin(omega * (t - t0))
        vy = (y - last_y) / dt

        state = ModelState()
        state.model_name = model_name
        state.reference_frame = "world"
        state.pose.position.x = x
        state.pose.position.y = y
        state.pose.position.z = z

        half = yaw * 0.5
        state.pose.orientation.x = 0.0
        state.pose.orientation.y = 0.0
        state.pose.orientation.z = math.sin(half)
        state.pose.orientation.w = math.cos(half)

        state.twist = Twist()
        state.twist.linear.y = vy

        try:
            set_state(state)
        except rospy.ServiceException as e:
            rospy.logwarn("set_model_state failed: %s", str(e))

        last_t = t
        last_y = y
        rate.sleep()

if __name__ == "__main__":
    main()
