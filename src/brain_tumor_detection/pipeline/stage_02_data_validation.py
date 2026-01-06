from brain_tumor_detection.config.configuration import ConfigurationManager
from brain_tumor_detection.components.data_validation import DataValidation
from brain_tumor_detection.logging.logger import logging


class DataValidationPipeline:
    def main(self):
        config = ConfigurationManager()
        validation_config = config.get_data_validation_config()

        validator = DataValidation(validation_config)
        validator.validate_segmentation_data()


if __name__ == "__main__":
    logging.info("Stage 02: Data Validation started")
    DataValidationPipeline().main()
    logging.info("Stage 02: Data Validation completed")
