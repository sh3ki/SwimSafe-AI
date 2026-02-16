"""Simple direct download script"""
import os
import shutil
from roboflow import Roboflow
from pathlib import Path

# Clean up previous failed attempt
old_dir = Path("SwimmingXDrowning-4")
if old_dir.exists():
    try:
        shutil.rmtree(old_dir)
    except:
        pass

# Download
rf = Roboflow(api_key="nj2hBBqtpJKD11ULpQpN")
project = rf.project("swimmingxdrowning")

print("Downloading dataset in YOLOv8 format...")
dataset = project.version(4).download("yolov8", location="downloaded_dataset")

print(f"\nDownloaded to: {dataset.location}")
print("\nContents:")
for item in Path(dataset.location).iterdir():
    print(f"  - {item.name}")
