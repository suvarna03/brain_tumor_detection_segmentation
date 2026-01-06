from brain_tumor_detection.config.configuration import ConfigurationManager

if __name__ == "__main__":
    config = ConfigurationManager()
    data_ingestion_config = config.get_data_ingestion_config()
    print(data_ingestion_config)

