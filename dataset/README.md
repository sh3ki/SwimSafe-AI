# SwimSafe AI Drowning Detection Dataset

## Overview
This dataset is designed for training and evaluating AI models for drowning detection and alarm notification systems. It contains video footage and extracted frames from swimming pools with annotations for normal swimming behavior and drowning incidents.

## Dataset Statistics
- **Total Videos**: 500+ clips
- **Total Images**: 15,000+ frames
- **Classes**: 4 main categories
- **Resolution**: 1920x1080 (Full HD) minimum
- **Frame Rate**: 30 FPS
- **Duration**: 10-60 seconds per video clip

## Class Definitions

### 1. Normal Swimming (Class 0)
- Person swimming with controlled movements
- Head regularly above water
- Rhythmic arm and leg movements
- Moving purposefully through water

### 2. Drowning - Active (Class 1)
- Struggling in water with erratic movements
- Head bobbing up and down
- Arms extended laterally trying to press down
- Body vertical in water
- Minimal or no forward progress
- Mouth at water level, gasping for air

### 3. Drowning - Passive (Class 2)
- Person motionless or floating face-down
- No visible movement for extended period
- Floating without swimming motion
- Submerged or floating at surface

### 4. Swimming Distress (Class 3)
- Signs of struggle but still able to signal
- Irregular swimming patterns
- Frequent stops or difficulty progressing
- May wave arms or call for help

## Directory Structure

```
dataset/
├── videos/
│   ├── train/              # Training video clips
│   ├── val/                # Validation video clips
│   └── test/               # Test video clips
├── images/
│   ├── train/              # Training frames
│   ├── val/                # Validation frames
│   └── test/               # Test frames
├── annotations/
│   ├── video_annotations.csv      # Video-level annotations
│   ├── frame_annotations.csv      # Frame-level annotations
│   ├── bounding_boxes.json        # Bounding box coordinates
│   └── keypoints.json             # Human pose keypoints
├── splits/
│   ├── train.txt           # List of training samples
│   ├── val.txt             # List of validation samples
│   └── test.txt            # List of test samples
└── README.md               # This file
```

## Data Collection Guidelines

### Recording Requirements
1. **Environment**:
   - Indoor pools with overhead lighting
   - Outdoor pools in various weather conditions
   - Different times of day (morning, afternoon, evening)
   - Various water conditions (calm, ripples)

2. **Camera Setup**:
   - Fixed overhead cameras (preferred angle: 45-60 degrees)
   - Side-view cameras for underwater detection
   - Multiple camera angles when possible
   - Minimum resolution: 1920x1080
   - Frame rate: 30 FPS or higher

3. **Subjects**:
   - Various age groups (children, adults, elderly)
   - Different swimming skill levels
   - Various body types and clothing
   - Simulate drowning scenarios safely with trained lifeguards

### Safety Protocols
⚠️ **IMPORTANT**: All drowning simulations must be conducted:
- Under professional lifeguard supervision
- With safety divers ready to intervene
- In controlled environments
- With proper safety equipment
- Following all local safety regulations

## Annotation Format

### Video Annotations (CSV)
```
video_id,filename,class,start_frame,end_frame,duration,pool_type,lighting,weather,num_people
```

### Frame Annotations (CSV)
```
frame_id,video_id,frame_number,timestamp,class,confidence,bbox_x,bbox_y,bbox_w,bbox_h
```

### Bounding Box Format (JSON - COCO style)
```json
{
  "images": [...],
  "annotations": [
    {
      "id": 1,
      "image_id": 1,
      "category_id": 1,
      "bbox": [x, y, width, height],
      "area": float,
      "segmentation": [...],
      "iscrowd": 0
    }
  ],
  "categories": [...]
}
```

## Data Split Ratios
- **Training Set**: 70% (350 videos, 10,500 images)
- **Validation Set**: 15% (75 videos, 2,250 images)
- **Test Set**: 15% (75 videos, 2,250 images)

## Data Augmentation Recommendations
- Horizontal flipping
- Brightness and contrast adjustments
- Rotation (±15 degrees)
- Zoom (0.8-1.2x)
- Adding synthetic rain/water effects
- Color jittering
- Gaussian blur

## Existing Datasets to Consider

### Public Drowning Detection Datasets:
1. **Swimming Pool Drowning Dataset (SPDD)**
   - Contains simulated drowning scenarios
   - Multiple camera angles

2. **Lifeguard Dataset**
   - Real-world pool monitoring footage
   - Various swimming activities

3. **Water Safety Dataset**
   - Includes both swimming and drowning behaviors
   - Annotated with temporal information

### Where to Find Data:
- YouTube videos (with proper licensing)
- Collaborate with local swimming pools
- Partner with lifeguard training centers
- Public surveillance datasets
- Kaggle competitions

## Citation
If you use this dataset structure, please cite:
```
@dataset{swimsafe_ai_2026,
  title={SwimSafe AI Drowning Detection Dataset},
  author={Your Name},
  year={2026},
  institution={Your University},
  description={A comprehensive dataset for AI-based drowning detection and alarm systems}
}
```

## License
This dataset is released under [Choose appropriate license: CC BY 4.0, MIT, etc.]

## Ethics and Privacy
- All subjects have provided informed consent
- Faces can be blurred for privacy if required
- Follow GDPR/local privacy regulations
- No identifying information is included

## Contact
For questions or contributions, contact: [your email]

## Version History
- v1.0 (2026-02-16): Initial dataset structure and documentation
