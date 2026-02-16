# Existing Drowning Detection Datasets - Resources and References

## Overview
This document provides information on existing datasets, research papers, and resources that can be used or referenced for drowning detection research.

---

## 1. Public Datasets

### 1.1 Swimming Pool Drowning Dataset (Hypothetical/Simulated)
**Status**: Research datasets with simulated scenarios

**Description**: Various research groups have created drowning simulation datasets
- Focus on controlled pool environments
- Professional actors simulating drowning behavior
- Multiple camera angles

**Where to Find**:
- Academic research papers
- University research group websites
- Contact authors directly

---

### 1.2 Video Surveillance Datasets (Related)

#### UCF Crime Dataset
- **URL**: https://www.crcv.ucf.edu/projects/real-world/
- **Contains**: 1900 long untrimmed surveillance videos
- **Relevance**: Anomaly detection in videos (similar to drowning detection)
- **Classes**: 13 anomalous events
- **Note**: No specific drowning scenes, but useful for transfer learning

#### VIRAT Video Dataset
- **URL**: http://viratdata.org/
- **Contains**: Realistic outdoor surveillance videos
- **Relevance**: Human activity recognition in surveillance
- **Use Case**: Transfer learning for person detection

---

### 1.3 Human Activity Recognition Datasets

#### Kinetics-700
- **URL**: https://deepmind.com/research/open-source/kinetics
- **Contains**: 700 human action classes
- **Relevance**: Includes swimming-related activities
- **Classes**: Swimming, diving, water sports
- **Videos**: ~650,000 video clips
- **Use Case**: Pre-training models for swimming behavior understanding

#### HMDB51 (Human Motion Database)
- **URL**: http://serre-lab.clps.brown.edu/resource/hmdb-a-large-human-motion-database/
- **Contains**: 51 action categories
- **Relevance**: Includes swimming activities
- **Videos**: ~7,000 clips
- **Use Case**: Action recognition baseline

#### UCF101
- **URL**: https://www.crcv.ucf.edu/data/UCF101.php
- **Contains**: 101 action categories
- **Relevance**: Includes swimming and diving
- **Videos**: 13,320 videos
- **Use Case**: Pre-training and transfer learning

---

### 1.4 Pose Estimation Datasets

#### COCO (Common Objects in Context)
- **URL**: https://cocodataset.org/
- **Contains**: Person keypoints annotations
- **Relevance**: 17 body keypoints for pose estimation
- **Use Case**: Train pose estimation models for drowning detection

#### MPII Human Pose
- **URL**: http://human-pose.mpi-inf.mpg.de/
- **Contains**: ~25,000 images with annotated body joints
- **Use Case**: Human pose estimation in various positions

---

## 2. How to Acquire Drowning-Specific Data

### 2.1 Public Sources

#### YouTube
- **Search Terms**:
  - "Drowning simulation"
  - "Lifeguard training drowning"
  - "Swimming pool safety training"
  - "Drowning rescue training"
- **Considerations**:
  - Check licensing and usage rights
  - Contact creators for permission
  - Use youtube-dl or similar tools (respecting copyright)

#### Vimeo
- Higher quality professional training videos
- Lifeguard certification programs
- Water safety organizations

#### Stock Footage Websites
- **Shutterstock**: Commercial underwater footage
- **Getty Images**: Professional swimming footage
- **Pond5**: Stock video marketplace
- **Note**: Requires licensing fees

---

### 2.2 Partnerships and Collaborations

#### Swimming Pool Facilities
- **Local Community Pools**
  - Approach management with research proposal
  - Offer to share results for their safety
  - Sign data usage agreements

- **University Pools**
  - Easier access for student researchers
  - May have existing IRB protocols
  - Can coordinate with sports departments

#### Lifeguard Training Organizations
- **American Red Cross**
- **YMCA**
- **National Swimming Pool Foundation**
- **Ellis & Associates**

**Benefits**:
- Access to training scenarios
- Professional lifeguards for supervision
- Controlled simulation environments
- Existing safety protocols

