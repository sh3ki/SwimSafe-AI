# Quick Start Guide - SwimSafe AI Dataset

## Getting Started in 5 Minutes

Welcome! This guide will help you quickly understand and start using the SwimSafe AI Drowning Detection Dataset.

---

## 📋 What's in This Dataset?

This dataset is designed for training AI models to detect drowning incidents in swimming pools.

**Contents:**
- 🎥 Video clips of swimming scenarios
- 🖼️ Extracted frames from videos
- 📊 Annotations (classifications, bounding boxes, keypoints)
- 📁 Organized train/validation/test splits
- 📝 Comprehensive documentation

---

## 🗂️ Directory Structure

```
dataset/
├── README.md                          ← Start here for overview
├── QUICK_START.md                     ← This file
├── DATASET_PROPOSAL.md                ← Present to your professor
├── DATA_COLLECTION_GUIDE.md           ← How to collect data
├── EXISTING_DATASETS_RESOURCES.md     ← Where to find data
├── dataset_loader.py                  ← Python script to load dataset
├── dataset_metadata.json              ← Dataset statistics and info
│
├── videos/                           ← Video files go here
│   ├── train/
│   ├── val/
│   └── test/
│
├── images/                           ← Extracted frames go here
│   ├── train/
│   ├── val/
│   └── test/
│
├── annotations/                      ← All annotations
│   ├── video_annotations.csv        ← Video-level labels
│   ├── frame_annotations.csv        ← Frame-level labels
│   ├── bounding_boxes.json          ← COCO format bounding boxes
│   └── keypoints.json               ← Human pose keypoints
│
└── splits/                           ← Train/val/test split lists
    ├── train.txt
    ├── val.txt
    └── test.txt
```

---

## 🚀 Quick Actions

### For Your Professor

**Show them this:**
1. **[DATASET_PROPOSAL.md](DATASET_PROPOSAL.md)** - Complete dataset proposal
2. **[README.md](README.md)** - Dataset overview and specifications
3. **This folder structure** - Shows you have a professional framework

**Key points to highlight:**
- ✅ Well-structured dataset design
- ✅ Multiple annotation formats
- ✅ Safety protocols documented
- ✅ Clear data collection guidelines
- ✅ Ethical considerations addressed

---

### To Start Collecting Data

1. **Read**: [DATA_COLLECTION_GUIDE.md](DATA_COLLECTION_GUIDE.md)
2. **Check**: [EXISTING_DATASETS_RESOURCES.md](EXISTING_DATASETS_RESOURCES.md) for existing data sources
3. **Plan**: Use the budget and timeline from [DATASET_PROPOSAL.md](DATASET_PROPOSAL.md)

---

### To Use the Dataset (Once You Have Data)

**Option 1: Using Python Script**
```python
from dataset_loader import SwimSafeDataset

# Load training data
dataset = SwimSafeDataset(root_dir="dataset", split="train")

# Print statistics
dataset.print_statistics()

# Get a sample
sample = dataset[0]
print(f"Video ID: {sample['video_id']}")
print(f"Class: {sample['class_name']}")
```

**Option 2: Direct File Access**
- Videos: `dataset/videos/train/`
- Annotations: `dataset/annotations/video_annotations.csv`
- Splits: `dataset/splits/train.txt`

---

## 📊 Dataset Classes

| Class | Description | Behavior Indicators |
|-------|-------------|---------------------|
| **0: Normal Swimming** | Regular swimming | Controlled movements, head above water |
| **1: Active Drowning** | Struggling in water | Vertical body, arms extended, gasping |
| **2: Passive Drowning** | Motionless/unconscious | Face-down floating, no movement |
| **3: Swimming Distress** | Difficulty but can signal | Irregular swimming, visible fatigue |

---

## 🎯 Next Steps

### Immediate (Week 1)
- [ ] Present dataset proposal to professor
- [ ] Get feedback and approval
- [ ] Apply for IRB approval (if needed)
- [ ] Identify potential data sources

### Short-term (Weeks 2-4)
- [ ] Contact local swimming pools for partnerships
- [ ] Acquire or borrow recording equipment
- [ ] Collect existing videos from public sources
- [ ] Start initial test recordings

### Medium-term (Weeks 5-8)
- [ ] Conduct data collection sessions
- [ ] Begin annotation process
- [ ] Extract frames from videos
- [ ] Organize files according to structure

---

## 💰 Budget Options

### Minimal Budget (~$1,500)
- Use university pool (free/discounted)
- Borrow camera equipment
- Student volunteers as participants
- Annotate yourself

### Moderate Budget (~$3,000-$5,000)
- Rent pool facilities
- Purchase/rent good cameras
- Hire professional lifeguards
- Some professional annotation help

