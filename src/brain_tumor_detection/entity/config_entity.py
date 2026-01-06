from dataclasses import dataclass
from pathlib import Path
from typing import List


@dataclass
class DataIngestionConfig:
    root_dir: Path
    dataset_dir: Path


@dataclass
class DataValidationConfig:
    root_dir: Path
    segmentation_images: Path
    segmentation_masks: Path


@dataclass
class DataTransformationConfig:
    root_dir: Path
    image_size: List[int]
