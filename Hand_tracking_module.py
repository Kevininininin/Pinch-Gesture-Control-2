import cv2
import mediapipe as mp
import time
import math

class handDetector():
    def __init__(self, mode=False, maxHands=2, detectionCon=0.5, trackCon=0.5):
        self.mode = mode
        self.maxHands = maxHands
        self.detectionCon = detectionCon
        self.trackCon = trackCon

        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(
            static_image_mode=self.mode,
            max_num_hands=self.maxHands,
            min_detection_confidence=self.detectionCon,
            min_tracking_confidence=self.trackCon)
        # Draw lines in between each hand landmarks
        self.mpDraw = mp.solutions.drawing_utils

    def findHands(self, img, draw=True):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(imgRGB)
        # print(results.multi_hand_landmarks)

        if self.results.multi_hand_landmarks:
            for handLms in self.results.multi_hand_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(img, handLms, self.mpHands.HAND_CONNECTIONS)
        return img

    # handNo specifies which hand are we looking at
    def findPosition(self, img, distance_threshold=True, draw=True, click_green=True):
        allLmList = []
        if self.results.multi_hand_landmarks:
            for handLms in self.results.multi_hand_landmarks:
                lmList = []
                # myHand = self.results.multi_hand_landmarks[handNo]

                # iterate through the number(identification aka id) of each landmark aka lm
                for id, lm in enumerate(handLms.landmark):
                    # id - number of the landmark
                    # cx - x coordinate (in pixel count)
                    # cy - y coordinate (in pixel count)
                    h, w, c = img.shape
                    cx, cy = int(lm.x * w), int(lm.y * h)
                    # print(id, cx, cy)
                    lmList.append([id, cx, cy])
                    # Drawing a white circle on the tip of thumb (4) and index finger (8)
                    if draw:
                        if click_green:
                            if id == 4 or id == 8:
                                # Draw green if close enough to pinch, otherwise white
                                color = (0, 255, 0) if distance_threshold else (255, 255, 255)
                                cv2.circle(img, (cx, cy), 10, color, cv2.FILLED)

                allLmList.append(lmList)

        return allLmList

    def pinch_distance(self, allLmList, handNo=0):
        # No hands detected or handNo out of range
        if not allLmList or len(allLmList) <= handNo:
            return "300"

        # Ensure the hand has enough landmarks (at least 9 landmarks)
        if len(allLmList[handNo]) <= 8:
            return "300"  # Not enough landmarks
        # White circles are on the tip of thumb (4) and index finger (8)
        # Landmark format [[hand1],[hand2]], in hand1:[LmCount, x-pixel, y-pixel]

        # Distance of hand1
        x_diff = allLmList[handNo][4][1] - allLmList[handNo][8][1]
        y_diff = allLmList[handNo][4][2] - allLmList[handNo][8][2]

        distance = math.sqrt(x_diff**2 + y_diff**2)

        return distance

    def get_lm_location(self, allLmList, handNo=0, lm_num=0, axis="x"):
        # No hands detected or handNo out of range
        if not allLmList or len(allLmList) <= handNo:
            return None
        # Ensure the hand has enough landmarks (at least 9 landmarks)
        if len(allLmList[handNo]) <= 8:
            return None

        if axis == "x":
            return allLmList[handNo][lm_num][1]
        elif axis == "y":
            return allLmList[handNo][lm_num][2]


def main():
    previous_time = 0
    # current_time = 0
    cap = cv2.VideoCapture(0)
    detector = handDetector()
    while True:
        success, img = cap.read()
        img = detector.findHands(img)
        # findPosition(self, img, handNo=0, draw=True)
        # allLmList[0] is hand 1, allLmList[1] is hand 2
        allLmList = detector.findPosition(img, draw=False)

        # print(allLmList)

        current_time = time.time()
        fps = 1 / (current_time - previous_time)
        previous_time = current_time

        cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 3, (255, 255, 255), 3)

        cv2.imshow('Image', img)
        cv2.waitKey(1)




if __name__ == '__main__':
    main()