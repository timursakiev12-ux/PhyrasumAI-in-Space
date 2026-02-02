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

## Software Modules

### 1. Network Generation Module
Allows users to:
- define new node configurations;
- apply the trained AI model;
- select probability thresholds;
- generate adaptive network topologies.

This module demonstrates AI-driven network design beyond classical optimization methods.

### 2. Experimental Data Analysis Module
Allows users to:
- select experiment IDs;
- adjust probability thresholds;
- visualize real experimentally observed networks.

This module is used for validation and comparison between AI-generated and observed network structures.

---

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
