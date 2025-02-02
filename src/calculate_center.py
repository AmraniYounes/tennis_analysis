def calculate_center(box):
    """
    Calculate the lower center of a bounding box.

    Parameters:
    box (tuple): A tuple containing the coordinates of the bounding box in the format (x_min, y_min, x_max, y_max).

    Returns:
    tuple: The (x, y) coordinates of the center of the bounding box.
    """
    x_min, y_min, x_max, y_max = box
    center_x = (x_min + x_max) / 2
    return (center_x, y_max)