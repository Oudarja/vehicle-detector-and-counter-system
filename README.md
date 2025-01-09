This repository contains a Python-based vehicle detector and counter system that processes video footage to identify and count vehicles crossing a specified line. It leverages computer vision techniques with OpenCV to provide real-time object detection and tracking.

Features
Detects moving vehicles in video streams.
Counts vehicles as they cross a predefined line in the frame.
Uses bounding boxes to highlight detected vehicles.
Displays the total vehicle count in real-time.

Technologies Used
Programming Language: Python

Libraries and Frameworks
OpenCV: Core library for computer vision tasks such as object detection, background subtraction, morphological transformations, and contour analysis.

Techniques and Algorithms
1)Background Subtraction (MOG2): Used to segment moving vehicles from the static background.
2)Grayscale Conversion: Simplifies frames to single-channel images for efficient processing.
3)Gaussian Blur: Reduces noise in frames to improve object detection accuracy.
4)Morphological Operations: Enhances detected regions using dilation and closing operations to refine object boundaries.
5)Contours and Bounding Boxes: Identifies and tracks vehicles using object boundaries.
6)Vehicle Counting Logic: Tracks vehicle positions and increments the counter when they cross the specified line.

How It Works

->The system reads video input using OpenCV's VideoCapture.

->Frames are preprocessed with grayscale conversion and Gaussian blur to prepare for background subtraction.

->Moving objects are detected using the MOG2 background subtraction algorithm.

->Morphological operations are applied to improve the quality of detected regions.

->Contours are analyzed to identify individual vehicles, and bounding boxes are drawn around them.

->The centroid of each detected vehicle is calculated, and tracking logic determines when it crosses the counting line.

->A counter is incremented for each vehicle that successfully crosses the line.

->Results are displayed in real-time, showing the video with annotations and the total vehicle count.
