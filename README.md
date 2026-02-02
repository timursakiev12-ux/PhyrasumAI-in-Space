# PhyrasumAI-in-Space
Space-AI MVP for adaptive infrastructure design: generates robust energy, water, and logistics networks under uncertainty and node failures.

## Problem
Future space colonization requires robust infrastructure systems, including energy, water, logistics, and communication networks.  
On Earth, many efficient infrastructure pathways emerged through long-term adaptation rather than rigid upfront planning, gradually optimizing themselves through repeated use and environmental feedback.

In space, this evolutionary process is absent. Infrastructure must be designed in advance under highly uncertain and changing conditions, where failures are costly and physical reconfiguration is extremely limited.  
Rigid optimization models struggle in such environments, highlighting the need for a fundamentally different approach to infrastructure design.

## Solution
We propose a non-traditional solution inspired by how adaptive networks emerge in living systems. *Physarum polycephalum* is evolutionarily optimized to form efficient and resilient transport networks under resource constraints, noise, and changing conditions.

Instead of using Physarum as a metaphor, we collected large-scale experimental data from hundreds of controlled network-formation experiments and used it to train an AI model.  
PhysarumAI learns probabilistic rules of adaptive network formation directly from data and applies them to the design of resilient space infrastructure networks capable of functioning under uncertainty and node failures.

## Experimental Data and Dataset Collection
PhysarumAI is built on a proprietary experimental dataset collected in controlled conditions.

**Dataset collection pipeline:**

1. **Experimental setup**  
   Experiments are conducted in Petri dishes with an agar substrate. A predefined spatial configuration of resource points is placed inside each dish.  
   *Physarum polycephalum* is placed at the center and forms a living transport network composed of tubular structures.  
   Each configuration is repeated **10 to 18 independent times** to capture network variability. Final network images are recorded on days **3–4** of growth.

2. **Image processing**  
   Network images are processed in ImageJ and converted into binary format for standardized analysis.

3. **Graph construction**  
   Binary images are transformed into graph representations describing nodes and connections.

4. **Adjacency matrices**  
   For each experiment, an adjacency matrix is generated representing the presence of connections between nodes.

5. **General matrix**  
   Adjacency matrices from all repeats of the same configuration are aggregated into a general matrix reflecting connection frequencies.

6. **Probability matrix**  
   A probability matrix is derived from the general matrix, indicating how often each connection appears across identical experimental configurations.

**The experimental database contains:**
- experiment ID;  
- repeat number;  
- coordinates and spatial layout of resource points;  
- probability adjacency matrix;  
- distance matrix between nodes.

### Why this matters
This approach allows the AI model to learn from distributions of real network structures rather than single deterministic solutions, capturing adaptive behavior observed in physical systems.

## MVP
The current MVP is implemented in **Wolfram Mathematica** and represents a functional AI prototype for adaptive infrastructure network design and analysis.

At its core, the MVP uses a trained neural network with **four input parameters** that predicts the probability of connections between nodes.  
The model is trained on the experimental dataset and serves as the computational core of the system.

Two applied software modules are built on top of the trained model:

### 1. Network generation for new node configurations
Users can define node locations, select a probability threshold, and generate an adaptive network.  
This module demonstrates how the AI forms stable and alternative connections using probabilistic logic rather than rigid optimization.  
*(Interactive interface in development.)*

### 2. Analysis of real experimental data
The system allows direct exploration of the experimental database by selecting an experiment ID and adjusting the probability threshold to visualize real networks formed in physical experiments.  
This module is used for model validation and demonstrates consistency between AI-generated networks and observed experimental structures.

The MVP is focused on demonstrating adaptive network design principles and does not require deployment or a graphical user interface. All computations are performed locally.

## Data (Zenodo)
The AI model is trained and evaluated using an experimental dataset hosted on Zenodo.

- **Dataset source:** Zenodo (DOI: [TBD](https://doi.org/10.5281/zenodo.18411398))  
- **Data type:** photo, binary images, network graphs, adjacency matrices, probability matrices  
- **Access:** external download (data not stored in this repository)

A helper script for downloading the dataset will be provided in `scripts/download_data.py`.

## How to Run (Local)
The MVP runs locally in **Wolfram Mathematica**.

1. Install Wolfram Mathematica (version 13 or later recommended).  
2. Download the experimental dataset (CSV files) from Zenodo.  
3. Place the CSV files into the `data/` directory.  
4. Open the provided Wolfram notebook (`.nb`).  
5. Execute the notebook cells to load the trained model, select experiment IDs or define new node configurations, set probability thresholds, and visualize the resulting networks.
