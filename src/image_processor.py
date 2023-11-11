#!/usr/bin/python3

# Python
import copy

# Object detection
import cv2
import numpy as np
from ultralytics import YOLO
from ultralytics.utils.plotting import Annotator
from ultralytics.engine.results import Results

# ROS
import rospy
from sensor_msgs.msg import Image


class ImageProcessor:
    def __init__(self) -> None:
        # Image message
        self.image_msg = Image()

        self.image_res = 240, 320, 3 # Camera resolution: height, width
        self.image_np = np.zeros(self.image_res) # The numpy array to pour the image data into

        # TODO: Subscribe on your robot's camera topic
        # NOTE: Make sure you use the provided listener for this subscription
        self.camera_subscriber = None

        # TODO: Instantiate your YOLO object detector/classifier model
        self.model: YOLO = None
        # TODO: You need to update results each time you call your model
        self.results: Results = None

        self.cv2_frame_size = 400, 320
        cv2.namedWindow("robot_view", cv2.WINDOW_NORMAL)
        cv2.resizeWindow("robot_view", *self.cv2_frame_size)

        # TODO: Setup your "human detection" service
        self.human_detection_server = None

        self.update_view()


    def camera_listener(self, msg: Image):
        self.image_msg.data = copy.deepcopy(msg.data)


    def update_view(self):
        try:
            while not rospy.is_shutdown():
                if len(self.image_msg.data) == 0: # If there is no image data
                    continue

                # Convert binary image data to numpy array
                self.image_np = np.frombuffer(self.image_msg.data, dtype=np.uint8)
                self.image_np = self.image_np.reshape(self.image_res)

                frame = copy.deepcopy(self.image_np)

                # TODO: You can use an "Annotator" to draw object bounding boxes on frame

                cv2.imshow("robot_view", cv2.cvtColor(frame, cv2.COLOR_RGB2BGR))
                cv2.waitKey(1)

        except rospy.exceptions.ROSInterruptException:
            pass


if __name__ == "__main__":
    rospy.init_node("image_processor", anonymous=True)

    rospy.on_shutdown(cv2.destroyAllWindows)

    image_processor = ImageProcessor()

    rospy.spin()


