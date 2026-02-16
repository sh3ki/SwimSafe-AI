"""
Download Images from Roboflow Dataset
This script helps you download all images from your Roboflow project into the dataset structure.

Model: swimmingxdrowning/4
"""

from roboflow import Roboflow
import os
import shutil
from pathlib import Path

# Your Roboflow API Key (from detector.py)
API_KEY = "nj2hBBqtpJKD11ULpQpN"

# Roboflow project details
WORKSPACE = "sh3ki"               # Your workspace
PROJECT = "swimmingxdrowning"     # Your project name
VERSION = 4                        # Model version

# Dataset directory
DATASET_ROOT = Path(__file__).parent  # Current directory (dataset/)
IMAGES_DIR = DATASET_ROOT / "images"


def download_roboflow_dataset():
    """Download dataset from Roboflow and organize into our structure"""
    
    print("="*60)
    print("Roboflow Dataset Downloader for SwimSafe AI")
    print("="*60)
    print(f"Model: {PROJECT}/{VERSION}")
    print(f"Destination: {IMAGES_DIR}")
    print()
    
    # Initialize Roboflow
    try:
        rf = Roboflow(api_key=API_KEY)
        print("✓ Connected to Roboflow")
        
        # Get the project
        project = rf.workspace(WORKSPACE).project(PROJECT)
        print(f"✓ Found project: {PROJECT}")
        
        # Download the dataset (version 4)
        print(f"Downloading version {VERSION}...")
        dataset = project.version(VERSION).download("coco")
        
        print(f"✓ Dataset downloaded to: {dataset.location}")
        
        # Organize files into our structure
        organize_dataset(dataset.location)
        
        print("\n" + "="*60)
        print("✓ Download and organization complete!")
        print("="*60)
        
    except Exception as e:
        print(f"✗ Error: {e}")
        print("\nTroubleshooting:")
        print("1. Make sure you have roboflow installed: pip install roboflow")
        print("2. Check your API key is correct")
        print("3. Verify project name and version")


def organize_dataset(download_path):
    """Organize downloaded images into train/val/test folders"""
    
    download_path = Path(download_path)
    
    # Create destination directories
    for split in ['train', 'val', 'test']:
        (IMAGES_DIR / split).mkdir(parents=True, exist_ok=True)
    
    # Copy images from each split
    splits_map = {
        'train': 'train',
        'valid': 'val',  # Roboflow uses 'valid' instead of 'val'
        'test': 'test'
    }
    
    total_copied = 0
    
    for robo_split, our_split in splits_map.items():
        source_dir = download_path / robo_split
        dest_dir = IMAGES_DIR / our_split
        
        if not source_dir.exists():
            print(f"  Warning: {robo_split}/ folder not found")
            continue
        
        # Copy all images
        image_extensions = ['.jpg', '.jpeg', '.png', '.bmp']
        copied = 0
        
        for img_file in source_dir.iterdir():
            if img_file.suffix.lower() in image_extensions:
                dest_file = dest_dir / img_file.name
                shutil.copy2(img_file, dest_file)
                copied += 1
        
        print(f"  ✓ Copied {copied} images to {our_split}/")
        total_copied += copied
    
    print(f"\nTotal images copied: {total_copied}")
    
    # Also copy annotations if needed
    copy_annotations(download_path)


def copy_annotations(download_path):
    """Copy annotation files to annotations directory"""
    
    download_path = Path(download_path)
    annotations_dir = DATASET_ROOT / "annotations"
    annotations_dir.mkdir(parents=True, exist_ok=True)
    
    # Look for annotation files
    annotation_files = list(download_path.glob("**/_annotations.coco.json"))
    
    if annotation_files:
        print(f"\nCopying annotation files:")
        for ann_file in annotation_files:
            # Determine which split this is for
            split_name = ann_file.parent.name
            dest_name = f"{split_name}_annotations.json"
            dest_file = annotations_dir / dest_name
            
            shutil.copy2(ann_file, dest_file)
            print(f"  ✓ Copied {split_name} annotations")


def get_dataset_info():
    """Get information about the Roboflow dataset"""
    
    try:
        rf = Roboflow(api_key=API_KEY)
        project = rf.workspace(WORKSPACE).project(PROJECT)
        version = project.version(VERSION)
        
        print("="*60)
        print("Roboflow Dataset Information")
        print("="*60)
        print(f"Project: {PROJECT}")
        print(f"Version: {VERSION}")
        print(f"Workspace: {WORKSPACE}")
        print("="*60)
        
    except Exception as e:
        print(f"Could not fetch dataset info: {e}")


if __name__ == "__main__":
    import sys
    
    print("\n")
    
    if len(sys.argv) > 1 and sys.argv[1] == "info":
        get_dataset_info()
    else:
        print("This will download images from Roboflow model: swimmingxdrowning/4")
        print(f"Destination: {IMAGES_DIR}")
        print()
        
        response = input("Continue? (y/n): ")
        
        if response.lower() == 'y':
            download_roboflow_dataset()
        else:
            print("Cancelled.")
