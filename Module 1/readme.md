# Module 1: Bayesian Network for Poaching Risk Estimation

## Overview
This module implements a Bayesian Network (BN) to estimate poaching risk in a wildlife reserve based on environmental and human-activity factors. The model captures how terrain, time of day, historical poaching density, human movement, and wildlife hotspot proximity contribute to the probability of poaching.

## Problem Addressed
Poaching risk depends on uncertain, interrelated factors. This module builds a probabilistic model that can estimate risk levels under different conditions using Bayesian inference.

## Methodology
- Six variables defined: TerrainType, TimeOfDay, HistoricalPoachingDensity, HumanMovement, WildlifeHotspotProximity, and PoachingRisk.
- All five environmental factors independently influence PoachingRisk in the BN structure.
- Priors assigned for each parent node.
- Conditional Probability Table (CPT) for PoachingRisk constructed using representative probability slices.
- Bayesian inference performed for a given evidence set to compute P(PoachingRisk | evidence).
- D-separation properties validated conceptually.

## How the Code Works
- Defines the full Bayesian Network: variable states, priors, and conditional dependencies.
- Computes joint probability contributions for each factor.
- Uses enumeration-based inference to calculate the posterior probability of PoachingRisk.
- Outputs High/Low risk probabilities for the specified evidence.

## Key Outputs
- Posterior probability of PoachingRisk based on input conditions.
- Clear demonstration of how environmental and behavioural factors influence risk.
- Fully reproducible Bayesian reasoning pipeline implemented in pure Python.

## Individual Contributions
- **Khem:** Selected variables, wrote theoretical sections, prepared CPT interpretations, formatted tables, and contributed to conceptual explanation.
- **Mithun:** Constructed CPTs, performed numerical inference calculations, wrote the implementation summary, and validated computational steps.

## How to Run
1. Ensure you have Python 3 installed.
2. Navigate to the Module 1 folder:
3. Run the script: python3 main.py
