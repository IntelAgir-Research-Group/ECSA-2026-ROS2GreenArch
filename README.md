# ECSA-2026-ROS2GreenArch
Replication package of the paper submitted to ECSA 2026 as a short paper. On Green ROS 2 Architecture.

This repository contains the replication package, datasets, and supplementary material for the paper:
**"On the Architectural Evolution of ROS 2: Toward Greener Robotics Software Design"** (Submitted to ECSA 2026).

## 🔍 Overview
The Robot Operating System (ROS) is the standard middleware for modern robotics. As many robotic systems are battery-dependent, energy optimization is vital for longer and more reliable missions. This research investigates the architectural evolution of ROS 2 across seven distributions—from **Dashing Diademata** to **Jazzy Jalisco**—to identify design decisions that impact energy efficiency.

### Key Research Contributions:
* **Systematic Mapping**: A dataset of 386 architectural decisions manually mapped from official documentation and meta-tickets.
* **Green Decisions**: Identification of 44 energy-related design decisions (green decisions) through qualitative analysis.
* **Code Implementation**: Mapping of key Pull Requests (PRs) providing pre- and post-change code versions for further investigation.
* **Quality Analysis**: A static analysis dataset generated with **SonarQube** to support the investigation of software quality attributes like maintainability.

---

## 📂 Repository Structure
* `/tools`: Automation scripts used for data mining and code extraction.
* `/dataset`: Contains the spreadsheets with the 386 mapped decisions and the 44 "green decisions".
  * `ros2_distributions.csv`: Analyzed ROS 2 distributions (Dashing to Jazzy).
  * `ros2_architectural_decisions.csv`: Full mapping of 386 architectural decisions.
  * `ros2_green_decisions.csv`: Subset of 44 energy-related (green) decisions.
  * `ros2_code_mapping_prs.csv`: Links to PRs and code versions (Base/Head SHAs).
* `/sonarqube`: Static code analysis results for the considered ROS 2 repository versions.
* `/code`: Metadata and commits for the identified Pull Requests (PRs).
* `/figures`: Distribution charts of architectural decisions by ROS 2 version and category.

---

## 🛠️ Tools & Automation
The `/tools` folder contains Python scripts to support the study's workflow:
* **`extract_meta_tickets.py`**: Scrapes ROS 2 GitHub meta-tickets and documentation to extract issue and Pull Request links.
* **`download_pr_versions.py`**: Automates the download of source code in two states: **Before** (pre-change) and **After** (post-change) for each architectural decision.

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
To replicate the study or use the provided scripts, follow these steps:

1. **Environment Setup**: Install the necessary Python libraries using the requirements file located in the tools folder to ensure all scripts run correctly:
   ```bash
   pip install -r tools/requirements.txt
2. **Decision Review**: Access `/dataset` to view the full mapping of ROS 2 evolution.
3. **Data Extraction**: Run `extract_meta_tickets.py` to identify relevant architectural artifacts.
4. **Code Comparison**: Use `download_pr_versions.py` to retrieve the "before" and "after" code versions for a specific decision.
5. **Quality Metrics**: Consult the `/sonarqube` folder for static analysis reports.

---

## 📄 How to Cite
If you use this dataset or findings in your research, please cite our ECSA 2026 paper:
*(BibTeX placeholder - To be updated upon paper acceptance)*
