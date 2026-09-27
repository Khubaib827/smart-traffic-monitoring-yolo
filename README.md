# Smart Traffic Monitoring using YOLO

## Project Overview

Smart Traffic Monitoring using YOLO is a computer vision project that automatically detects vehicles from traffic videos using the YOLO11 object detection model.

The system detects cars, motorcycles, buses, and trucks. It counts the detected vehicles and classifies the traffic condition as Low, Medium, or High Traffic.

The processed video contains bounding boxes, vehicle labels, vehicle count, and traffic status.

## Objectives

- Detect vehicles automatically from traffic videos.
- Identify cars, motorcycles, buses, and trucks.
- Count the detected vehicles.
- Display bounding boxes around detected objects.
- Classify traffic conditions.
- Save the processed traffic video.
- Support image, video, and webcam detection.

## Features

- Vehicle detection using YOLO11
- Car detection
- Motorcycle detection
- Bus detection
- Truck detection
- Vehicle counting
- Traffic status classification
- Bounding box visualization
- Traffic video processing
- Image detection
- Webcam detection
- Processed output video generation

## Technologies Used

- Python
- YOLO11
- Ultralytics
- OpenCV
- Computer Vision

## Project Structure

Smart-Traffic-Monitoring-using-YOLO/
│
├── video.py
├── webcam.py
├── predict.py
├── train.py
├── README.md
├── .gitignore
│
├── test_images/
│   └── traffic.jpg
│
└── test_result.jpg

## Installation

Install the required Python packages:

pip install ultralytics opencv-python

## YOLO Model

This project uses the YOLO11n pretrained model.

Download the yolo11n.pt model and place it in the main project folder.

## Running Video Detection

Place an MP4 traffic video inside the videos folder:

videos/
└── traffic.mp4

Then run:

python video.py

The system will detect vehicles and display the vehicle count and traffic status.

Example:

Vehicles: 4
Traffic Status: MEDIUM TRAFFIC

## Traffic Classification

| Vehicle Count | Traffic Status |
|---:|---|
| 0–3 | Low Traffic |
| 4–6 | Medium Traffic |
| 7+ | High Traffic |

## Vehicle Classes

| Class ID | Vehicle |
|---:|---|
| 2 | Car |
| 3 | Motorcycle |
| 5 | Bus |
| 7 | Truck |

## Webcam Detection

To run the system using a laptop webcam:

python webcam.py

The webcam detects objects in real time.

Press Q to stop the webcam.

## Image Detection

The project also supports image-based object detection.

Run:

python predict.py

## Output

The processed traffic video contains:

- Vehicle bounding boxes
- Vehicle labels
- Vehicle count
- Traffic status

The final processed video is saved as:

output/traffic_status.mp4

## Results

The system successfully detects vehicles from traffic videos and displays:

- Detected vehicle objects
- Bounding boxes
- Vehicle count
- Traffic condition

The project was tested using traffic video, image detection, and webcam detection.

## Applications

This system can be used for:

- Smart city traffic monitoring
- Traffic congestion analysis
- Road monitoring
- CCTV-based vehicle detection
- Intelligent transportation systems
- Traffic management

## Advantages

- Automatic vehicle detection
- Real-time object detection capability
- Vehicle counting
- Simple and easy to use
- Supports video and webcam input
- Saves processed output
- Can be extended for smart-city applications

## Limitations

- Detection accuracy depends on video quality.
- Low-light or heavily crowded scenes may affect detection.
- The current traffic classification is based only on vehicle count.
- The system does not currently estimate vehicle speed.

## Future Scope

Future improvements can include:

- Real-time CCTV traffic monitoring
- Vehicle speed estimation
- Automatic traffic signal control
- Number plate recognition
- Accident detection
- Emergency vehicle detection
- Traffic congestion alerts
- Web-based traffic monitoring dashboard
- Smart-city traffic management integration

## Conclusion

Smart Traffic Monitoring using YOLO demonstrates how computer vision and YOLO11 can be used to automatically detect vehicles, count traffic, and classify traffic conditions from video data.

The project provides a foundation for developing more advanced intelligent traffic monitoring and smart transportation systems.

## Author

Sana Rajini
