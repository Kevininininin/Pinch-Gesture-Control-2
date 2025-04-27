# Comment test

import cv2
# import mediapipe as mp
import time
import Hand_tracking_module as htm
import pyautogui as pag
import numpy as np
from Mouse_Control import MouseControl


pag.FAILSAFE = True


def pinch_detection(detector, allLmList):
    # Pring pinch distance of hand_0
    hand_0_distance = detector.pinch_distance(allLmList, 0)
    hand_0_distance = round(float(hand_0_distance), 3)
    if hand_0_distance <= 55:
        return True
    elif hand_0_distance > 55:
        return False
    else:
        return False

def main():
    previous_time = 0
    cap = cv2.VideoCapture(0)

    detector = htm.handDetector()
    distance_threshold = False
    smoothening = 4
    previous_location_x, previous_location_y = 0, 0
    current_location_x, current_location_y = 0, 0

    mouseControl = MouseControl()
    dragging = False

    while True:
        success, img = cap.read()

        # Always draw the detection area frame FIRST
        cv2.rectangle(img, (200, 100), (1920 - 500, 1080 - 200), (255, 255, 255), 3)

        img = detector.findHands(img, draw=True)

        allLmList = detector.findPosition(img, distance_threshold, draw=True, click_green=True)

        if allLmList:
            distance_threshold = pinch_detection(detector, allLmList)

            index_x_coordinate = detector.get_lm_location(allLmList, handNo=0, lm_num=4, axis="x")
            index_y_coordinate = detector.get_lm_location(allLmList, handNo=0, lm_num=4, axis="y")

            if index_x_coordinate is not None and index_y_coordinate is not None:
                x_converted = np.interp(index_x_coordinate, (200, 1420), (0, 1512))
                y_converted = np.interp(index_y_coordinate, (100, 880), (0, 982))

                current_location_x = previous_location_x + (x_converted - previous_location_x) / smoothening
                current_location_y = previous_location_y + (y_converted - previous_location_y) / smoothening

                mouseControl.move_mouse_to(1512 - current_location_x, current_location_y)

                if distance_threshold and not dragging:
                    pag.mouseDown(button='left')
                    dragging = True
                elif not distance_threshold and dragging:
                    pag.mouseUp(button='left')
                    dragging = False

                previous_location_x = current_location_x
                previous_location_y = current_location_y

        current_time = time.time()
        fps = 1 / (current_time - previous_time)
        previous_time = current_time

        cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 3, (255, 255, 255), 3)

        cv2.imshow('Image', img)
        cv2.waitKey(20)

    cap.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()