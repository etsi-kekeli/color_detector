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

        contours, _ = cv2.findContours(
            mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        for contour in contours:
            if cv2.contourArea(contour) > 50:
                rect = cv2.boundingRect(contour)
                cv2.rectangle(frame, rect, color=(255, 255, 0), thickness=2)

        cv2.imshow("Webcam", frame[:, ::-1, :])

    if cv2.waitKey(20) == ord('q'):
        loop = False

webcam.release()
cv2.destroyAllWindows()
