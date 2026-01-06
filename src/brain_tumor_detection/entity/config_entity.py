from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    dataset_name: str
    source: str
    kaggle_dataset: str


@dataclass(frozen=True)
class DataValidationConfig:
    root_dir: Path


@dataclass(frozen=True)
class DataTransformationConfig:
    root_dir: Path
    image_size: list


@dataclass(frozen=True)
class ClassificationConfig:
    root_dir: Path
    model_name: str


@dataclass(frozen=True)
class SegmentationConfig:
    root_dir: Path
    model_name: str
