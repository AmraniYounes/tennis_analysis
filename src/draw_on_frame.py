import cv2

def draw_on_frame(frame, center, cls_id, colors, class_ids):
    """Draw a circle on the video frame based on the class ID."""
    if cls_id == class_ids["player"]:
        color = colors["player"]
        radius = 5
    elif cls_id == class_ids["ball"]:
        color = colors["ball"]
        radius = 8
    else:
        return

    cv2.circle(frame, (int(center[0]), int(center[1])), radius, color, -1)