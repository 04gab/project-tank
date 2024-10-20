import cv2
import numpy as np
from picamera2 import Picamera2

# Initialize the camera
picam2 = Picamera2()
picam2.preview_configuration.main.size = (640, 480)
picam2.preview_configuration.main.format = "RGB888"
picam2.preview_configuration.align()
picam2.configure("preview")
picam2.start()

lower_blue = np.array([0, 0, 0])
upper_blue = np.array([210, 255, 50])
while True:
   # Capture frame from the camera
   frame = picam2.capture_array()

   # Convert the frame to the HSV color space
   hsv = cv2.cvtColor(frame, cv2.COLOR_RGB2HSV)

   # Create a mask for the color red
   mask = cv2.inRange(hsv, lower_blue, upper_blue)

   kernel = np.ones((5,5),np.uint8)
   mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
   mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)

   # Find contours of the detected objects
   contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

   if contours:
       largest_contour = max(contours, key=cv2.contourArea)

       (x, y, w, h) = cv2.boundingRect(largest_contour)
       cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)

   height_cam, width_cam, _ = frame.shape
  
   print(f"relative position: "
         f"x = {x}/{width_cam}, y = {y}/{height_cam}")
   # Display the original frame with bounding boxes
   cv2.imshow("Color Detection", frame)

   # Break the loop on 'q' key press
   if cv2.waitKey(1) == ord('q'):
       break

# Clean up and close windows
cv2.destroyAllWindows()

