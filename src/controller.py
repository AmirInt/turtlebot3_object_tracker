#!/usr/bin/python3

# ROS
import rospy
from geometry_msgs.msg import Twist


class Controller:
    def __init__(self) -> None:
        # Use these Twists to control your robot
        self.move = Twist()
        self.move.linear.x = 0.1
        self.freeze = Twist()

        # The "p" parameter for your p-controller, TODO: you need to tune this
        self.angular_vel_coef = 1

        # TODO: Create a service proxy for your human detection service
        
        # TODO: Create a publisher for your robot "cmd_vel"
    
    def run(self) -> None:
        try:
            while not rospy.is_shutdown():
                # TODO: Call your service, ride your robot
                pass

        except rospy.exceptions.ROSInterruptException:
            pass
                

if __name__ == "__main__":
    rospy.init_node("controller", anonymous=True)
    
    controller = Controller()
    controller.run()
    

