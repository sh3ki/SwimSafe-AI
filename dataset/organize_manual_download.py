"""
Organize manually downloaded Roboflow dataset into SwimSafe AI structure

INSTRUCTIONS:
1. Download dataset from Roboflow website (Version 4)
2. Extract the ZIP file  
3. Update the EXTRACTED_PATH below to point to your extracted folder
4. Run this script: python organize_manual_download.py
"""

import shutil
from pathlib import Path

# UPDATE THIS PATH to where you extracted the Roboflow dataset
EXTRACTED_PATH = r"C:\Users\USER\Downloads\SwimmingXDrowning-4"  # Change this!

# Dataset structure
DATASET_ROOT = Path(__file__).parent
IMAGES_DIR = DATASET_ROOT / "images"

def organize_images():
    extracted = Path(EXTRACTED_PATH)
    
    if not extracted.exists():
        print(f"❌ Error: Path not found: {extracted}")
        print("\nPlease update EXTRACTED_PATH in this script to point to your extracted dataset folder.")
        return
    
    print(f"✓ Found extracted dataset at: {extracted}")
    print()
    
    # Mapping of Roboflow folders to our folders
    folder_map = {
        "train": "train",
        "valid": "val",  # Roboflow uses 'valid'
        "test": "test"
    }
    
    total_copied = 0
    
    for robo_folder, our_folder in folder_map.items():
        source = extracted / robo_folder
        dest = IMAGES_DIR / our_folder
        
        if not source.exists():
            print(f"⚠ Warning: {robo_folder}/ folder not found, skipping...")
            continue
        
        # Create destination
        dest.mkdir(parents=True, exist_ok=True)
        
        # Copy all image files
        image_exts = ('.jpg', '.jpeg', '.png', '.bmp')
        count = 0
        
        for img_file in source.iterdir():
            if img_file.suffix.lower() in image_exts:
                shutil.copy2(img_file, dest / img_file.name)
                count += 1
        
        print(f"✓ Copied {count:4d} images: {robo_folder}/ → images/{our_folder}/")
        total_copied += count
    
    print()
    print("="*60)
    print(f"✓ SUCCESS! Total images copied: {total_copied}")
    print("="*60)
    print()
    print("Your dataset is now ready in:")
    for folder in ["train", "val", "test"]:
        path = IMAGES_DIR / folder
        if path.exists():
            count = len(list(path.glob("*.jpg"))) + len(list(path.glob("*.png")))
            print(f"  - images/{folder}/ ({count} images)")

if __name__ == "__main__":
    print("\n" + "="*60)
    print("SwimSafe AI - Organize Manual Roboflow Download")
    print("="*60)
    print()
    
    organize_images()
