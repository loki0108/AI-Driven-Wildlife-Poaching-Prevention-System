# Module 4: Decision Making using MDP & Reinforcement Learning

## Overview
This module models anti-poaching patrol allocation as a **Markov Decision Process (MDP)** and implements a **Reinforcement Learning (RL)** solution using tabular **Q-Learning**. The goal is to optimize ranger and drone deployment in response to alerts, changing poaching risk, and limited resources.

## Problem Addressed
Poaching threats change dynamically across the reserve. Patrol agents must:
- respond to alerts quickly,
- monitor high-risk hotspots,
- conserve limited movement resources,
- maximize prevention of poaching.

This module learns an adaptive patrol policy using RL and compares it with a handcrafted rule-based baseline.

## Methodology
### MDP Formulation
- **State** includes:  
  `alert, risk_level, ranger_position, drone_position, resource_levels`
- **Actions** include:  
  holding position, dispatching ranger to alert, dispatching drone, patrolling hotspot.
- **Transition model** (stochastic):  
  - alerts may trigger,  
  - poaching attempts occur based on risk & time,  
  - resources decrease on movement,  
  - movement success is probabilistic.

### Baseline Patrol Strategy (Rule-Based)
- If alert active → send ranger (or drone if ranger unavailable)
- If no alert & risk high → patrol hotspot
- Else → hold and conserve resources

### Q-Learning Approach
- Learns Q-values through repeated environment interaction.
- ε-greedy exploration with decay.
- Q-update rule:
Q[s,a] ← Q[s,a] + α * (r + γ * max(Q[s'],:) – Q[s,a])

### Experimental Setup
- 300 training episodes  
- 200 evaluation episodes  
- γ = 0.95, α = 0.1  
- ε decays from 0.3 → 0.05  
- Episode length: 30 steps

## How the Code Works
- **patrol_env.py**  
Implements the full MDP environment, reward rules, transitions, and stochastic behaviour.
- **oliver_mdp_baseline.py**  
Implements the rule-based baseline policy and evaluates it.
- **shanmuga_qlearning.py**  
Runs Q-learning, trains the agent, and compares performance with the baseline.

Outputs include:
- Training episode rewards  
- Baseline vs RL average returns  
- Behaviour analysis (alert response times, hotspot coverage, movement efficiency)

## Key Outputs
- RL agent outperforms baseline patrol strategy.
- Learned behaviours include:
- faster response to alerts,
- proactive positioning near hotspots,
- fewer unnecessary movements,
- better use of ranger/drone resources.
- Demonstrates that RL offers measurable performance improvements.

## Individual Contributions
- **Oliver Kandir (25CS06006):**  
Formulated the MDP, built the stochastic environment simulator, created the baseline policy.
- **Peta Shanmuga Teja (25CS06007):**  
Implemented tabular Q-Learning, training loop, ε-greedy exploration, and evaluation pipeline.

## How to Run

### 1. Install dependencies (optional)
If you want to view plots:

pip install matplotlib

### 2. Run the Baseline Policy

python3 oliver_mdp_baseline.py

### 3. Train & Evaluate the Q-Learning Agent

python3 shanmuga_qlearning.py

You will see:
- Baseline average return  
- Learned policy average return  
- Training reward progression