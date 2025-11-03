from setuptools import find_packages, setup

setup(name='Air_Quality_Prediction_and_Forecasting_for_Indian_Cities', version='0.1', packages=find_packages())

import os

project_name = "Air_Quality_Prediction_and_Forecasting_for_Indian_Cities"

# List of directories to create
dirs = [
    f"{project_name}/src/components",
    f"{project_name}/src/pipeline",
    f"{project_name}/src/utils",
    f"{project_name}/artifacts",
    f"{project_name}/notebooks",
    f"{project_name}/app",
    f"{project_name}/config",
    f"{project_name}/tests",
    f"{project_name}/mlflow",
    f"{project_name}/.github/workflows"
]

# List of files to create with optional initial content
files = {
    f"{project_name}/src/components/__init__.py": "",
    f"{project_name}/src/pipeline/__init__.py": "",
    f"{project_name}/src/utils/__init__.py": "",
    f"{project_name}/src/__init__.py": "",
    f"{project_name}/config/__init__.py": "",
    f"{project_name}/tests/__init__.py": "",
    f"{project_name}/.github/workflows/ci-cd.yml": "# GitHub Actions CI/CD pipeline\n",
    f"{project_name}/src/components/data_ingestion.py": "# Handles data ingestion\n",
    f"{project_name}/src/components/data_transformation.py": "# Handles preprocessing and feature engineering\n",
    f"{project_name}/src/components/model_trainer.py": "# Handles model training logic\n",
    f"{project_name}/src/components/model_evaluation.py": "# Handles model evaluation metrics\n",
    f"{project_name}/src/pipeline/training_pipeline.py": "# Pipeline for training\n",
    f"{project_name}/src/pipeline/prediction_pipeline.py": "# Pipeline for prediction\n",
    f"{project_name}/src/utils/logger.py": "# Logging setup\n",
    f"{project_name}/src/utils/exception.py": "# Custom exception handling\n",
    f"{project_name}/app/main.py": "# FastAPI or Flask app entry point\n",
    f"{project_name}/config/config.yaml": "# Configuration parameters\n",
    f"{project_name}/mlflow/mlflow_tracking_setup.py": "# MLflow experiment tracking setup\n",
    f"{project_name}/tests/test_data_ingestion.py": "# Unit tests for data ingestion\n",
    f"{project_name}/tests/test_model_trainer.py": "# Unit tests for model trainer\n",
    f"{project_name}/notebooks/EDA.ipynb": "",
    f"{project_name}/notebooks/model_experiments.ipynb": "",
    f"{project_name}/Dockerfile": "FROM python:3.10-slim\nWORKDIR /app\nCOPY . .\nRUN pip install -r requirements.txt\nCMD [\"python\", \"app/main.py\"]\n",
    f"{project_name}/requirements.txt": "# Add dependencies here\npandas\nnumpy\nscikit-learn\nfastapi\nuvicorn\nmlflow\nxgboost\nprophet\n",
    f"{project_name}/setup.py": f"from setuptools import find_packages, setup\n\nsetup(name='{project_name}', version='0.1', packages=find_packages())\n",
    f"{project_name}/.gitignore": "__pycache__/\n*.pyc\n.env\nartifacts/\nlogs/\nmlruns/\n",
    f"{project_name}/README.md": f"# {project_name}\n\nEnd-to-end ML project for Air_Quality_Prediction_and_Forecasting_for_Indian_Cities.\n"
}

# Create directories
for d in dirs:
    os.makedirs(d, exist_ok=True)

# Create files
for file_path, content in files.items():
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)

print(f"✅ Project structure for '{project_name}' created successfully!")
