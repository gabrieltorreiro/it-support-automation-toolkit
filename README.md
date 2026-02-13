# IT Support Automation Toolkit

This repository contains Python scripts designed to automate common technical support tasks.  
The goal is to improve efficiency, reduce manual work, and standardize troubleshooting routines.

These scripts simulate real-world IT support scenarios and demonstrate practical automation skills.

---

## 📌 Project Objective

In technical support environments, repetitive tasks such as system checks, backups, and network diagnostics consume time and increase the risk of human error.

This toolkit provides simple automation scripts to:

- Perform system health checks
- Run network diagnostics
- Automate folder backups

All scripts are built using Python standard libraries.

---

## 🛠 Technologies Used

- Python 3
- os
- shutil
- datetime
- subprocess
- platform
- psutil
- socket

---

## 📂 Scripts Overview

### 1️⃣ backup_automation.py

Automates folder backups by:

- Creating a timestamped backup folder
- Copying all files and subfolders
- Preserving file metadata
- Handling basic errors

#### Example Use Case:
Used to back up user directories before system maintenance or OS reinstallation.

---

### 2️⃣ system_health_check.py

Performs a basic system diagnostic by:

- Listing system information
- Checking CPU usage
- Checking RAM usage
- Checking disk space
- Listing top running processes by CPU Usage

#### Example Use Case:
Quick health verification during remote troubleshooting.

---

### 3️⃣ network_diagnostics.py

Runs basic network tests such as:

- Local IP display
- Internet Connectivity
- DNS resolution check
- Ping test

#### Example Use Case:
Diagnosing connectivity issues in support scenarios.

---

## 🚀 How to Run

1. Install Python >= 3.14
2. Clone the repository: git clone https://github.com/gabrieltorreiro/it-support-automation-toolkit.git
3. Install all packages: pip install -r requirements.txt
4. Run the scripts: python system_heath_check.py