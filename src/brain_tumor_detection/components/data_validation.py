import os
import cv2
from pathlib import Path

from brain_tumor_detection.logging.logger import logging
from brain_tumor_detection.exception.exception import BrainTumorException
from brain_tumor_detection.entity.config_entity import DataValidationConfig


class DataValidation:
    def __init__(self, config: DataValidationConfig):
        self.config = config

    def validate_segmentation_data(self):
        try:
            logging.info("Validating segmentation dataset")

            images = sorted(os.listdir(self.config.segmentation_images))
            masks = sorted(os.listdir(self.config.segmentation_masks))

            assert len(images) > 0, "No segmentation images found"
            assert len(images) == len(masks), "Image-mask count mismatch"

            for img, msk in zip(images, masks):
                img_path = self.config.segmentation_images / img
                mask_path = self.config.segmentation_masks / msk

                if cv2.imread(str(img_path)) is None:
                    raise ValueError(f"Corrupt image: {img}")

                if cv2.imread(str(mask_path), cv2.IMREAD_GRAYSCALE) is None:
                    raise ValueError(f"Corrupt mask: {msk}")

            logging.info("Segmentation validation passed")

        except Exception as e:
            raise BrainTumorException(e, sys)
