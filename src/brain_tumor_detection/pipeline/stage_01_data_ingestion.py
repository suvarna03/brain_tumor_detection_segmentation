from brain_tumor_detection.config.configuration import ConfigurationManager
from brain_tumor_detection.components.data_ingestion import DataIngestion
from brain_tumor_detection.logging.logger import logging


STAGE_NAME = "Data Ingestion Stage"


class DataIngestionPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()

        data_ingestion = DataIngestion(data_ingestion_config)
        data_ingestion.download_dataset()


if __name__ == "__main__":
    try:
        logging.info(f">>>>>> {STAGE_NAME} started <<<<<<")
        obj = DataIngestionPipeline()
        obj.main()
        logging.info(f">>>>>> {STAGE_NAME} completed <<<<<<\n")

    except Exception as e:
        logging.exception(e)
        raise e
