import os
from pathlib import Path

list_of_files = [
    "data/raw/",
    "data/processed/",
    "notebook/exploratory_data_analysis.ipynb",
    "notebook/model_training.ipynb",
    "notebook/model_evaluation.ipynb",
    "src/data_preprocessing.py",
    "src/train_model.py",
    "src/prediction_script.py",
    "src/utils.py",
    "models/",
    "outputs/",
    "requirements.txt",
    "setup.py"  
]

for file_path in list_of_files:
    path = Path(file_path)
    
    # Check if the path is a folder
    if file_path.endswith('/') or path.suffix == '':
        os.makedirs(path, exist_ok=True)  
    else:
        os.makedirs(path.parent, exist_ok=True)  
        if not path.exists() or path.stat().st_size == 0:
            with open(path, 'w') as f:
                pass  
        else:
            print(f"'{file_path}' already exists and is not empty.")
