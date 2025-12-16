import os
import sys
import yaml
import pickle
from box import ConfigBox
from ensure import ensure_annotations
from pathlib import Path

from brain_tumor_detection.exception.exception import BrainTumorException
from brain_tumor_detection.logging.logger import logger


@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """Reads yaml file and returns ConfigBox"""
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"YAML file loaded successfully: {path_to_yaml}")
            return ConfigBox(content)
    except Exception as e:
        raise BrainTumorException(e, sys)


@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """Create list of directories"""
    try:
        for path in path_to_directories:
            os.makedirs(path, exist_ok=True)
            if verbose:
                logger.info(f"Directory created at: {path}")
    except Exception as e:
        raise BrainTumorException(e, sys)


@ensure_annotations
def save_bin(data, path: Path):
    """Save binary file"""
    try:
        with open(path, "wb") as file:
            pickle.dump(data, file)
            logger.info(f"Binary file saved at: {path}")
    except Exception as e:
        raise BrainTumorException(e, sys)


@ensure_annotations
def load_bin(path: Path):
    """Load binary file"""
    try:
        with open(path, "rb") as file:
            data = pickle.load(file)
            logger.info(f"Binary file loaded from: {path}")
            return data
    except Exception as e:
        raise BrainTumorException(e, sys)
