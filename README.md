# Project Title
Vehicle Counter using OpenCV

## Project Overview
The Vehicle Counter project is designed to count vehicles in a video file using OpenCV. The project utilizes a background subtraction algorithm to detect moving objects (vehicles) and counts them as they cross a predefined line.

## Features
* Vehicle detection using background subtraction algorithm
* Real-time vehicle counting
* Line crossing detection
* Display vehicle count on video feed

## File Descriptions
### Vehicle.py
The `Vehicle.py` script is the core of the project. It defines a `VehicleCounter` class that encapsulates the vehicle counting logic. The script uses the MOG2 background subtraction algorithm to detect moving objects in the video and counts vehicles as they cross a predefined line.

## Getting Started
### Prerequisites
* Python
* OpenCV library

### Installation
To get started with the project, follow these steps:

1. Create a new virtual environment:
```bash
python -m venv venv
```
2. Activate the virtual environment:
```bash
# On Windows
venv\Scripts\activate

# On Linux/Mac
source venv/bin/activate
```
3. Install the required libraries:
```bash
pip install opencv-python
```
4. Clone the repository:
```bash
git clone https://github.com/your-username/Vehicle-Counter.git
```
5. Navigate to the project directory:
```bash
cd Vehicle-Counter
```

### Running the Project
To run the project, simply execute the `Vehicle.py` script:
```bash
python Vehicle.py
```
This will display the video feed with the vehicle count. The count will be printed to the console and displayed on the video feed.

## Usage
To use the script, simply run `Vehicle.py` with a video file (e.g., "video.mp4") and it will display the video feed with the vehicle count.

Example usage:

```bash
python Vehicle.py
```
