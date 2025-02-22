#!/home/yao/anaconda3/envs/Calibration/bin/python

import cv2
import argparse
import sys
from utils import get_limits, get_color_representation

parser = argparse.ArgumentParser()
parser.add_argument("--color", default='yellow')

args = parser.parse_args()
target_color = get_color_representation(args.color)
print(target_color)

if target_color is None:
    print("Unsupported color specified. Update the supported colors list.")
    sys.exit(1)

webcam = cv2.VideoCapture(0)
loop = True

while loop:
    ret, frame = webcam.read()

    if ret:
        hsvImage = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        lower, upper = get_limits(target_color, tol=20)
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
