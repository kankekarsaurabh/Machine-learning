
---

## 📊 Exploratory Data Analysis (EDA)

### 🔍 Objective
To consolidate, clean, and visualize a diverse dataset collected from 49 student participants—covering surveys, smartphone-based passive sensing, and real-time EMAs (Ecological Momentary Assessments).

### 📌 Data Sources

- **EMA (Ecological Momentary Assessments)**  
  In-the-moment data on:
  - Stress & mood  
  - Academic & social activities  
  - Physical activity & well-being  

- **Surveys**  
  - PHQ-9 (Depression)  
  - Big Five Personality  
  - Flourishing & Loneliness Scales  
  - PANAS (Positive/Negative Affect)  

- **Passive Sensing**  
  - Activity: walking, running, stationary  
  - Audio: silence, voice, noise  
  - Screen time, phone lock/unlock, charging  
  - Communication: calls, SMS  
  - App usage  
  - Location: home, academic, dining  

- **Academic Info**  
  Class schedule, grades, deadlines

### ⚙️ Notebook Workflow (`DataSet_Creation_and_EDA.ipynb`)
- Parses and maps EMA definitions
- Cleans and aggregates survey & sensor data
- Engineering of features like:
  - Total conversation duration
  - Daily activity breakdown
  - Sleep proxy via phone usage
- Creates a unified daily-level DataFrame per student
- Early visualizations (e.g., PHQ-9 histogram)

---

## 💤 Sleep Quality Prediction: Model Creation & Analysis

### 🎯 Goal
To predict binary **sleep quality** ("Not Poor Sleep" vs "Poor Sleep") using a RandomForest classifier and compare it with other models like XGBoost and SVM.

### ⚙️ Notebook Workflow (`modelcreation.ipynb`)
- Loads cleaned data from `master_daily_data_cleaned_for_sleep_model.csv`
- Defines binary target: `sleep_quality_binary`
- Chooses features on:
  - Screen time  
  - Sensor-based activity  
  - PHQ-9 score  
  - Social interaction  
  - Location patterns  

#### ✅ Models Trained
- RandomForest (with class_weight='balanced')
- Logistic Regression
- Support Vector Machine (SVM)
- XGBoost

#### 🧠 Feature Engineering
- `sedentary_ratio`  
- `academic_to_social_ratio`  
- `stress_x_screentime` interaction

#### 📊 Model Interpretation
- **Permutation Importance**
- **Partial Dependence & ICE Plots**

### 🏆 Key Insights

- **PHQ-9 Score**: Strongest predictor of sleep quality  
- **Sedentary Time**: Higher inactivity → poorer sleep  
- **Social Interaction**: More conversations → better sleep  
- **Screen Time**: Higher screen time → worse sleep  
- **Location Balance**: Home vs. academic place imbalance → signal poor sleep

---

## 🚀 Artifacts for Deployment

Stored in `/models/` directory for integration with a Streamlit app:

- `sleep_model.joblib`: Final RandomForest model  
- `scaler.joblib`: StandardScaler for feature normalization  
- `label_encoder.joblib`: Encodes target labels  
- `feature_columns.json`: Model’s expected features

---

## 🧑‍💻 Getting Started

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/student-wellbeing-sleep-prediction.git
   cd student-wellbeing-sleep-prediction
