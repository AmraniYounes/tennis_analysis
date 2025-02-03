# Tennis Court Minimap Projection
Real-time player and ball tracking projection on tennis court minimap using YOLOv8 detection and perspective transformation.

## Team members
    - Chakrabane Houda
    - Bouamar Hajar
    - Amrani Younes
    - Guendaoui Adnane
    - Taiar Abdellah
    - Manchoud Reda

## Features
- 🎾 Custom YOLOv8 model for player and ball detection
- 🗺️ Homography matrix transformation for court projection
- 📍 Bounding box center point mapping


## Requirement

**Dimension Matching**  
For accurate perspective projection using homography matrix transformation:  

✅ **Input video frame** and **minimap image** heights must be equal  


## Installation

1. Clone the repository:
```yaml
git clone https://github.com/AmraniYounes/tennis_analysis.git
cd tennis_analysis
```

### Key Notes:
- Ensure you have Python 3.8 or higher installed.
```bash
pip install -r requirements.txt
```