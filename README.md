# ECSA-2026-ROS2GreenArch
Replication package of the paper submitted to ECSA 2026 as a short paper. On Green ROS 2 Architecture.

This repository contains the replication package, datasets, and supplementary material for the paper:
**"On the Architectural Evolution of ROS 2: Toward Greener Robotics Software Design"** (Submitted to ECSA 2026).

## 🔍 Overview
The Robot Operating System (ROS) is the standard middleware for modern robotics. As many robotic systems are battery-dependent, energy optimization is vital for longer and more reliable missions. This research investigates the architectural evolution of ROS 2 across seven distributions—from **Dashing Diademata** to **Jazzy Jalisco**—to identify design decisions that impact energy efficiency.

### Key Research Contributions:
* **Systematic Mapping**: A dataset of 386 architectural decisions manually mapped from official documentation and meta-tickets.
* **Green Decisions**: Identification of 44 energy-related design decisions (green decisions) through qualitative analysis.
* **Code Implementation**: Mapping of 17 key Pull Requests (PRs) providing pre- and post-change code versions for further investigation.
* **Quality Analysis**: A static analysis dataset generated with **SonarQube** to support the investigation of software quality attributes like maintainability.

---

## 📂 Repository Structure
* `/tools`: Tools and automation used in the study.
* `/dataset`: Contains the spreadsheets with the 386 mapped decisions and the 44 "green decisions".
* `/sonarqube`: Static code analysis results for the considered ROS 2 repository versions.
* `/code`: Metadata and commits for the identified Pull Requests (PRs).
* `/figures`: Distribution charts of architectural decisions by ROS 2 version and category.

---

## 📊 Classification of Green Decisions
We classify green decisions into categories reflecting distinct mechanisms that influence energy consumption:
1. **Communication and Middleware Configuration**: DDS settings, QoS policies, and transport mechanisms.
2. **Memory Management**: Allocation strategies, buffer handling, and data lifecycle.
3. **Data Management and Logging**: Storage, logging mechanisms, and serialization (e.g., rosbag/SQLite).
4. **Node Architecture and Composition**: Intra-process communication and node structure.
5. **Concurrency and Execution Model**: Multi-threading models, executors, and callback handling.
6. **Tooling and Visualization Support**: Developer tools for diagnosis and system optimization.

---

## 🚀 Reproduction Steps
1. **Decision Review**: Access `/dataset` to view the full mapping of ROS 2 evolution.
2. **Code Extraction**: Use the PR mapping in `/code_base` to retrieve specific code changes (pre- and post-commit).
3. **Quality Metrics**: Consult the `/sonarqube` folder for static analysis reports related to the identified decisions.

---

## 📄 How to Cite
If you use this dataset or findings in your research, please cite our ECSA 2026 paper:
*(BibTeX placeholder - To be updated upon paper acceptance)*
