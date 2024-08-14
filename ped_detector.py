import cv2
import imutils

# Initializing the HOG person
# detector
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
  
cap = cv2.VideoCapture("assets/human_detect.mp4")
  
while cap.isOpened():
    # Reading the video stream
    ret, gray = cap.read()
    gray = cv2.cvtColor(gray, cv2.COLOR_BGR2GRAY) 
    if ret:
        gray = imutils.resize(gray, 
                               width=min(450, gray.shape[1]))
  
        (regions, _) = hog.detectMultiScale(gray,
                                            winStride=(4, 4),
                                            padding=(2, 2),
                                            scale=1.05)
  
        # Drawing the regions in the 
        # Image
        for (x, y, w, h) in regions:
            cv2.rectangle(gray, (x, y),
                          (x + w, y + h), 
                          (0, 0, 255), 2)
  
        # Showing the output Image
        cv2.imshow("Image", gray)
        if cv2.waitKey(1) == ord("q"):
            break
cap.release()
cv2.destroyAllWindows()