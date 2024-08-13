import cv2
img = cv2.imread('assets/LEGO_logo.png', 1)
img = cv2.resize(img, (400, 400))

# cv2.imshow("Image", img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

cap = cv2.VideoCapture("assets/human_detect.mp4")

while True:
    ret, frame = cap.read()
    height, width, _ = frame.shape

    scale_percent = 50
    new_width = int(width * scale_percent / 100)
    new_height = int(height * scale_percent / 100)
    dim = (new_width, new_height)
    resized = cv2.resize(frame, dim, interpolation = cv2.INTER_AREA)
    # img = cv2.line(frame, (0, 0), (width, height), (255, 0, 0), 10)
    # img = cv2.line(img, (0, height), (width, 0), (0, 255, 0), 5)
    # img = cv2.rectangle(img, (100, 100), (200, 200), (0, 0, 255), 2)

    # font = cv2.FONT_HERSHEY_COMPLEX
    # img = cv2.putText(img, 'human', (200, height -10), font, 0.7, (0, 0, 0), 1, cv2.LINE_AA)

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    cv2.imshow("frame",resized)

    if cv2.waitKey(1) == ord("q"):
        break
cap.release()
cv2.destroyAllWindows()
print("done")