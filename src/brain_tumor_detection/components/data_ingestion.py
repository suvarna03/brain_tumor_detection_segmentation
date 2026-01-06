import os
import shutil
import kagglehub
from pathlib import Path

from brain_tumor_detection.logging.logger import logging
from brain_tumor_detection.exception.exception import BrainTumorException 
from brain_tumor_detection.entity.config_entity import DataIngestionConfig


class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def download_dataset(self):
        try:
            logging.info("Starting dataset download from Kaggle")

            dataset_path = kagglehub.dataset_download(
                self.config.kaggle_dataset
            )

            dataset_path = Path(dataset_path)
            target_dir = self.config.root_dir

            if target_dir.exists():
                shutil.rmtree(target_dir)

            shutil.copytree(dataset_path, target_dir)

            logging.info(f"Dataset downloaded successfully at: {target_dir}")

        except Exception as e:
            raise CustomException(e)
