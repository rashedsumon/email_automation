"""
data_loader.py
Automatically download the Enron email dataset from KaggleHub into ./data/
Usage:
    python data_loader.py
"""

import os
import kagglehub

# Create data folder if not exists
os.makedirs("data", exist_ok=True)

# Download latest version of the Enron dataset
dataset_path = kagglehub.dataset_download("wcukierski/enron-email-dataset", extract=True)

print("Path to dataset files:", dataset_path)
