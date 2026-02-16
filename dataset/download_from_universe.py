"""
Download images from public Roboflow Universe projects
Attempts multiple public drowning detection datasets
"""

from roboflow import Roboflow
from pathlib import Path
import shutil

DATASET_ROOT = Path(__file__).parent
IMAGES_DIR = DATASET_ROOT / "images"

# Public Roboflow Universe projects (no auth required)
PUBLIC_PROJECTS = [
    ("mohamed-traore-2ekkp", "drowning-detection-v9i6h", 2),
    ("akshay-kher", "drowning-or-swimming", 1),
    ("new-workspace-p8dlm", "drowning-person-detection", 1),
]

def download_public_project(workspace, project, version=1):
    """Download from a public Roboflow Universe project"""
    
    print(f"\n{'='*70}")
    print(f"📦 Downloading: {workspace}/{project} (v{version})")
    print('='*70)
    
    try:
        # Initialize without API key for public datasets
        rf = Roboflow(api_key="")
        
        # Access project
        proj = rf.workspace(workspace).project(project)
        
        # Download
        print("Downloading dataset...")
        dataset = proj.version(version).download("yolov8", location=f"temp_{project}")
        
        print(f"✅ Downloaded to: {dataset.location}")
        return dataset.location
        
    except Exception as e:
        print(f"❌ Failed: {e}")
        
        # Try with Universe public access
        try:
            print("Trying with Universe public access...")
            url = f"https://universe.roboflow.com/{workspace}/{project}/{version}/dataset/download"
            print(f"Visit to download manually: {url}")
        except:
            pass
        
        return None


def organize_downloaded_images(download_path):
    """Organize downloaded images into our structure"""
    
    if not download_path or not Path(download_path).exists():
        return 0
    
    download_path = Path(download_path)
    
    # Mapping
    folder_map = {
        "train": "train",
        "valid": "val",
        "test": "test"
    }
    
    total = 0
    
    for source_name, dest_name in folder_map.items():
        source = download_path / source_name
        dest = IMAGES_DIR / dest_name
        
        if not source.exists():
            continue
        
        dest.mkdir(parents=True, exist_ok=True)
        
        # Copy images
        count = 0
        for img_file in source.glob("*.[jJ][pP]*[gG]"):
            shutil.copy2(img_file, dest / img_file.name)
            count += 1
        
        for img_file in source.glob("*.[pP][nN][gG]"):
            shutil.copy2(img_file, dest / img_file.name)
            count += 1
        
        print(f"  ✅ Copied {count} images to images/{dest_name}/")
        total += count
    
    return total


def main():
    print("\n" + "="*70)
    print("Downloading from Public Roboflow Universe Datasets")
    print("="*70)
    
    total_downloaded = 0
    
    for workspace, project, version in PUBLIC_PROJECTS:
        download_path = download_public_project(workspace, project, version)
        
        if download_path:
            count = organize_downloaded_images(download_path)
            total_downloaded += count
        
        if total_downloaded >= 1000:
            print(f"\n✅ Downloaded {total_downloaded} images - target reached!")
            break
    
    print("\n" + "="*70)
    print(f"📊 Total images downloaded: {total_downloaded}")
    print("="*70)
    
    if total_downloaded < 100:
        print("\n⚠️  Automatic download didn't work well.")
        print("Please download manually from:")
        print("https://universe.roboflow.com/mohamed-traore-2ekkp/drowning-detection-v9i6h")
        print("\nThen run: python organize_manual_download.py")


if __name__ == "__main__":
    main()