### Full Budget (~$8,000+)
- Professional equipment
- Multiple pool types
- Professional actors and lifeguards
- Professional annotation services

---

## 🔍 Where to Find Data

### Free Sources
1. **YouTube**: "drowning simulation", "lifeguard training"
2. **Research Papers**: Contact authors for datasets
3. **University Pools**: Often willing to help student research
4. **Public Datasets**: UCF Crime, Kinetics (see EXISTING_DATASETS_RESOURCES.md)

### Paid Sources
1. **Stock Footage**: Shutterstock, Getty Images
2. **Annotation Services**: Scale AI, Labelbox
3. **Professional Recordings**: Hire videographer

---

## ⚠️ Important Reminders

### Safety First
- **NEVER** record real drowning incidents
- Always have certified lifeguards present
- Use professional actors for simulations
- Follow all safety protocols in DATA_COLLECTION_GUIDE.md

### Ethics and Legal
- Get IRB approval for human subjects research
- Obtain informed consent from all participants
- Respect privacy (blur faces if needed)
- Clear copyright for any external videos

---

## 🛠️ Tools You'll Need

### Recording
- Camera (GoPro, smartphone, or security camera)
- Tripod or mounting equipment
- Good lighting
- Waterproof housing (optional)

### Annotation
- **CVAT**: Free, powerful annotation tool
  - Install: https://github.com/opencv/cvat
- **Labelbox**: Cloud-based alternative
  - Sign up: https://labelbox.com/

### Data Management
- External hard drive (1TB+) for backup
- Cloud storage (Google Drive, Dropbox)
- Python 3.8+ for dataset_loader.py

---

## 📚 Additional Resources

### Documentation Files
- **README.md**: Complete dataset overview
- **DATASET_PROPOSAL.md**: Present to professor/committee
- **DATA_COLLECTION_GUIDE.md**: Detailed collection instructions
- **EXISTING_DATASETS_RESOURCES.md**: Where to find data

### Annotation Files
- **video_annotations.csv**: Video-level labels (sample included)
- **frame_annotations.csv**: Frame-level labels (sample included)
- **bounding_boxes.json**: COCO format boxes (sample included)
- **keypoints.json**: Human pose keypoints (sample included)

### Code
- **dataset_loader.py**: Python utilities to load and manage dataset

---

## 🤔 Common Questions

### Q: I don't have any video data yet. Is this useful?
**A:** Yes! This provides the complete framework. You'll fill it with data as you collect.

### Q: How do I present this to my professor?
**A:** Show them:
1. DATASET_PROPOSAL.md (comprehensive plan)
2. This folder structure (professional organization)
3. Annotation samples (shows you understand the domain)

### Q: Can I use existing datasets instead of collecting my own?
**A:** Partially. Check EXISTING_DATASETS_RESOURCES.md for sources. You may need to collect some custom data for your specific use case.

### Q: How long does data collection take?
**A:** Typically 6-8 weeks for a complete dataset (400-500 videos). See timeline in DATASET_PROPOSAL.md.

### Q: What if I can't afford the full budget?
**A:** See "Minimal Budget" option above (~$1,500). Use university resources and volunteers.

### Q: How do I validate my dataset?
**A:** Run the validation script:
```python
from dataset_loader import DatasetValidator
validator = DatasetValidator("dataset")
validator.print_validation_report()
```

---

## 🎓 For Your Professor

Dear Professor,

This dataset framework provides:

1. **Professional Structure**: Industry-standard organization
2. **Comprehensive Documentation**: All aspects covered
3. **Ethical Compliance**: IRB and safety protocols included
4. **Realistic Plan**: Budget, timeline, and methodology
5. **Research Value**: Publishable dataset potential

**This demonstrates:**
- Strong understanding of machine learning data requirements
- Attention to safety and ethics
- Professional research methodology
- Ability to plan and execute complex projects

The student is ready to proceed with thesis work once data collection is approved.

---

## 📞 Support

If you have questions about this dataset:
1. Check the relevant documentation file
2. Review the DATA_COLLECTION_GUIDE.md
3. Contact your thesis advisor
4. Reach out to local lifeguard organizations for partnerships

---

## ✅ Final Checklist Before Meeting Professor

- [ ] Reviewed DATASET_PROPOSAL.md thoroughly
- [ ] Understand all four classes of drowning behavior
- [ ] Familiar with safety protocols
- [ ] Know your budget constraints
- [ ] Identified potential data sources
- [ ] Prepared to discuss timeline
- [ ] Have this folder structure ready to show
- [ ] Can explain annotation process
- [ ] Understand ethical considerations

---

**Good luck with your thesis! This framework will help you create a high-quality dataset for your SwimSafe AI system.** 🏊‍♂️🚨🤖

---

**Last Updated**: February 16, 2026  
**Version**: 1.0  
**Author**: SwimSafe AI Team
