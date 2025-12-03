# Module 3: Automated Patrol Planning using POP & GraphPlan

## Overview
This module applies two classical automated planning algorithms—Partial Order Planning (POP) and GraphPlan—to generate optimal deployment strategies for ranger teams and drones when multiple poaching alerts occur simultaneously. Both planners operate on the same wildlife emergency scenario and produce valid, explainable patrol plans.

## Problem Addressed
The system must respond to three high-risk alerts:
- Gunshot-like audio near the riverbed  
- Midnight thermal activity near the elephant corridor  
- Intelligence warning of planned poaching in tiger habitat  

With only two ranger teams and one drone, the goal is to generate a feasible plan that clears all alerts while respecting resource and ordering constraints.

## Methodology

### Partial Order Planning (POP)
- Uses least-commitment strategy and maintains partial ordering.
- Builds causal links between actions and resolves threats via promotion/demotion.
- Supports parallel execution where no ordering is required.
- Produces a flexible action structure suitable for real-time operations.

### GraphPlan
- Builds alternating state and action layers of a planning graph.
- Computes explicit mutex (mutual exclusion) relationships.
- Extracts a consistent plan through backward search from the goal state.
- Produces a structured, phase-based execution sequence.

Both planners share:
- The same initial and goal states
- The same domain operators (Analyze, Assign, Patrol/Monitor)

## How the Code Works

### POP Implementation
- Initializes Start and Finish nodes.
- Iteratively resolves open preconditions.
- Inserts operators that produce required effects.
- Detects and resolves threats to causal links.
- Outputs:
  - Number of steps
  - Ordering constraints
  - Causal links
  - POP Graph structure (graphviz)

### GraphPlan Implementation
- Builds multi-level planning graph: S₀ → A₀ → S₁ → A₁ → …  
- Applies mutex checks for both propositions and actions.
- Detects when goals become reachable at a non-mutex state level.
- Performs backward extraction to produce final plan.
- Saves planning graph visualization.

## Key Outputs
- Full POP partial-order plan with causal links.
- Complete GraphPlan sequential plan.
- Planning graph and POP graph images.
- Statistics including:
  - State levels
  - Action levels
  - Mutex relationships
  - Extracted non-NOOP action sequence

## Individual Contributions
- **Konisa Sai Sriyuktha (25CS06016):** Constructed initial/goal states and operators, implemented GraphPlan, generated graph output, and documented GraphPlan.
- **Bikram Shahi (25CS06010):** Constructed initial/goal states and operators, implemented POP, generated POP graph, and documented POP.

## How to Run

### Requirements
- Python 3
- Graphviz installed on your system
- Python packages: pip install graphviz networkx matplotlib
- Navigate to the Module 3 folder:
    - python3 module3.py
    - Outputs will be generated as:
        - wildlife_pop_graph.png
        - wildlife_graphplan_clear.png