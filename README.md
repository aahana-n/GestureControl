Hand Gesture-Based Volume Control using OpenCV
This project uses hand gesture recognition to control system volume in real-time. By measuring the distance between your thumb and index finger using OpenCV and MediaPipe, the system dynamically adjusts your computer's audio volume.

#Features
- Real-time hand tracking using webcam
- Gesture recognition to measure the distance between thumb and index finger
- Maps hand distance to system volume levels
- Visual feedback with volume bar overlay on the video stream

#Requirements
- Python 3.x
- OpenCV
- MediaPipe

#How to Run
1. Clone the repository or download the project folder.
2. Open a terminal in the project directory.
3. Run the main script
4. Show your hand to the webcam. Move your thumb and index finger closer or farther apart to decrease or increase the volume. Ensure you have a video of your choice playing in the background to test the same.

#How It Works
1. The webcam captures your hand
2. MediaPipe detects hand landmarks
3. The distance between the thumb tip and index finger tip is calculated
4. That distance is mapped to a system volume range
5. The volume percentage is displayed on screen as visual feedback



Author: Aahana Nischal
