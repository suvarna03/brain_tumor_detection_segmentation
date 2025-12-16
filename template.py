import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s')

project_name = "brain_tumor_detection"

list_of_files = [
    ".github/workflows/main.yaml",

    "config/config.yaml",
    "params.yaml",

    "research/01_data_ingestion.ipynb",
    "research/02_data_validation.ipynb",
    "research/03_data_transformation.ipynb",
    "research/04_classification.ipynb",
    "research/05_segmentation.ipynb",
    "research/06_model_evaluation.ipynb",

    f"src/{project_name}/__init__.py",

    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",

    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/components/data_ingestion.py",
    f"src/{project_name}/components/data_validation.py",
    f"src/{project_name}/components/data_transformation.py",
    f"src/{project_name}/components/classification_trainer.py",
    f"src/{project_name}/components/segmentation_trainer.py",
    f"src/{project_name}/components/model_evaluation.py",

    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/entity/config_entity.py",

    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",

    f"src/{project_name}/exception/__init__.py",
    f"src/{project_name}/exception/exception.py",

    f"src/{project_name}/logging/__init__.py",
    f"src/{project_name}/logging/logger.py",

    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/pipeline/stage_01_data_ingestion.py",
    f"src/{project_name}/pipeline/stage_02_data_validation.py",
    f"src/{project_name}/pipeline/stage_03_data_transformation.py",
    f"src/{project_name}/pipeline/stage_04_classification_trainer.py",
    f"src/{project_name}/pipeline/stage_05_segmentation_trainer.py",
    f"src/{project_name}/pipeline/stage_06_model_evaluation.py",
    f"src/{project_name}/pipeline/prediction.py",

    "app.py",
    "main.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "README.md",
    "LICENSE"
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filepath.parent.mkdir(parents=True, exist_ok=True)

    if not filepath.exists():
        filepath.touch()
        logging.info(f"Created: {filepath}")

print("✅ Brain Tumor Detection project structure created successfully!")
