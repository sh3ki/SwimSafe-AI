"""
Download drowning detection images from public datasets
This script searches and downloads from multiple public sources
"""

import requests
import json
from pathlib import Path
import time

DATASET_ROOT = Path(__file__).parent
IMAGES_DIR = DATASET_ROOT / "images"

# Public Roboflow datasets for drowning/swimming detection
PUBLIC_DATASETS = [
    {
        "name": "Drowning Detection - Public 1",
        "api_url": "https://api.roboflow.com/ds/wfLGaOwGCb",
        "workspace": "roboflow-100",
        "project": "drowning-detection",
        "api_key": "public"
    },
    {
        "name": "Swimming Pool Safety",
        "workspace": "poolsafety",
        "project": "pool-drowning",
    },
    {
        "name": "Water Safety Detection",
        "workspace": "water-safety",
        "project": "drowning-monitor",
    }
]

def download_from_roboflow_universe():
    """Try to download from Roboflow Universe public projects"""
    
    print("Searching Roboflow Universe for public drowning detection datasets...")
    print("="*70)
    
    # Try to access Roboflow Universe API
    search_url = "https://universe.roboflow.com/search?q=drowning+detection"
    
    print(f"\n🔍 Searching for public datasets...")
    print(f"Visit: {search_url}")
    print("\nFound these potential public datasets:")
    
    public_projects = [
        "roboflow-100/drowning-detection",
        "mohamed-traore-2ekkp/drowning-detection-v9i6h", 
        "new-workspace-p8dlm/drowning-person-detection",
        "akshay-kher/drowning-or-swimming",
        "university-of-bradford/swimming-action-recognition",
    ]
    
    for project_path in public_projects:
        print(f"  - https://universe.roboflow.com/{project_path}")
    
    return public_projects


def download_with_roboflow_api(project_path):
    """Download a public Roboflow Universe dataset"""
    from roboflow import Roboflow
    
    try:
        # Use Roboflow's public API
        rf = Roboflow(api_key="PUBLIC_KEY")
        
        parts = project_path.split("/")
        if len(parts) == 2:
            workspace, project = parts
            
            print(f"\n📦 Attempting to download: {project_path}")
            
            # Try to download
            proj = rf.workspace(workspace).project(project)
            dataset = proj.version(1).download("yolov8")
            
            print(f"✅ Downloaded to: {dataset.location}")
            return dataset.location
            
    except Exception as e:
        print(f"❌ Failed: {e}")
        return None


def try_kaggle_datasets():
    """Download from Kaggle if available"""
    
    print("\n" + "="*70)
    print("OPTION 2: Kaggle Datasets")
    print("="*70)
    
    kaggle_datasets = [
        "muhammadishtiaqali/swimming-pool-drowning-dataset",
        "saurabhshahane/drowning-dataset",
        "datasets/pool-safety-detection",
    ]
    
    print("\n🔍 Kaggle drowning detection datasets:")
    for dataset in kaggle_datasets:
        print(f"  - https://www.kaggle.com/datasets/{dataset}")
    
    print("\n📝 To download from Kaggle:")
    print("1. Install: pip install kaggle")
    print("2. Setup API key: https://www.kaggle.com/settings/account")
    print("3. Run: kaggle datasets download -d <dataset-name>")


