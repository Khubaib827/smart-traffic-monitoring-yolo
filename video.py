from ultralytics import YOLO
import cv2
import os
import glob

# ==============================
# 1. Load YOLO model
# ==============================
model = YOLO("yolo11n.pt")

# ==============================
# 2. Find MP4 video
# ==============================
videos = glob.glob("videos/*.mp4")

if len(videos) == 0:
    print("ERROR: No MP4 video found!")
    print("Put an MP4 video inside the videos folder.")
    exit()

video_path = videos[0]

print("Using video:", video_path)

# ==============================
# 3. Open video
# ==============================
cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print("ERROR: Could not open video.")
    exit()

# ==============================
# 4. Get video properties
# ==============================
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS)

if fps <= 0:
    fps = 30

# ==============================
# 5. Create output folder
# ==============================
os.makedirs("output", exist_ok=True)

# ==============================
# 6. Output video
# ==============================
output_path = "output/traffic_status.mp4"

fourcc = cv2.VideoWriter_fourcc(*"mp4v")

out = cv2.VideoWriter(
    output_path,
    fourcc,
    fps,
    (width, height)
)

if not out.isOpened():
    print("ERROR: Could not create output video.")
    cap.release()
    exit()

print("Video started!")
print("Output will be saved as:", output_path)
print("Press Q to stop.")

# ==============================
# 7. Process video
# ==============================
while True:

    ret, frame = cap.read()

    if not ret:
        print("Video finished.")
        break

    # YOLO detection
    results = model(frame, verbose=False)

    # Draw bounding boxes and labels
    frame = results[0].plot()

    # ==============================
    # 8. Count vehicles
    # ==============================
    vehicle_count = 0

    if results[0].boxes is not None:

        for box in results[0].boxes:

            class_id = int(box.cls[0])

            # COCO classes:
            # 2 = car
            # 3 = motorcycle
            # 5 = bus
            # 7 = truck

            if class_id in [2, 3, 5, 7]:
                vehicle_count += 1

    # ==============================
    # 9. Traffic status
    # ==============================
    if vehicle_count <= 3:
        traffic_status = "LOW TRAFFIC"

    elif vehicle_count <= 6:
        traffic_status = "MEDIUM TRAFFIC"

    else:
        traffic_status = "HIGH TRAFFIC"

    # ==============================
    # 10. Display vehicle count
    # ==============================
    cv2.putText(
        frame,
        f"Vehicles: {vehicle_count}",
        (20, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 255, 0),
        2
    )

    # ==============================
    # 11. Display traffic status
    # ==============================
    cv2.putText(
        frame,
        f"Traffic Status: {traffic_status}",
        (20, 80),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.9,
        (0, 255, 255),
        2
    )

    # ==============================
    # 12. Save processed frame
    # ==============================
    out.write(frame)

    # ==============================
    # 13. Show video
    # ==============================
    cv2.imshow("Smart Traffic Monitoring", frame)

    # Press Q to stop
    if cv2.waitKey(1) & 0xFF == ord("q"):
        print("Stopped by user.")
        break

# ==============================
# 14. Release resources
# ==============================
cap.release()
out.release()
cv2.destroyAllWindows()

print()
print("======================================")
print("TRAFFIC MONITORING COMPLETED!")
print("======================================")
print("Output saved at:")
print(output_path)
print("======================================")