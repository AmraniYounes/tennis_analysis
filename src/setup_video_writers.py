import cv2

def setup_video_writers(cap, minimap_image):
    """Set up video writers for original and combined output."""
    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = int(cap.get(cv2.CAP_PROP_FPS))

    # Resize minimap to match video frame height (preserve aspect ratio)
    minimap_height = frame_height
    minimap_width = int((minimap_image.shape[1] / minimap_image.shape[0]) * minimap_height)
    minimap_image = cv2.resize(minimap_image, (minimap_width, minimap_height))

    # Combined video writer setup
    combined_width = frame_width + minimap_width
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter('../output/result.mp4', fourcc, fps, (combined_width, frame_height))


    return out, minimap_image, minimap_width, minimap_height