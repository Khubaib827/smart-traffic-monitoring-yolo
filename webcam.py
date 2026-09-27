from ultralytics import YOLO
import cv2

# Load YOLO model
model = YOLO("yolo11n.pt")

# Start webcam
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("ERROR: Cannot open webcam")
    exit()

print("Webcam started!")
print("Press Q to stop.")

while True:
    ret, frame = cap.read()

    if not ret:
        print("ERROR: Cannot read webcam")
        break

    # Detect objects
    results = model(frame, verbose=False)

    # Draw detection boxes
    frame = results[0].plot()

    # Count vehicles
    vehicle_count = 0

    if results[0].boxes is not None:
        for box in results[0].boxes:
            class_id = int(box.cls[0])

            # COCO: car=2, motorcycle=3, bus=5, truck=7
            if class_id in [2, 3, 5, 7]:
                vehicle_count += 1

    # Display vehicle count
    cv2.putText(
        frame,
        f"Vehicles: {vehicle_count}",
        (20, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 255, 0),
        2
    )

    cv2.imshow("Smart Traffic Monitoring", frame)

    # Press Q to exit
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()