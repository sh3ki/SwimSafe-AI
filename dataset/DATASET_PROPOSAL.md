# Dataset Proposal: SwimSafe AI Drowning Detection Dataset

## Executive Summary

This document proposes the creation of a comprehensive dataset for training and evaluating AI models capable of detecting drowning incidents in swimming pools. The dataset will support the development of the **Smart AI Drowning Detection and Alarm Notification System** thesis project.

---

## 1. Problem Statement

Drowning is a leading cause of accidental death worldwide, with:
- **320,000+** annual drowning deaths globally (WHO)
- Most incidents occur in **swimming pools**
- **Silent nature** of drowning makes it difficult to detect
- Traditional surveillance systems require constant human monitoring

Current Challenges:
- Lack of publicly available drowning detection datasets
- Limited research data for AI model training
- Difficulty in recognizing drowning behavior vs. normal swimming

---

## 2. Dataset Objectives

### Primary Goals
1. Create a **high-quality, annotated dataset** of swimming pool videos
2. Include diverse scenarios: normal swimming, active drowning, passive drowning, and distress
3. Provide multiple annotation formats for different AI approaches
4. Enable real-time drowning detection model development

### Secondary Goals
1. Contribute to water safety research community
2. Establish standardized annotation protocols
3. Create reproducible benchmarks for drowning detection systems
4. Potentially publish as open-source for research advancement

---

## 3. Dataset Specifications

### 3.1 Dataset Size
- **Videos**: 500+ clips (target)
- **Frames**: 15,000+ annotated frames
- **Duration**: 10-60 seconds per clip
- **Total Duration**: ~4 hours of footage

### 3.2 Technical Specifications
- **Resolution**: Minimum 1920x1080 (Full HD)
- **Frame Rate**: 30 FPS
- **Format**: MP4 (H.264 codec)
- **Color Space**: RGB, 8-bit depth

### 3.3 Class Definitions

| Class ID | Class Name | Description | Target Count |
|----------|------------|-------------|--------------|
| 0 | Normal Swimming | Regular swimming behavior | 200 videos (40%) |
| 1 | Active Drowning | Struggling, vertical position | 150 videos (30%) |
| 2 | Passive Drowning | Motionless, floating | 100 videos (20%) |
| 3 | Swimming Distress | Fatigue, irregular patterns | 50 videos (10%) |

### 3.4 Annotation Types
1. **Video-level Classification**: Overall video category
2. **Frame-level Detection**: Per-frame classification and bounding boxes
3. **Temporal Segmentation**: Start/end times of behaviors
4. **Human Pose Keypoints**: 17-point body pose annotations
5. **Metadata**: Pool type, lighting, weather, camera angle, etc.

---

## 4. Data Collection Strategy

### 4.1 Data Sources

#### Phase 1: Existing Resources (Weeks 1-2)
- Public datasets (UCF Crime, Kinetics)
- YouTube video clips (with proper licensing)
- Stock footage websites
- Previous research datasets

#### Phase 2: Controlled Simulations (Weeks 3-6)
- Partner with local swimming pool facilities
- Collaborate with lifeguard training centers
- Professional actors simulating drowning scenarios
- Supervised by certified lifeguards

#### Phase 3: Real-world Footage (Weeks 7-8)
- Surveillance footage from partner pools (with consent)
- Various pool environments (indoor/outdoor)
- Different lighting and weather conditions

### 4.2 Safety Protocols
✅ All simulations supervised by certified lifeguards  
✅ Safety divers on standby  
✅ Medical personnel available  
✅ IRB (Institutional Review Board) approval obtained  
✅ Informed consent from all participants  
✅ Emergency stop protocols established  

---

## 5. Budget Estimation

