import rclpy
from rclpy.node import Node

from sensor_msgs.msg import CompressedImage
import numpy as np
from time import sleep
from cv_bridge import CvBridge
from .CameraEvent.camera_event import Camera


class StreamPublisher(Node):
    def __init__(self):
        super().__init__("stream_publisher")
        self.cap = Camera()
        self.bridge = CvBridge()
        self.publisher = self.create_publisher(CompressedImage, "stream", 10)
        self.publish()
    
    def publish(self) -> None:
        while True:
            try:
                self.frame = self.cap.get_frame()
                msg = self.bridge.cv2_to_compressed_imgmsg(np.array(self.frame))
                self.publisher.publish(msg)
                sleep(0.05)            
            except KeyboardInterrupt:
                sleep(3)

def main(args=None):
    rclpy.init(args=None)
    stream_pubs = StreamPublisher()
    rclpy.spin(stream_pubs)

    stream_pubs.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()
