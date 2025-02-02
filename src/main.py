import cv2
import numpy as np
import os
from calculate_center import calculate_center
from calculate_homography import calculate_homography
from load_ressources import load_resources
from setup_video_writers import setup_video_writers
from detect_objects import detect_objects
from draw_on_minimap import draw_on_minimap
from draw_on_frame import draw_on_frame
from transform_point_to_minimap import transform_point_to_minimap


# Constants
COLORS = {"player": (0, 0, 255), "ball": (0, 255, 255)}
CLASS_IDS = {"player": 0, "ball": 1}
SHARPEN_KERNEL = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
FRAME_DELAY = 50
HOMOGRAPHY_FILE = "../assets/homography_matrix.npy"


# Load resources
model, cap, minimap_image = load_resources(
    "../runs/train/new_tennis_model/weights/best.pt",
    "../assets/tennis_vid.mp4",
    "../assets/court_frame.jpg",
    "../assets/tennis_minimap.jpg"
)

# Check if homography matrix file exists
if os.path.exists(HOMOGRAPHY_FILE):
    # Load the homography matrix from the file
    H = np.load(HOMOGRAPHY_FILE)
else:
    # Compute homography matrix and save it to file
    H = calculate_homography("../assets/court_frame.jpg", "../assets/tennis_minimap.jpg")
    np.save(HOMOGRAPHY_FILE, H)



# Setup video writers
out, minimap_image, minimap_width, minimap_height = setup_video_writers(cap, minimap_image)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Apply sharpening filter
    sharpened_frame = cv2.filter2D(frame, -1, SHARPEN_KERNEL)

    # Fresh minimap copy for each frame
    frame_minimap = minimap_image.copy()

    # Detect objects
    boxes, class_ids = detect_objects(model, sharpened_frame)

    for box, cls_id in zip(boxes, class_ids):
        center = calculate_center(box)
        # Draw directly on the main frame using original coordinates
        draw_on_frame(frame, (int(center[0]), int(center[1])), cls_id, COLORS, CLASS_IDS)

        transformed_point = transform_point_to_minimap(center, H, minimap_width, minimap_height)

        if transformed_point:
            x, y = transformed_point
            draw_on_minimap(frame_minimap, x, y, cls_id, COLORS, CLASS_IDS)

    # Create combined view
    combined_frame = cv2.hconcat([frame, frame_minimap])
    out.write(combined_frame)
    cv2.imshow("Tennis Analytics", combined_frame)

    if cv2.waitKey(FRAME_DELAY) == ord("q"):
        break

# Cleanup
cap.release()
out.release()
cv2.destroyAllWindows()