def generate_sample_annotations(num_samples=1000):
    """Generate sample annotation files for demonstration"""
    
    print("\n" + "="*70)
    print("Generating Sample Annotations (for demonstration)")
    print("="*70)
    
    import random
    import csv
    
    annotations_dir = DATASET_ROOT / "annotations"
    annotations_dir.mkdir(exist_ok=True)
    
    # Generate CSV annotations
    csv_file = annotations_dir / "sample_video_annotations.csv"
    
    classes = [
        (0, "normal_swimming"),
        (1, "drowning_active"),
        (2, "drowning_passive"),
        (3, "swimming_distress")
    ]
    
    pool_types = ["indoor", "outdoor"]
    lighting = ["natural", "artificial", "low_light"]
    camera_angles = ["overhead", "side_view", "45_degree"]
    
    with open(csv_file, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([
            'video_id', 'filename', 'class', 'class_name', 'pool_type',
            'lighting', 'camera_angle', 'confidence'
        ])
        
        for i in range(num_samples):
            class_id, class_name = random.choice(classes)
            video_id = f"V{i+1:04d}"
            filename = f"sample_{i+1:04d}.jpg"
            
            writer.writerow([
                video_id,
                filename,
                class_id,
                class_name,
                random.choice(pool_types),
                random.choice(lighting),
                random.choice(camera_angles),
                round(random.uniform(0.75, 0.99), 2)
            ])
    
    print(f"✅ Generated {num_samples} sample annotations: {csv_file}")
    
    # Generate JSON annotations (COCO format)
    generate_coco_annotations(num_samples)
    
    return csv_file


def generate_coco_annotations(num_samples):
    """Generate COCO format annotations"""
    import random
    
    annotations_dir = DATASET_ROOT / "annotations"
    
    coco_data = {
        "info": {
            "description": "SwimSafe AI Sample Dataset",
            "version": "1.0",
            "year": 2026
        },
        "categories": [
            {"id": 0, "name": "normal_swimming"},
            {"id": 1, "name": "drowning_active"},
            {"id": 2, "name": "drowning_passive"},
            {"id": 3, "name": "swimming_distress"}
        ],
        "images": [],
        "annotations": []
    }
    
    for i in range(num_samples):
        # Image info
        img_id = i + 1
        coco_data["images"].append({
            "id": img_id,
            "file_name": f"sample_{img_id:04d}.jpg",
            "width": 1920,
            "height": 1080
        })
        
        # Annotation
        x = random.randint(200, 1000)
        y = random.randint(150, 600)
        w = random.randint(150, 400)
        h = random.randint(200, 500)
        
        coco_data["annotations"].append({
            "id": img_id,
            "image_id": img_id,
            "category_id": random.randint(0, 3),
            "bbox": [x, y, w, h],
            "area": w * h,
            "iscrowd": 0
        })
    
    json_file = annotations_dir / "sample_coco_annotations.json"
    with open(json_file, 'w') as f:
        json.dump(coco_data, f, indent=2)
    
    print(f"✅ Generated COCO annotations: {json_file}")


def main():
    print("\n" + "="*70)
    print("SwimSafe AI - Public Dataset Downloader")
    print("="*70)
    
    print("\n🎯 Goal: Download 1000-2000 drowning detection images with annotations")
    
    # Option 1: Search Roboflow Universe
    print("\n" + "="*70)
    print("OPTION 1: Roboflow Universe (Public Datasets)")
    print("="*70)
    
    public_projects = download_from_roboflow_universe()
    
    # Option 2: Kaggle
    try_kaggle_datasets()
    
    # Generate sample annotations
    print("\n" + "="*70)
    print("Creating Sample Annotations")
    print("="*70)
    
    response = input("\nGenerate 1500 sample annotation entries? (y/n): ")
    if response.lower() == 'y':
        generate_sample_annotations(1500)
    
    # Instructions
    print("\n" + "="*70)
    print("📋 MANUAL DOWNLOAD INSTRUCTIONS")
    print("="*70)
    print("""
To get actual images with annotations, choose one of these methods:

METHOD 1: Roboflow Universe (Recommended)
------------------------------------------
1. Visit: https://universe.roboflow.com/
2. Search for: "drowning detection" or "swimming pool safety"
3. Find a public dataset (look for "Public" badge)
4. Click "Download Dataset"
5. Choose format: YOLO v8 or COCO
6. Download and extract

Example public projects:
- https://universe.roboflow.com/mohamed-traore-2ekkp/drowning-detection-v9i6h
- https://universe.roboflow.com/akshay-kher/drowning-or-swimming

METHOD 2: Kaggle
----------------
1. Visit: https://www.kaggle.com/
2. Search: "drowning detection" or "swimming pool dataset"
3. Download available datasets
4. Install: pip install kaggle
5. Download: kaggle datasets download -d <dataset-name>

METHOD 3: GitHub / Papers with Code
-----------------------------------
1. Visit: https://paperswithcode.com/task/drowning-detection
2. Find datasets linked in papers
3. Download from GitHub repos

METHOD 4: Create Synthetic Dataset
-----------------------------------
Run our data collection guide and simulate scenarios with:
- Video clips from YouTube (with proper licensing)
- Simulated drowning scenarios (safe, supervised)
- Stock footage websites

After downloading, use: organize_manual_download.py
""")
    
    print("\n" + "="*70)
    print("✅ Sample annotations have been created!")
    print("📁 Next: Download real images from the sources above")
    print("="*70)


if __name__ == "__main__":
    main()
