from ultralytics import YOLO

def main():
    # Load YOLOv8 model
    model = YOLO('yolov8s.pt')  

    # Train the model
    model.train(
        data='../Tennis Match.v3i.yolov8/data.yaml',
        epochs=100,              
        imgsz=640,              
        batch=16,                
        optimizer='SGD',        
        lr0=0.01,               
        lrf=0.01,               
        momentum=0.937,         
        weight_decay=0.0005,    
        patience=10,            # Early stopping
        amp=True,               
        project='runs/train',   # Folder where results are saved
        name='new_tennis_model',    # Name of the run
        workers=16,              
        device=0,              
    )


if __name__ == '__main__':
    main()