#### Water Parks and Recreation Centers
- Larger organizations may have surveillance footage
- Can provide diverse scenarios
- Multiple camera angles already installed

---

### 2.3 Research Collaborations

#### Academic Institutions
Search for researchers working on:
- Computer vision for safety
- Aquatic sports analysis
- Emergency response systems
- Human activity recognition

**Databases to Search**:
- Google Scholar: "drowning detection dataset"
- IEEE Xplore: Drowning detection papers
- ACM Digital Library
- arXiv.org

#### Contact Researchers
- Email authors of drowning detection papers
- Request dataset access
- Propose collaboration
- Offer to contribute annotations

---

## 3. Relevant Research Papers

### Key Papers with Datasets/Methods

1. **"Deep Learning for Drowning Detection in Swimming Pools"**
   - Various authors have published on this topic
   - Check recent conferences: CVPR, ICCV, ECCV
   - Look for papers from 2018-2025

2. **"Automated Drowning Detection Using Computer Vision"**
   - Focus on real-time detection methods
   - Often includes methodology for data collection

3. **"Human Pose Estimation for Swimming Activity Recognition"**
   - Pose-based drowning detection
   - Relevant for keypoint annotation

### Where to Find Papers
- **Google Scholar**: https://scholar.google.com/
- **IEEE Xplore**: https://ieeexplore.ieee.org/
- **arXiv**: https://arxiv.org/ (search "drowning detection")
- **ResearchGate**: https://www.researchgate.net/

---

## 4. Creating Your Own Dataset

### 4.1 Simulation Approach

#### Safe Simulation Protocol
1. **Professional Actors**
   - Hire trained lifeguards/swimmers
   - Teach drowning behavior patterns
   - Ensure safety protocols

2. **Controlled Environment**
   - Use shallow pools initially
   - Progress to deeper water with safety
   - Multiple safety personnel present

3. **Recording Setup**
   - Multiple camera angles
   - High-quality recording equipment
   - Proper lighting

#### Cost Considerations
- Camera equipment: $500-$2000
- Pool rental: $50-$200/hour
- Professional lifeguards: $20-$50/hour
- Actors/participants: $15-$30/hour
- Total estimated cost: $2000-$10,000 for comprehensive dataset

---

### 4.2 Using Existing Surveillance Footage

#### Approach Swimming Pools
**Proposal Template**:
```
Subject: Research Collaboration - AI Drowning Detection System

Dear [Pool Manager],

I am a [your status] at [your institution] conducting research on 
AI-based drowning detection systems. 

We are seeking to collect video footage of swimmers in pool environments 
to train our detection algorithms. The system aims to improve water 
safety by providing early warning of potential drowning incidents.

Benefits to your facility:
- Free evaluation of our system for your pool
- Contribution to water safety research
- Recognition in our research publications
- No cost to your facility

Privacy and Security:
- All footage will be anonymized
- Faces can be blurred if required
- Data securely stored and not shared publicly
- IRB approved research protocol

Would you be interested in discussing this collaboration?

Best regards,
[Your name]
```

---

### 4.3 Crowdsourcing

#### Platforms
- **Amazon Mechanical Turk**: For annotations
- **Figure Eight (Appen)**: Data labeling
- **Labelbox**: Annotation platform
- **Scale AI**: Professional annotation service

#### What to Crowdsource
- Video collection (users submit videos)
- Frame-level annotations
- Bounding box drawing
- Quality verification

---

## 5. Data Augmentation Techniques

When you have limited real data, use augmentation:

### Video Augmentation
```python
- Temporal cropping
- Frame sampling at different rates
- Speed variation (0.8x - 1.2x)
- Horizontal flipping
- Brightness/contrast adjustment
- Adding synthetic water effects
- Color jittering
- Random rotation (±15°)
- Zoom in/out (0.8-1.2x)
- Adding synthetic rain/waves
```

### Synthetic Data Generation
- **Unity3D**: Create swimming simulations
- **Unreal Engine**: Realistic water physics
- **Blender**: 3D animation of swimming scenarios

---

## 6. Annotation Services

