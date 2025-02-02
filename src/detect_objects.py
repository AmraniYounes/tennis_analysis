def detect_objects(model, frame, conf=0.23):
    """Detect objects in the frame using the YOLO model."""
    results = model(frame, conf=conf)
    boxes = results[0].boxes.xyxy.cpu().numpy()
    class_ids = results[0].boxes.cls.cpu().numpy().astype(int)
    return boxes, class_ids