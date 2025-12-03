# AI-Driven Wildlife Poaching Prevention System  
**Group 7 — M.Tech CSE, IIT Bhubaneswar**

This repository contains the complete implementation of our **5-module AI system** designed for intelligent wildlife-protection operations in a 500 km² Central India reserve.  
Each module is contained in its own folder, with a **README**, **code**, and **report**.

This file explains **where to find everything**, how to run each part, and how the modules connect.

---

## Repository Structure

AI-Driven Wildlife Poaching Prevention System/
│
├── Module1/ → Bayesian Network for Poaching Risk Estimation
├── Module2/ → Search-Based Ranger & Drone Patrol Routing
├── Module3/ → Automated Planning (POP & GraphPlan)
├── Module4/ → MDP + Reinforcement Learning for Patrol Allocation
├── Module5/ → LLM-Based Operational Briefing (Prompt Engineering)
├── PDF report
└── README.md ← (this file)


Each module folder contains:
- **Code / Notebook**
- **Module-specific README**
- **Module Report (PDF)**

---

## Quick Guide for the Professor

Below is a simple navigation guide for evaluation.

---

### **▶ Module 1 — Bayesian Network Risk Estimation**
**Folder:** `/Module1/`  
**Files to check:**
- `module1_report.pdf`
- `main.py`
- `README.md`  
**What it contains:**  
Probabilistic model predicting poaching risk using terrain, time, human movement, historical density, and hotspot proximity.

---

### **▶ Module 2 — Search-Based Patrol Routing (UCS & A*)**
**Folder:** `/Module2/`  
**Files to check:**
- `patrol_routing.ipynb` or `module2.py`
- `module2_report.pdf`
- `README.md`  
**What it contains:**  
5×5 grid, dynamic edge weights, UCS/A* algorithms, heuristic admissibility, and path visualization.

---

### **▶ Module 3 — Automated Planning (POP & GraphPlan)**
**Folder:** `/Module3/`  
**Files to check:**
- `module3.py`
- `Module3_Report.pdf`
- `README.md`  
**What it contains:**  
POP causal-link planning and GraphPlan mutex-based planning for multi-alert deployment.

---

### **▶ Module 4 — Decision Making using MDP & Reinforcement Learning**
**Folder:** `/Module4/`  
**Files to check:**
- `patrol_env.py`
- `oliver_mdp_baseline.py`
- `shanmuga_qlearning.py`
- `module4_report.pdf`
- `README.md`  
**What it contains:**  
MDP model, baseline patrol policy, Q-learning agent, environment simulator, and performance comparison.

---

### **▶ Module 5 — LLM-Based Operational Briefing**
**Folder:** `/Module5/`  
**Files to check:**
- `module5_report.pdf`
- `README.md`  
**What it contains:**  
Prompt engineering to convert outputs from Modules 1–4 into ranger-ready intelligence reports.

---

## ▶ How to Run the Project (Summary)

Every module has its own **How to Run** section inside its folder.  
Here is a short master summary:

### **Module 1**

cd Module1
python3 main.py


### **Module 2**

cd Module2
python3 module2.py

or open the notebook:

jupyter notebook


### **Module 3**
Requires graphviz:

pip install graphviz networkx matplotlib
cd Module3
python3 module3.py


### **Module 4**

cd Module4
python3 oliver_mdp_baseline.py
python3 shanmuga_qlearning.py


### **Module 5**
No execution — documentation only.

---

## 👥 Group Members (Group 7)

- Chetan — 25CS06003  
- Khem Singh — 25CS06004  
- Lingam Lokesh — 25CS06005  
- Oliver Kandir — 25CS06006  
- Peta Shanmuga Teja — 25CS06007  
- Rahul Dewangan — 25CS06008  
- Bikram Shahi — 25CS06010  
- Konisa Sai Sriyuktha — 25CS06016  
- Seepana Mithun — 25CS06019  
- Singi Maharshi — 25CS06021  

---