"""
SwimSafe AI Dataset Loader and Management Utilities

This script provides utilities for loading, processing, and managing
the SwimSafe AI drowning detection dataset.

Author: SwimSafe AI Team
Date: 2026-02-16
Version: 1.0
"""

import os
import json
import csv
import pandas as pd
import numpy as np
from pathlib import Path
from typing import Dict, List, Tuple, Optional
from dataclasses import dataclass


@dataclass
class DatasetConfig:
    """Configuration for dataset paths and parameters"""
    root_dir: str
    videos_dir: str = "videos"
    images_dir: str = "images"
    annotations_dir: str = "annotations"
    splits_dir: str = "splits"
    
    def __post_init__(self):
        self.root_path = Path(self.root_dir)
        self.videos_path = self.root_path / self.videos_dir
        self.images_path = self.root_path / self.images_dir
        self.annotations_path = self.root_path / self.annotations_dir
        self.splits_path = self.root_path / self.splits_dir


class SwimSafeDataset:
    """Main dataset class for SwimSafe AI Drowning Detection"""
    
    # Class definitions
    CLASSES = {
        0: "normal_swimming",
        1: "drowning_active",
        2: "drowning_passive",
        3: "swimming_distress"
    }
    
    CLASS_NAMES = ["normal_swimming", "drowning_active", "drowning_passive", "swimming_distress"]
    
    def __init__(self, root_dir: str, split: str = "train"):
        """
        Initialize dataset
        
        Args:
            root_dir: Root directory of the dataset
            split: Dataset split ('train', 'val', or 'test')
        """
        self.config = DatasetConfig(root_dir)
        self.split = split
        
        # Load annotations
        self.video_annotations = self._load_video_annotations()
        self.frame_annotations = self._load_frame_annotations()
        self.bounding_boxes = self._load_bounding_boxes()
        self.keypoints = self._load_keypoints()
        
        # Load split
        self.samples = self._load_split(split)
        
        print(f"Loaded {len(self.samples)} samples for {split} split")
    
    def _load_video_annotations(self) -> pd.DataFrame:
        """Load video-level annotations from CSV"""
        csv_path = self.config.annotations_path / "video_annotations.csv"
        if csv_path.exists():
            return pd.read_csv(csv_path)
        else:
            print(f"Warning: Video annotations not found at {csv_path}")
            return pd.DataFrame()
    
    def _load_frame_annotations(self) -> pd.DataFrame:
        """Load frame-level annotations from CSV"""
        csv_path = self.config.annotations_path / "frame_annotations.csv"
        if csv_path.exists():
            return pd.read_csv(csv_path)
        else:
            print(f"Warning: Frame annotations not found at {csv_path}")
            return pd.DataFrame()
    
    def _load_bounding_boxes(self) -> Dict:
        """Load bounding box annotations from JSON"""
        json_path = self.config.annotations_path / "bounding_boxes.json"
        if json_path.exists():
            with open(json_path, 'r') as f:
                return json.load(f)
        else:
            print(f"Warning: Bounding boxes not found at {json_path}")
            return {}
    
    def _load_keypoints(self) -> Dict:
        """Load keypoint annotations from JSON"""
        json_path = self.config.annotations_path / "keypoints.json"
        if json_path.exists():
            with open(json_path, 'r') as f:
                return json.load(f)
        else:
            print(f"Warning: Keypoints not found at {json_path}")
            return {}
    
    def _load_split(self, split: str) -> List[str]:
        """Load train/val/test split"""
        split_path = self.config.splits_path / f"{split}.txt"
        samples = []
        
        if split_path.exists():
            with open(split_path, 'r') as f:
                for line in f:
                    line = line.strip()
                    # Skip comments and empty lines
                    if line and not line.startswith('#'):
                        samples.append(line.split(',')[0])  # Get video_id
        else:
            print(f"Warning: Split file not found at {split_path}")
        
        return samples
    
    def __len__(self) -> int:
        """Return number of samples in the dataset"""
        return len(self.samples)
    
    def __getitem__(self, idx: int) -> Dict:
        """
        Get a sample from the dataset
        
        Args:
            idx: Sample index
            
        Returns:
            Dictionary containing sample data
        """
        video_id = self.samples[idx]
        
        # Get video annotation
        video_info = self.video_annotations[
            self.video_annotations['video_id'] == video_id
        ].iloc[0].to_dict() if len(self.video_annotations) > 0 else {}
        
        # Get frame annotations for this video
        frame_info = self.frame_annotations[
            self.frame_annotations['video_id'] == video_id
        ] if len(self.frame_annotations) > 0 else pd.DataFrame()
        
        return {
            'video_id': video_id,
            'video_info': video_info,
            'frame_annotations': frame_info,
            'class': video_info.get('class', -1),
            'class_name': video_info.get('class_name', 'unknown')
        }
    
    def get_class_distribution(self) -> Dict[str, int]:
        """Get distribution of classes in the current split"""
        distribution = {class_name: 0 for class_name in self.CLASS_NAMES}
        
        for sample in self.samples:
            video_info = self.video_annotations[
                self.video_annotations['video_id'] == sample
            ]
            if len(video_info) > 0:
                class_name = video_info.iloc[0]['class_name']
                if class_name in distribution:
                    distribution[class_name] += 1
        
        return distribution
    
    def get_statistics(self) -> Dict:
        """Get dataset statistics"""
        stats = {
            'total_samples': len(self.samples),
            'split': self.split,
            'class_distribution': self.get_class_distribution(),
            'total_frames': len(self.frame_annotations),
            'total_videos': len(self.video_annotations)
        }
        
        return stats
    
    def print_statistics(self):
        """Print dataset statistics"""
        stats = self.get_statistics()
        
        print(f"\n{'='*50}")
        print(f"Dataset Statistics - {self.split.upper()} Split")
        print(f"{'='*50}")
        print(f"Total Samples: {stats['total_samples']}")
        print(f"Total Videos: {stats['total_videos']}")
        print(f"Total Frames: {stats['total_frames']}")
        print(f"\nClass Distribution:")
        for class_name, count in stats['class_distribution'].items():
            percentage = (count / stats['total_samples'] * 100) if stats['total_samples'] > 0 else 0
            print(f"  {class_name:25s}: {count:3d} ({percentage:5.2f}%)")
        print(f"{'='*50}\n")


