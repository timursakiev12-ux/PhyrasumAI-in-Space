# Technical Documentation

## System Overview
PhysarumAI is a data-driven AI system for adaptive infrastructure network design.  
The system combines an experimentally derived dataset with a trained neural network model to generate and analyze probabilistic network topologies under uncertainty.

The MVP is implemented in Wolfram Mathematica and runs entirely locally without external services or deployment.

---

## Architecture
The system consists of three main layers:

1. **Experimental dataset layer**  
   A structured database of experimental network data represented as graphs, adjacency matrices, probability matrices, and distance matrices.

2. **AI model layer**  
   A trained neural network model that predicts the probability of connections between nodes based on input features derived from the dataset.

3. **Application layer**  
   Two analysis and visualization tools built on top of the trained model:
   - network generation for new node configurations;
   - analysis and visualization of real experimental networks.

---

## Experimental Data Representation
Each experiment is represented in tabular form using CSV files and includes:
- experiment ID;
- repeat ID;
- spatial coordinates of nodes;
- adjacency matrices;
- aggregated probability matrices;
- distance matrices between nodes.

Repeated experiments with identical configurations allow probabilistic modeling of network formation rather than deterministic reconstruction.

---

## AI Model
The core AI component is a supervised neural network trained on experimental data.

### Model characteristics:
- **Input:** four numerical features describing node relationships;
- **Output:** probability of connection between node pairs;
- **Training data:** probability matrices derived from repeated experiments;
- **Purpose:** learning probabilistic rules of adaptive network formation.

The model is designed to prioritize robustness and adaptability rather than minimal path length or cost.

---

## Network Generation Logic
Generated networks are constructed by applying a user-defined probability threshold to the predicted connection probabilities.

- High-probability edges represent stable connections;
- Lower-probability edges represent optional or alternative pathways;
- Threshold selection enables scenario-based analysis of network resilience and redundancy.

---

## Software Modules and Scripts

All computational and analytical components of the PhysarumAI MVP are implemented as modular Wolfram Notebook (`.nb`) files and auxiliary scripts. Each file has a clearly defined role, ensuring transparency and reproducibility of the system.

---

### `PhysarumAI_PredictionV1.nb`
**Purpose:**  
Core AI inference module.

**Description:**  
This notebook contains the trained PhysarumAI neural network used to predict the probability of connections between pairs of nodes. The model serves as the computational core for generating adaptive and resilient network topologies based on probabilistic rules learned from experimental data.

---

### `PhysarumAI_V4.1.nb`
**Purpose:**  
Model training and development.

**Description:**  
This notebook is used for training and experimental tuning of the PhysarumAI neural network. It includes data loading, feature preparation, and model training procedures. The file is intended for research and reproducibility and is not required for running the MVP.

---

### `trainedNet4_flow_groupSplit.wlnet`
**Purpose:**  
Serialized trained model.

**Description:**  
A saved neural network model trained on the experimental dataset. It is loaded by `PhysarumAI_PredictionV1.nb` to perform predictions without retraining.

---

### `experimental_data_viewer.nb`
**Purpose:**  
Exploration and visualization of experimental data.

**Description:**  
This tool enables direct interaction with the experimental dataset. Users can select experiment IDs, adjust probability thresholds, and visualize real networks formed in physical experiments. It is used for data analysis and validation of AI-generated networks.

---

### `scripts/download_data.py`
**Purpose:**  
Dataset access helper.

**Description:**  
An auxiliary script indicating that the PhysarumAI dataset is hosted on Zenodo. It creates the local `data/` directory and documents the expected format of CSV files. The script does not perform automatic data downloading and serves reproducibility and project structure clarity.

---

## Data Handling Note
Experimental data are stored externally on Zenodo and are not included in the GitHub repository. This separation ensures proper data versioning, scalability, and compliance with best practices for experimental datasets.

---

## Design Rationale
The separation between model training, inference, experimental data analysis, and dataset storage minimizes hidden assumptions, simplifies validation, and improves reproducibility. This modular architecture supports transparent evaluation by external experts and enables future system extension.


## Technology Stack
- Wolfram Mathematica (core environment)
- Wolfram Neural Networks
- CSV-based data storage
- ImageJ (image preprocessing pipeline)

---

## Limitations and Future Work
Current limitations include:
- 2D spatial layouts;
- limited node counts per configuration;
- local execution only.

Planned extensions include:
- larger-scale node configurations;
- interactive graphical interface;
- integration into space mission simulation environments.

---

## How to Run
See `README.md` for local execution instructions.
