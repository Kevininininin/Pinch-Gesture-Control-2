import cv2
import mediapipe as mp
import time

cap = cv2.VideoCapture(0)

mpHands = mp.solutions.hands
hands = mpHands.Hands()
# Draw lines in between each hand landmarks
mpDraw = mp.solutions.drawing_utils

Previous_time = 0
Current_time = 0

while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    # print(results.multi_hand_landmarks)

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            # iterate through the number(identification aka id) of each landmark aka lm
            for id, lm in enumerate(handLms.landmark):
                # id - number of the landmark
                # cx - x coordinate (in pixel count)
                # cy - y coordinate (in pixel count)
                h, w, c = img.shape
                cx, cy = int(lm.x*w), int(lm.y*h)
                print(id, cx, cy)
                # Drawing a white circle on the tip of thumb (4) and index finger (8)
                if id == 4 or id == 8:
                    cv2.circle(img, (cx, cy),20,(255,255,255),cv2.FILLED)


            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)

    current_time = time.time()
    fps = 1 / (current_time - Previous_time)
    Previous_time = current_time

    cv2.putText(img,str(int(fps)), (10,70), cv2.FONT_HERSHEY_SIMPLEX, 3, (255,255,255),3)

    cv2.imshow('Image', img)
    cv2.waitKey(1)