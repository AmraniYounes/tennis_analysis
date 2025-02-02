from ultralytics import YOLO
import cv2

def load_resources(model_path, video_path, court_path, minimap_path):
    """Load model, video, and images."""
    model = YOLO(model_path)
    cap = cv2.VideoCapture(video_path)
    minimap_image = cv2.imread(minimap_path)
    return model, cap, minimap_image