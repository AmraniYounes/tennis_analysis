# Tennis Court Minimap Projection System

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![YOLOv8](https://img.shields.io/badge/YOLO-v8-red)
![OpenCV](https://img.shields.io/badge/OpenCV-4.9.0-green)

Real-time player and ball tracking projection on tennis court minimap using YOLOv8 detection and perspective transformation.

## Features
- 🎾 Custom YOLOv8 model for player and ball detection
- 🗺️ Homography matrix transformation for court projection
- 📍 Bounding box center point mapping
- 🎥 Video processing pipeline for match analysis

## Requirement

**Dimension Matching**  
For accurate perspective projection using homography matrix transformation:  

✅ **Input video frame** and **minimap image** must satisfy:  

Frame Height (video) == Pixel Height (minimap)

## Installation
```yaml
1. Clone the repository:
```bash
git clone https://github.com/AmraniYounes/tennis_analysis.git
cd tennis_analysis

