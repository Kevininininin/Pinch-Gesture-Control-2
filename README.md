# Pinch Gesture Cursor Control

This project allows users to control their computer mouse using **hand gestures** captured through the webcam.  
By detecting the pinch motion between the thumb and index finger, the system can move the cursor and simulate drag-and-drop actions.

## Features

- **Hand Detection**: Tracks your hand and fingertips using MediaPipe and OpenCV.
- **Cursor Control**: Moves the mouse based on your finger position.
- **Pinch Gesture Detection**: Left-click and drag using a simple pinch gesture.
- **Smooth Cursor Movement**: Applies smoothening to avoid jittery movement.
- **Boundary Frame**: Displays an interactive area for gesture control.

## Technologies Used

- Python 3.12
- OpenCV
- MediaPipe
- PyAutoGUI
- NumPy

