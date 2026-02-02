"""
PhysarumAI dataset is hosted on Zenodo.
https://doi.org/10.5281/zenodo.18411398

Please download the CSV files from Zenodo and place them into the 'data/' directory.

Expected data format:
- adjacency matrices
- probability matrices
- node coordinates
- distance matrices
"""
import os

DATA_DIR = "data"

if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)
