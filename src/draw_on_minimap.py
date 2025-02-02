import cv2

def draw_on_minimap(frame_minimap, x, y, cls_id, colors, class_ids):
    """Draw a circle on the minimap based on the class ID."""
    if cls_id == class_ids["player"]:
        color = colors["player"]
        radius = 5
    elif cls_id == class_ids["ball"]:
        color = colors["ball"]
        radius = 8
    else:
        return

    cv2.circle(frame_minimap, (x, y), radius, color, -1)