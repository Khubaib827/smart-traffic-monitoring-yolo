from ultralytics import YOLO
import os

# Load YOLO11 model
model = YOLO("yolo11n.pt")

# Input image
image_path = "test_images/traffic.jpg"

# Check image exists
if not os.path.exists(image_path):
    print("ERROR: traffic.jpg not found!")
    print("Put traffic.jpg inside the test_images folder.")
    exit()

# Detect objects
results = model.predict(
    source=image_path,
    conf=0.4,
    save=True
)

print("Traffic detection completed!")

# Print detected objects
for result in results:
    if result.boxes is not None:
        for box in result.boxes:
            class_id = int(box.cls[0])
            confidence = float(box.conf[0])
            name = model.names[class_id]

            print(f"{name}: {confidence:.2f}")