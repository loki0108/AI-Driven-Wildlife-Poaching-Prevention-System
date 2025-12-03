# Module 2: Search-Based Ranger and Drone Patrol Routing

## Overview
This module implements a search-based patrol routing system for navigating a 5×5 wildlife reserve grid. The model computes optimal routes for a ranger or drone to reach an alert location, with edge weights influenced by environmental factors such as weather, season, thermal activity, poaching density, migration paths, and high-risk zones.

## Problem Addressed
Patrol teams must reach alert zones efficiently while accounting for environmental risks and terrain-related traversal costs. This module finds the cost-optimal route using classical search algorithms.

## Methodology
- Constructed a 5×5 grid graph with 25 nodes (N0–N24).
- Dynamic edge weights computed using:
  - time of day, weather, season,
  - thermal propagation from alert node,
  - poaching density,
  - migration corridor penalties,
  - high-risk zone multipliers,
  - drone vs. ranger traversal adjustments.
- Implemented two search algorithms:
  - Uniform Cost Search (UCS)
  - A* Search using Manhattan Distance (admissible & consistent heuristic).
- Generated optimal paths, total costs, and node-expansion metrics for both algorithms.

## How the Code Works
- Builds the grid graph and assigns all environmental weight multipliers.
- Prompts user for conditions (time, weather, mode, alert node, etc.).
- Computes and displays:
  - the optimal path,
  - the total cost,
  - the number of nodes expanded.
- Compares UCS vs. A* performance.
- Produces a final grid visualization with edge weights and chosen path.

## Key Outputs
- Optimal route from ranger base to alert node.
- Path cost and node-expansion statistics for both UCS and A*.
- Validation of Manhattan heuristic admissibility.
- Final grid visualization showing weighted edges and optimal patrol route.

## Individual Contributions
- **Lokesh Lingam:** Developed grid structure and weight model, implemented UCS with node-expansion tracking, documented UCS behavior.
- **Rahul Dewangan:** Developed grid and weight model, implemented A* with heuristic justification, documented A* and comparative analysis.

## How to Run
1. Ensure you have Python 3 installed.
2. Navigate to the Module 2 folder.
3. Run the notebook or script (depending on your file): jupyter notebook patrol_routing.ipynb