# ECSA-2026-ROS2GreenArch
Replication package of the paper submitted to ECSA 2026 as a short paper. On Green ROS 2 Architecture.

This repository contains the replication package, datasets, and supplementary material for the paper:
**"On the Architectural Evolution of ROS 2: Toward Greener Robotics Software Design"** (Submitted to ECSA 2026).

## 🔍 Overview
The Robot Operating System (ROS) is the standard middleware for modern robotics. As many robotic systems are battery-dependent, energy optimization is vital for longer and more reliable missions. This research investigates the architectural evolution of ROS 2 across seven distributions—from **Dashing Diademata** to **Jazzy Jalisco**—to identify design decisions that impact energy efficiency.

## 👥 Researchers Involved

This study was conducted by:

* **[Michel Albonico]([https://michel.iotrixx.com.br/])** – Professor at the Federal Technological University of Paraná (UTFPR).
* **[Maciel Felipe Borges](https://github.com/Macielfborges)** – Professor at the Federal Institute of Paraná (IFPR).
* **[José Augusto Fabri]** – Professor at the Federal Technological University of Paraná (UTFPR).

This research is part of a collaborative effort focused on software engineering and robotics sustainability.


### Key Research Contributions:
* **Systematic Mapping**: A dataset of 386 architectural decisions manually mapped from official documentation and meta-tickets.
* **Green Decisions**: Identification of 44 energy-related design decisions (green decisions) through qualitative analysis.
* **Code Implementation**: Mapping of key Pull Requests (PRs) providing pre- and post-change code versions for further investigation.

---

## 📂 Repository Structure
* `/tools`: Automation scripts used for data mining and code extraction.
  * `extract_meta_tickets.py`: Automated scraper for ROS 2 meta-tickets and documentation to map architectural decisions.
  * `download_pr_versions.py`: Script to retrieve "Before" and "After" code versions from GitHub Pull Requests.
  * `requirements.txt`: List of Python dependencies (e.g., `requests`, `beautifulsoup4`) for the research environment.
* `/dataset`: Contains the spreadsheets with the 386 mapped decisions and the 44 "green decisions".
  * `ros2_distributions.csv`: Analyzed ROS 2 distributions (Dashing to Jazzy).
  * `ros2_architectural_decisions.csv`: Full mapping of 386 architectural decisions.
  * `ros2_green_decisions.csv`: Subset of 44 energy-related (green) decisions.
  * `ros2_code_mapping_prs.csv`: Links to PRs and code versions (Base/Head SHAs).
* `/code`: Source code versions for the identified green decisions:
  * Each subfolder (e.g., `PR 1`, `PR 2`) contains the `before` and `after` versions of the files modified in that specific Pull Request.

---

## 🚀 Reproduction Steps
To replicate the study or use the provided scripts, follow these steps:

1. **Environment Setup**: Install the necessary Python libraries using the requirements file located in the tools folder to ensure all scripts run correctly:
   ```bash
   pip install -r tools/requirements.txt
2. **Decision Review**: Access `/dataset` to view the full mapping of ROS 2 evolution.
3. **Data Extraction**: Run `extract_meta_tickets.py` to identify relevant architectural artifacts.
4. **Code Comparison**: Use `download_pr_versions.py` to retrieve the "before" and "after" code versions for a specific decision.

---

## 📄 How to Cite
If you use this dataset or findings in your research, please cite our ECSA 2026 paper:
*(BibTeX placeholder - To be updated upon paper acceptance)*
