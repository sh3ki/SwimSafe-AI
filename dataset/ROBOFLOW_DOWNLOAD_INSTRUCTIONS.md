# How to Download Images from Your Roboflow Model

## Your Current Model

**Model ID**: `swimmingxdrowning/4`
- Workspace: swimmingxdrowning
- Project: swimmingxdrowning
- Version: 4

---

## Method 1: Using the Python Script (RECOMMENDED)

### Step 1: Install Roboflow SDK
```powershell
pip install roboflow
```

### Step 2: Run the Download Script
```powershell
cd "C:\Users\USER\Documents\SYSTEMS\IOT\SwimSafe AI\dataset"
python download_roboflow_images.py
```

This will:
- ✅ Download all images from version 4
- ✅ Organize them into train/val/test folders
- ✅ Copy annotations to the annotations folder
- ✅ Show progress and statistics

---

## Method 2: Manual Download from Roboflow Web

### Step 1: Go to Roboflow Dashboard
1. Visit: https://app.roboflow.com/
2. Log in with your account
3. Navigate to your project: `swimmingxdrowning`
4. Select Version 4

### Step 2: Export Dataset
1. Click on **"Export Dataset"** or **"Download"**
2. Select format: **COCO JSON** (for bounding boxes)
3. Click **"Download ZIP"**
4. Wait for download to complete

### Step 3: Extract and Organize
1. Extract the ZIP file
2. You'll see folders: `train/`, `valid/`, `test/`
3. Copy images:
   ```
   From: extracted_folder/train/*.jpg
   To:   dataset/images/train/
   
   From: extracted_folder/valid/*.jpg
   To:   dataset/images/val/
   
   From: extracted_folder/test/*.jpg
   To:   dataset/images/test/
   ```

### Step 4: Copy Annotations
Copy the `_annotations.coco.json` files:
```
From: extracted_folder/train/_annotations.coco.json
To:   dataset/annotations/train_annotations.json

From: extracted_folder/valid/_annotations.coco.json
To:   dataset/annotations/val_annotations.json

From: extracted_folder/test/_annotations.coco.json
To:   dataset/annotations/test_annotations.json
```

---

## Method 3: Using Roboflow CLI

### Step 1: Install Roboflow CLI
```powershell
pip install roboflow
```

### Step 2: Download via Command Line
```powershell
# Navigate to dataset folder
cd "C:\Users\USER\Documents\SYSTEMS\IOT\SwimSafe AI\dataset"

# Run Python command
python -c "from roboflow import Roboflow; rf = Roboflow(api_key='nj2hBBqtpJKD11ULpQpN'); project = rf.workspace('swimmingxdrowning').project('swimmingxdrowning'); dataset = project.version(4).download('coco')"
```

---

## Verify Download

After downloading, verify the structure:

```
dataset/
├── images/
│   ├── train/          ← Should contain training images
│   ├── val/            ← Should contain validation images
│   └── test/           ← Should contain test images
└── annotations/
    ├── train_annotations.json
    ├── val_annotations.json
    └── test_annotations.json
```

### Check Image Counts
```powershell
# Run this in PowerShell
cd "C:\Users\USER\Documents\SYSTEMS\IOT\SwimSafe AI\dataset"

# Count images in each folder
(Get-ChildItem "images/train" -Filter *.jpg).Count
(Get-ChildItem "images/val" -Filter *.jpg).Count
(Get-ChildItem "images/test" -Filter *.jpg).Count
```

---

## Troubleshooting

### Error: "roboflow module not found"
```powershell
pip install roboflow
```

### Error: "Invalid API key"
- Check your API key in detector.py (line 12): `nj2hBBqtpJKD11ULpQpN`
- Verify it's still valid at https://app.roboflow.com/settings/api

### Error: "Project not found"
- Make sure the workspace and project names are correct
- Check if you have access to the project
- Try logging into Roboflow web interface first

### Images not downloading
- Check your internet connection
- Verify you have enough disk space
- Make sure you have permissions to the project

---

## Dataset Statistics

After downloading, you can check statistics:

```powershell
cd "C:\Users\USER\Documents\SYSTEMS\IOT\SwimSafe AI\dataset"
python dataset_loader.py
```

This will show:
- Total images per split
- Class distribution
- Annotation counts
- Dataset validation results

---

## Next Steps After Download

1. ✅ Verify all images downloaded correctly
2. ✅ Check annotations are present
3. ✅ Run dataset validation script
4. ✅ Update your dataset documentation with actual counts
5. ✅ Start training your AI model!

---

## Quick Command Summary

```powershell
# Install Roboflow
pip install roboflow

# Download dataset
cd "C:\Users\USER\Documents\SYSTEMS\IOT\SwimSafe AI\dataset"
python download_roboflow_images.py

# Verify dataset
python dataset_loader.py

# Check image counts
(Get-ChildItem "images/train" -Filter *.jpg).Count
(Get-ChildItem "images/val" -Filter *.jpg).Count
(Get-ChildItem "images/test" -Filter *.jpg).Count
```

---

**Your API Key**: `nj2hBBqtpJKD11ULpQpN` (already configured)  
**Model**: `swimmingxdrowning/4`  
**Last Updated**: February 16, 2026