### Professional Annotation Companies
1. **Scale AI** - High quality, expensive
2. **Appen (formerly Figure Eight)** - Mid-range
3. **Hive** - Specialized in video annotation
4. **Labelbox** - Collaborative platform
5. **V7** - AI-assisted annotation

### Cost Estimates
- **Bounding boxes**: $0.01-$0.10 per box
- **Keypoints**: $0.05-$0.20 per person
- **Video classification**: $0.50-$5.00 per video
- **Semantic segmentation**: $1.00-$10.00 per frame

---

## 7. Legal and Ethical Considerations

### Data Collection Ethics
- ✓ IRB approval required
- ✓ Informed consent from all participants
- ✓ Privacy protection (face blurring)
- ✓ Secure data storage
- ✓ Proper data usage agreements

### Copyright and Licensing
- Check video licensing before use
- Cite original sources
- Follow Creative Commons guidelines
- Obtain permission for commercial use

### GDPR and Privacy Laws
- If in EU, follow GDPR
- California: CCPA compliance
- Anonymize personal data
- Provide opt-out mechanisms

---

## 8. Dataset Quality Metrics

### Evaluation Criteria
1. **Diversity**
   - Multiple pool types
   - Various lighting conditions
   - Different age groups
   - Various swimming abilities

2. **Balance**
   - Equal representation of all classes
   - Avoid class imbalance
   - Sufficient samples per category

3. **Quality**
   - High resolution (min 1080p)
   - Good lighting
   - Clear visibility
   - Proper annotations

4. **Realism**
   - Real-world scenarios
   - Natural behaviors
   - Authentic drowning simulations

---

## 9. Benchmarking Your Dataset

### Standard Evaluation
- Train/Val/Test split: 70/15/15
- Cross-validation (5-fold)
- Report multiple metrics:
  - Accuracy
  - Precision
  - Recall
  - F1-Score
  - mAP
  - FPS (real-time performance)

### Compare Against
- State-of-the-art models
- Baseline methods
- Human performance
- Commercial systems

---

## 10. Recommended Tools

### Video Processing
- **FFmpeg**: Video extraction and processing
- **OpenCV**: Computer vision operations
- **MoviePy**: Python video editing

### Annotation Tools
- **CVAT**: Free, comprehensive
- **Labelbox**: Cloud-based
- **VGG Image Annotator (VIA)**: Simple, lightweight
- **Label Studio**: Multi-format support

### Dataset Management
- **DVC** (Data Version Control)
- **Roboflow**: Dataset management for CV
- **FiftyOne**: Dataset visualization

### Model Training
- **PyTorch**: Deep learning framework
- **TensorFlow**: Deep learning framework
- **Detectron2**: Object detection
- **MMDetection**: Toolbox for detection
- **YOLOv8**: Real-time detection

---

## 11. Sample Dataset URLs

### Similar Datasets (for reference)
```
1. UCF Crime Dataset
   https://www.crcv.ucf.edu/projects/real-world/

2. Kinetics-700
   https://github.com/cvdfoundation/kinetics-dataset

3. COCO Dataset
   https://cocodataset.org/

4. UCF101
   https://www.crcv.ucf.edu/data/UCF101.php

5. VIRAT Video Dataset
   http://viratdata.org/

6. YouTube-8M
   https://research.google.com/youtube8m/
```

---

## 12. Conclusion

Building a drowning detection dataset requires:
1. **Safety First**: Always prioritize participant safety
2. **Quality Data**: High-resolution, well-annotated
3. **Diversity**: Various conditions and scenarios
4. **Ethics**: Proper consent and privacy protection
5. **Documentation**: Thorough metadata and guidelines

### Next Steps for Your Project
1. Apply for IRB approval
2. Partner with local pools
3. Collect initial pilot data
4. Validate annotation process
5. Scale up collection
6. Publish dataset (optional)
7. Share with research community

---

## Contact and Collaboration

If you create a dataset or need assistance:
- Share with the research community
- Publish a dataset paper
- Create a GitHub repository
- Host on platforms like Kaggle, Roboflow
- Contribute to open science

---

**Last Updated**: February 16, 2026
**Version**: 1.0
