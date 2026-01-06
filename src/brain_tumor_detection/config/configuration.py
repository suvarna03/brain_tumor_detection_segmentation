from pathlib import Path

from brain_tumor_detection.utils.common import read_yaml, create_directories
from brain_tumor_detection.entity.config_entity import (
    DataIngestionConfig,
    DataValidationConfig,
    DataTransformationConfig,
    ClassificationConfig,
    SegmentationConfig,
)

CONFIG_FILE_PATH = Path("config/config.yaml")
PARAMS_FILE_PATH = Path("params.yaml")


class ConfigurationManager:
    def __init__(
        self,
        config_filepath=CONFIG_FILE_PATH,
        params_filepath=PARAMS_FILE_PATH,
    ):
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)

        create_directories([self.config.artifacts_root])

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion
        create_directories([config.root_dir])

        return DataIngestionConfig(
            root_dir=Path(config.root_dir),
            dataset_name=config.dataset_name,
            source=config.source,
            kaggle_dataset=config.kaggle_dataset,
        )

    def get_data_validation_config(self) -> DataValidationConfig:
        config = self.config.data_validation
        create_directories([config.root_dir])

        return DataValidationConfig(
            root_dir=Path(config.root_dir)
        )

    def get_data_transformation_config(self) -> DataTransformationConfig:
        config = self.config.data_transformation
        create_directories([config.root_dir])

        return DataTransformationConfig(
            root_dir=Path(config.root_dir),
            image_size=config.image_size,
        )

    def get_classification_config(self) -> ClassificationConfig:
        config = self.config.classification
        create_directories([config.root_dir])

        return ClassificationConfig(
            root_dir=Path(config.root_dir),
            model_name=config.model_name,
        )

    def get_segmentation_config(self) -> SegmentationConfig:
        config = self.config.segmentation
        create_directories([config.root_dir])

        return SegmentationConfig(
            root_dir=Path(config.root_dir),
            model_name=config.model_name,
        )
