# Pinch Gesture Cursor Control

While there are many video tutorials and resources on implementing Google MediaPipe's hand landmark detection, most focus on achieving basic results. In this repository, I explored extending these capabilities by implementing the **pinch-to-select** control logic, similar to what’s seen on the Apple Vision Pro, on a laptop (Without eye-tracking).

This project enables users to control their computer mouse using **hand gestures** captured via the webcam. By detecting the pinch motion between the thumb and index finger, the system can move the cursor and simulate drag-and-drop actions.

The program uses **PyAutoGUI** for cursor control. While it successfully supports basic cursor movement and drag-and-drop functionality, it cannot visually display the drag process in real-time. The computer will only respond when the user releases the pinch gesture.

A quick demo of this program can be found here:  [LinkedIn Demo Link](https://www.linkedin.com/posts/jinghan-wu-446a0b233_why-i-think-apples-decision-to-complement-activity-7209560750422376449-22g_?utm_source=social_share_send&utm_medium=member_desktop_web&rcm=ACoAADpZNLYBelKKeog8xIczccE5stEKRHPKYjY)

## Features

- **Hand Detection**: Tracks hands and fingertips using MediaPipe and OpenCV.
- **Cursor Control**: Moves the mouse based on finger position.
- **Pinch Gesture Detection**: Simulates left-click and drag using a simple pinch.
- **Smooth Cursor Movement**: Applies smoothing to minimize jittery motion.
- **Boundary Frame**: Displays an interactive frame defining the gesture control area.

## Technologies Used

- Python 3.12
- OpenCV
- MediaPipe
- PyAutoGUI
- NumPy

## How to Use

### 1. Install Required Packages
Make sure you have Python 3.12 installed. Then install the required libraries:
```bash
pip install opencv-python mediapipe pyautogui numpy
```

### 2. Run the Program
Clone this repository to your local machine. Navigate into the project directory and run the main Python file:
```bash
python Pinch_Control.py
```

### 3. Control Your Cursor with Hand Gestures
- Position your hand inside the webcam frame.
- Move your hand to control the cursor based on your finger position.
- Pinch your thumb and index finger together to perform a left-click and drag.
- Release the pinch to drop.
> **Tip:** For best results, keep your hand within the displayed boundary frame and ensure good lighting conditions for more accurate detection.
