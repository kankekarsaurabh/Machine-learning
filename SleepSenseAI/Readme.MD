# 📚 Exploratory Data Analysis of Student Life & Well-being

This project presents a comprehensive **Exploratory Data Analysis (EDA)** on a multi-modal dataset collected from 49 student participants. The primary goal is to process, clean, and consolidate various data streams—including **Ecological Momentary Assessments (EMAs)**, **psychological surveys**, and **passive smartphone sensor data**—into unified daily summaries. These summaries enable the exploration of relationships between students' behaviors, contexts, and self-reported well-being.

---

## 📦 Dataset Overview

The dataset integrates multiple sources of information:

### 📝 EMA (Ecological Momentary Assessment)
High-frequency, real-time survey responses collected via smartphone, covering:

- Stress & Mood  
- Social Interactions  
- Academic Activities (Classes, Studying)  
- Exercise and Daily Routines  
- Self-reported Behaviors  

💡 **Reference File:** `EMA_definition.json` — describes all EMA questions and response formats.

### 🧠 Psychological Surveys
Baseline measures of mental health and personality traits:

- **PHQ-9**: Depression Assessment  
- **Big Five Personality Traits**  
- **Flourishing & Loneliness Scales**  
- **PANAS**: Positive and Negative Affect Schedule  

### 📱 Passive Sensing Data
Behavioral data collected via phone sensors:

- **Activity**: Stationary, Walking, Running  
- **Audio**: Silence, Voice, Noise detection  
- **Location**: Semantic categories via Wi-Fi/GPS (e.g., home, library, dining)  
- **Phone Status**: Screen activity, lock/unlock events, charging  
- **Communication**: Calls and SMS  
- **App Usage**: Application log data  

### 🎓 Academic Information
Includes class schedules, deadlines, and academic performance metrics.

---

## ⚙️ Project Workflow

Implemented within the notebook: `DataSet_Creation_and_EDA.ipynb`

### 1. Environment Setup
- Import libraries: `pandas`, `numpy`, `seaborn`, `matplotlib`, `glob`, etc.
- Define paths and configurations.

### 2. Initial Exploration
- Traverse the dataset structure.
- Identify and catalog available data per user.

### 3. Data Loading & Preprocessing
- Parse `EMA_definition.json` to interpret response codes.
- Load and clean survey data.
- Compute key psychological scores (e.g., PHQ-9).

### 4. Feature Engineering & Aggregation
- **EMA**: Merge and standardize all user EMA responses.
- **Sensor Data**:
  - Calculate total durations for movement states.
  - Audio exposure breakdown.
  - Phone usage metrics (lock time, dark screen).
  - Time spent at various locations.
- **Rest Estimation**: Infer sleep/rest from phone lock/dark periods.

### 5. Master DataFrame Creation
All features merged into a unified, per-day-per-student format.

### 6. Data Visualization
- Example: Histogram of baseline PHQ-9 scores to illustrate cohort distribution.

---

## 🗂 Repository Structure

📁 dataset/
    ├── 📁 EMA/
    │   └── 📁 response/
    ├── 📁 dinning/
    ├── 📁 calendar/
    ├── 📁 sms/
    ├── 📁 education/
    ├── 📁 call_log/
    ├── 📁 app_usage/
    ├── 📁 sensing/
    │   ├── 📁 wifi/
    │   ├── 📁 gps/
    │   ├── 📁 activity/
    │   ├── 📁 phonelock/
    │   ├── 📁 wifi_location/
    │   ├── 📁 audio/
    │   ├── 📁 bluetooth/
    │   ├── 📁 dark/
    │   ├── 📁 phonecharge/
    │   └── 📁 conversation/
    └── 📁 survey/
        📄 PerceivedStressScale.csv
        📄 panas.csv
        📄 BigFive.csv
        📄 psqi.csv
        📄 FlourishingScale.csv
        📄 LonelinessScale.csv
        📄 vr_12.csv
        📄 PHQ-9.csv

--- Traversal Complete ---
Found 1988 files and 46 sub-folders (excluding the base folder itself in the sub-folder count).

--- Top-level contents of '/Users/saurabhkankekar/jupyter_env/dataset': ---
📁 EMA/
📁 dinning/
📄 .DS_Store
📁 calendar/
📁 sms/
📁 education/
📁 call_log/
📁 app_usage/
📁 sensing/
📁 survey/


##

