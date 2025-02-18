import cv2
from utils import get_limits

webcam = cv2.VideoCapture(0)
target_color = (0, 255, 255)  # Jaune dans l'espace BGR
loop = True

while loop:
    ret, frame = webcam.read()

    if ret:
        hsvImage = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        lower, upper = get_limits(target_color)
        mask = cv2.inRange(hsvImage, lower, upper)

        cv2.imshow("Webcam", mask)

    if cv2.waitKey(30) == ord('q'):
        loop = False

webcam.release()
cv2.destroyAllWindows()
