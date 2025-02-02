import cv2
import numpy as np

def ginput(image, window_name="Select Points"):
    """
    Allows the user to select 4 points on an image interactively.

    Parameters:
        image (np.ndarray): The input image.
        window_name (str): Name of the window to display the image.

    Returns:
        np.ndarray: Array of 4 (x, y) points selected by the user, in np.float32 format.
    """
    points = []
    img = image.copy()  # Work on a copy to preserve the original image

    def mouse_handler(event, x, y, flags, param):
        nonlocal img
        if event == cv2.EVENT_LBUTTONDOWN and len(points) < 4:
            points.append((x, y))
            cv2.circle(img, (x, y), 5, (0, 255, 0), -1)  # Draw a circle at the selected point
            cv2.putText(img, str(len(points)), (x + 10, y), 
                       cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)  # Label the point
            cv2.imshow(window_name, img)  # Update the displayed image

    cv2.namedWindow(window_name)
    cv2.setMouseCallback(window_name, mouse_handler)

    print(f"Click 4 points on {window_name} (then press any key to continue)")
    while len(points) < 4:
        cv2.imshow(window_name, img)
        if cv2.waitKey(20) & 0xFF == 27:  # ESC key to force exit
            break

    cv2.destroyWindow(window_name)
    return np.array(points, dtype=np.float32)


def calculate_homography(image1_path, image2_path):
    """
    Computes the homography matrix using 4 corresponding points selected from two images.

    Parameters:
        image1_path (str): File path to the first input image.
        image2_path (str): File path to the second input image.

    Returns:
        H (np.ndarray): 3x3 homography matrix.
    """
    # Load images from file paths
    image1 = cv2.imread(image1_path)
    image2 = cv2.imread(image2_path)

    # Validate images
    if image1 is None:
        raise ValueError(f"Could not load image1 from path: {image1_path}")
    if image2 is None:
        raise ValueError(f"Could not load image2 from path: {image2_path}")

    # Select 4 points from the first image
    print("=== Select 4 points for the FIRST image ===")
    src_points = ginput(image1, "First Image")

    # Select 4 corresponding points from the second image
    print("=== Select 4 points for the SECOND image ===")
    dst_points = ginput(image2, "Second Image")

    # Compute the homography matrix
    H, _ = cv2.findHomography(src_points, dst_points)
    return H