| Item | Cost (USD) | Notes |
|------|------------|-------|
| Camera Equipment | $800 - $1,500 | GoPro/Action cameras (2-3 units) |
| Pool Rental | $400 - $1,200 | $50-200/hour × 6-8 sessions |
| Lifeguard Services | $480 - $1,200 | $20-50/hour × 24 hours |
| Actors/Participants | $600 - $1,500 | $15-30/hour × 40 hours |
| Annotation Services | $500 - $2,000 | Professional annotation (if needed) |
| Storage (Cloud) | $100 - $300 | 1TB+ cloud storage for 1 year |
| Miscellaneous | $200 - $500 | Travel, equipment rental, etc. |
| **TOTAL** | **$3,080 - $8,200** | Estimated range |

**Budget Optimization Options:**
- Use university pool facilities (reduced/free rental)
- Recruit student volunteers for simulations
- Use existing equipment from computer science department
- Annotate data ourselves (time investment vs. cost)

**Minimal Viable Dataset Budget**: ~$1,500-$2,000

---

## 6. Timeline

### 8-Week Collection and Annotation Plan

| Week | Tasks | Deliverables |
|------|-------|--------------|
| 1 | IRB approval, equipment setup, partner outreach | Approved protocols, partnerships |
| 2 | Collect existing video data, test recordings | 50-100 videos from public sources |
| 3 | First data collection session (normal swimming) | 80-100 normal swimming videos |
| 4 | Second session (drowning simulations - active) | 60-80 active drowning videos |
| 5 | Third session (drowning simulations - passive, distress) | 60-80 passive drowning/distress videos |
| 6 | Additional recordings to fill gaps | Complete 500 video target |
| 7 | Frame extraction and annotation | 50% annotations complete |
| 8 | Complete annotations, quality control | 100% dataset ready |

**Critical Path Items:**
- IRB approval (can take 2-4 weeks)
- Pool facility partnerships
- Equipment acquisition

---

## 7. Annotation Strategy

### 7.1 Annotation Tools
- **CVAT** (Computer Vision Annotation Tool) - Free, open-source
- **Labelbox** - Cloud-based collaboration
- **VGG Image Annotator (VIA)** - Lightweight option

### 7.2 Annotation Workflow
1. **Video Classification**: Assign overall class label
2. **Frame Extraction**: Extract frames every 1-2 seconds
3. **Bounding Box Annotation**: Draw boxes around persons
4. **Keypoint Annotation**: Mark 17 body keypoints
5. **Metadata Recording**: Document environmental conditions
6. **Quality Control**: Second annotator reviews 20% of data

### 7.3 Annotation Team
- **Lead Annotator**: Yourself (familiar with drowning behaviors)
- **Assistant Annotators**: 1-2 team members or hired annotators
- **Quality Reviewer**: Advisor or domain expert (lifeguard)

### 7.4 Inter-Annotator Agreement
- Calculate Cohen's Kappa or Fleiss' Kappa
- Target agreement: >0.8 (substantial agreement)
- Resolve disagreements through discussion

---

## 8. Dataset Validation

### 8.1 Quality Metrics
- Resolution and frame rate consistency
- Annotation completeness (100% of samples)
- Inter-annotator agreement
- Class balance
- Diversity of scenarios

### 8.2 Validation Process
```python
✓ Automated checks for file integrity
✓ Verify all required metadata present
✓ Check annotation format consistency
✓ Validate bounding box coordinates
✓ Ensure train/val/test split integrity
```

---

## 9. Expected Outcomes

### 9.1 Research Contributions
1. **First comprehensive drowning detection dataset** (potentially)
2. **Standardized evaluation protocol** for drowning detection systems
3. **Baseline AI model performance** benchmarks
4. **Publication opportunity** at computer vision conference

### 9.2 Practical Applications
1. Train production-ready drowning detection models
2. Validate SwimSafe AI system performance
3. Deploy to real swimming pool facilities
4. Save lives through early detection

### 9.3 Academic Impact
- **Thesis defense**: Strong, data-driven foundation
- **Publications**: Dataset paper + application paper
- **Citations**: Future researchers will cite your work
- **Community contribution**: Advance water safety research

---

## 10. Ethical and Legal Considerations

### 10.1 Ethics
✓ IRB approval for human subjects research  
✓ Informed consent from all participants  
✓ Safety as top priority (no real drowning risk)  
✓ Privacy protection (face blurring if needed)  
✓ Transparent data usage policies  

