from pathlib import Path
from brain_tumor_detection.utils.common import read_yaml, create_directories
from brain_tumor_detection.entity.config_entity import (
    DataIngestionConfig,
    DataValidationConfig,
    DataTransformationConfig
)


class ConfigurationManager:
    def __init__(
        self,
        config_filepath=Path("config/config.yaml"),
        params_filepath=Path("params.yaml")
    ):
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)

        create_directories([self.config.artifacts_root])

    # ------------------ DATA INGESTION ------------------
    def get_data_ingestion_config(self) -> DataIngestionConfig:
        ingestion = self.config.data_ingestion

        dataset_dir = Path(
            ingestion.root_dir
        ) / ingestion.dataset_name

        create_directories([dataset_dir])

        return DataIngestionConfig(
            root_dir=Path(ingestion.root_dir),
            dataset_dir=dataset_dir
        )

    # ------------------ DATA VALIDATION ------------------
    def get_data_validation_config(self) -> DataValidationConfig:
        ingestion_root = self.config.data_ingestion.root_dir
        dataset = self.config.data_ingestion.dataset_name

        segmentation_images = Path(
            ingestion_root
        ) / dataset / "segmentation_task/train/images"

        segmentation_masks = Path(
            ingestion_root
        ) / dataset / "segmentation_task/train/masks"

        create_directories([self.config.data_validation.root_dir])

        return DataValidationConfig(
            root_dir=Path(self.config.data_validation.root_dir),
            segmentation_images=segmentation_images,
            segmentation_masks=segmentation_masks
        )

    # ------------------ DATA TRANSFORMATION ------------------
    def get_data_transformation_config(self) -> DataTransformationConfig:
        return DataTransformationConfig(
            root_dir=Path(self.config.data_transformation.root_dir),
            image_size=self.config.data_transformation.image_size
        )
