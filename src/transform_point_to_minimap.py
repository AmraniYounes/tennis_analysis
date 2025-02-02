import numpy as np

def transform_point_to_minimap(center, H, minimap_width, minimap_height):
    """Transform a point from the frame to the minimap using the homography matrix."""
    center_homogenized = np.array([center[0], center[1], 1.0], dtype=np.float32).reshape(3, 1)
    transformed_point = H @ center_homogenized

    if transformed_point[2] != 0:
        x = int(transformed_point[0] / transformed_point[2])
        y = int(transformed_point[1] / transformed_point[2])
        if 0 <= x < minimap_width and 0 <= y < minimap_height:
            return x, y
    return None