class DatasetValidator:
    """Validate dataset integrity and quality"""
    
    def __init__(self, dataset_root: str):
        self.dataset_root = Path(dataset_root)
        self.config = DatasetConfig(dataset_root)
    
    def validate_structure(self) -> Dict[str, bool]:
        """Validate directory structure"""
        checks = {
            'root_exists': self.dataset_root.exists(),
            'videos_dir_exists': self.config.videos_path.exists(),
            'images_dir_exists': self.config.images_path.exists(),
            'annotations_dir_exists': self.config.annotations_path.exists(),
            'splits_dir_exists': self.config.splits_path.exists(),
        }
        
        return checks
    
    def validate_annotations(self) -> Dict[str, bool]:
        """Validate annotation files"""
        checks = {
            'video_annotations_exist': (self.config.annotations_path / 'video_annotations.csv').exists(),
            'frame_annotations_exist': (self.config.annotations_path / 'frame_annotations.csv').exists(),
            'bounding_boxes_exist': (self.config.annotations_path / 'bounding_boxes.json').exists(),
            'keypoints_exist': (self.config.annotations_path / 'keypoints.json').exists(),
        }
        
        return checks
    
    def validate_splits(self) -> Dict[str, bool]:
        """Validate split files"""
        checks = {
            'train_split_exists': (self.config.splits_path / 'train.txt').exists(),
            'val_split_exists': (self.config.splits_path / 'val.txt').exists(),
            'test_split_exists': (self.config.splits_path / 'test.txt').exists(),
        }
        
        return checks
    
    def run_full_validation(self) -> Dict:
        """Run all validations"""
        results = {
            'structure': self.validate_structure(),
            'annotations': self.validate_annotations(),
            'splits': self.validate_splits()
        }
        
        return results
    
    def print_validation_report(self):
        """Print validation report"""
        results = self.run_full_validation()
        
        print(f"\n{'='*50}")
        print("Dataset Validation Report")
        print(f"{'='*50}")
        
        for category, checks in results.items():
            print(f"\n{category.upper()}:")
            for check_name, passed in checks.items():
                status = "✓ PASS" if passed else "✗ FAIL"
                print(f"  {check_name:30s}: {status}")
        
        # Overall summary
        all_checks = [check for checks in results.values() for check in checks.values()]
        total = len(all_checks)
        passed = sum(all_checks)
        
        print(f"\n{'='*50}")
        print(f"Overall: {passed}/{total} checks passed")
        print(f"{'='*50}\n")


def create_sample_splits(dataset_root: str, train_ratio: float = 0.7, val_ratio: float = 0.15):
    """
    Create train/val/test splits from video annotations
    
    Args:
        dataset_root: Root directory of dataset
        train_ratio: Ratio for training set (default: 0.7)
        val_ratio: Ratio for validation set (default: 0.15)
    """
    config = DatasetConfig(dataset_root)
    
    # Load video annotations
    annotations_file = config.annotations_path / 'video_annotations.csv'
    if not annotations_file.exists():
        print(f"Error: Video annotations not found at {annotations_file}")
        return
    
    df = pd.read_csv(annotations_file)
    
    # Shuffle the data
    df = df.sample(frac=1, random_state=42).reset_index(drop=True)
    
    # Calculate split indices
    n_total = len(df)
    n_train = int(n_total * train_ratio)
    n_val = int(n_total * val_ratio)
    
    # Split the data
    train_df = df[:n_train]
    val_df = df[n_train:n_train + n_val]
    test_df = df[n_train + n_val:]
    
    # Write split files
    for split_name, split_df in [('train', train_df), ('val', val_df), ('test', test_df)]:
        split_file = config.splits_path / f'{split_name}.txt'
        with open(split_file, 'w') as f:
            f.write(f"# {split_name.upper()} Set - {len(split_df)} samples\n")
            f.write("# Format: video_id,filename,class\n\n")
            for _, row in split_df.iterrows():
                f.write(f"{row['video_id']},{row['filename']},{row['class']}\n")
    
    print(f"Created splits:")
    print(f"  Train: {len(train_df)} samples")
    print(f"  Val: {len(val_df)} samples")
    print(f"  Test: {len(test_df)} samples")


def main():
    """Example usage"""
    # Set your dataset root directory
    dataset_root = "dataset"
    
    # Validate dataset
    print("Validating dataset...")
    validator = DatasetValidator(dataset_root)
    validator.print_validation_report()
    
    # Load dataset
    print("\nLoading training dataset...")
    train_dataset = SwimSafeDataset(dataset_root, split='train')
    train_dataset.print_statistics()
    
    # Get a sample
    if len(train_dataset) > 0:
        sample = train_dataset[0]
        print("\nSample data:")
        print(f"Video ID: {sample['video_id']}")
        print(f"Class: {sample['class_name']}")
        print(f"Video Info: {sample['video_info']}")


if __name__ == "__main__":
    main()