### 10.2 Legal
✓ Copyright clearance for all video sources  
✓ Data usage agreements with pool facilities  
✓ GDPR/CCPA compliance for personal data  
✓ Liability waivers for participants  
✓ Insurance coverage for data collection activities  

### 10.3 Data Privacy
- Anonymize all personal information
- Secure storage with encryption
- Access control (authorized researchers only)
- Option to withdraw data at any time
- No facial recognition without explicit consent

---

## 11. Dataset Distribution

### 11.1 Initial Use
- Private use for thesis research
- Validation of SwimSafe AI system
- Model training and testing

### 11.2 Potential Public Release
**Options:**
1. **Institutional Repository**: University's research data repository
2. **Kaggle**: Host as a Kaggle dataset/competition
3. **GitHub**: Release with paper publication
4. **Roboflow**: Computer vision dataset platform
5. **IEEE DataPort**: Professional research data hosting

**Licensing Options:**
- CC BY 4.0 (Attribution)
- CC BY-NC 4.0 (Non-commercial)
- CC BY-SA 4.0 (Share-alike)

---

## 12. Success Criteria

### Minimum Viable Dataset (MVP)
- ✅ 200+ videos across all classes
- ✅ 6,000+ annotated frames
- ✅ Basic metadata and annotations
- ✅ Train/val/test splits
- ✅ Documentation and loading scripts

### Ideal Complete Dataset
- ✅ 500+ videos across all classes
- ✅ 15,000+ annotated frames
- ✅ Comprehensive annotations (boxes + keypoints)
- ✅ Detailed metadata
- ✅ Validation benchmarks
- ✅ Published documentation

---

## 13. Backup Plan

If primary data collection faces challenges:

### Alternative Approaches
1. **Data Augmentation**: Expand smaller dataset through augmentation
2. **Transfer Learning**: Use pre-trained models on similar tasks
3. **Synthetic Data**: Generate simulated scenarios using Unity/Unreal
4. **Collaboration**: Partner with other researchers for data sharing
5. **Reduced Scope**: Focus on 2-3 classes instead of 4

---

## 14. References and Related Work

### Key Research Papers
1. "Drowning Detection Based on Deep Learning" (Various authors, 2018-2024)
2. "Computer Vision for Swimming Pool Surveillance"
3. "Human Activity Recognition in Videos"
4. "Anomaly Detection in Surveillance Videos"

### Existing Datasets (for reference)
- UCF Crime Dataset
- Kinetics-700
- COCO (for pose estimation)
- VIRAT Video Dataset

---

## 15. Conclusion

This dataset will provide the **foundation for developing a reliable AI-based drowning detection system**. The proposed approach balances:
- **Scientific rigor**: Proper annotation and validation
- **Safety**: All simulations supervised by professionals
- **Feasibility**: Realistic timeline and budget
- **Impact**: Potential to save lives and advance research

### Next Steps
1. **Present proposal** to thesis advisor/committee
2. **Secure funding** or identify cost-reduction strategies
3. **Begin IRB application** process
4. **Initiate partnerships** with pool facilities
5. **Acquire equipment** and test recording setup
6. **Start with Phase 1** (existing data collection)

---

## 16. Contact Information

**Student Researcher**: [Your Name]  
**Email**: [your.email@university.edu]  
**Advisor**: [Advisor Name]  
**Institution**: [University Name]  
**Department**: [Department Name]  

**Project Repository**: [GitHub URL]  
**Last Updated**: February 16, 2026

---

## Appendices

### Appendix A: Sample Consent Form
[Included in supplementary materials]

### Appendix B: IRB Application Template
[Included in supplementary materials]

### Appendix C: Dataset Structure Diagram
[See README.md in dataset folder]

### Appendix D: Annotation Guidelines
[See DATA_COLLECTION_GUIDE.md]

### Appendix E: Budget Breakdown Details
[Detailed cost analysis available upon request]

---

**Document Version**: 1.0  
**Date**: February 16, 2026  
**Status**: Proposal - Awaiting Approval
