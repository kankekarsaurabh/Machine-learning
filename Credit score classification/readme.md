# Credit Score Classification Analysis

**Team Members**: Arpan Banerjee, Saurabh Kankekar, Suyash Mohta

---

## Table of Contents
- [Project Overview](#project-overview)  
- [Business Problem](#business-problem)  
- [Data](#data)  
  - [Data Source](#data-source)  
  - [Key Features & EDA Insights](#key-features--eda-insights)  
  - [Data Cleaning and Transformation](#data-cleaning-and-transformation)  
- [Methodology](#methodology)  
  - [Exploratory Data Analysis (EDA)](#exploratory-data-analysis-eda)  
  - [Model Development](#model-development)  
  - [Model Selection](#model-selection)  
  - [Model Interpretation](#model-interpretation)  
- [Key Findings and Results](#key-findings-and-results)  
- [Conclusion and Value Proposition](#conclusion-and-value-proposition)  
- [Repository Structure](#repository-structure)  
- [Getting Started](#getting-started)  
  - [Prerequisites](#prerequisites)  
  - [Running the Analysis](#running-the-analysis)  
- [Limitations and Future Work](#limitations-and-future-work)  

---

## Project Overview
This project focuses on building a machine learning model to forecast credit scores based on historical financial data. The goal is to classify individuals' creditworthiness into three categories: **Bad**, **Average**, and **Good**. Leveraging Exploratory Data Analysis (EDA) and various classification models, we identify key factors affecting credit scores and select the most accurate predictive model. These insights aim to improve risk evaluation for financial institutions.

---

## Business Problem
Lenders and financial institutions require robust tools to assess credit risk. Traditional models can be opaque and may not capture evolving behaviors. This project aims to:

- Accurately classify credit scores using predictive modeling.
- Support data-driven decision-making for financial institutions.
- Reduce default risks through improved credit risk profiling.
- Increase transparency and adaptability in credit scoring methods.

---

## Data

### Data Source
The dataset includes historical financial data for a group of customers. Each customer initially had multiple records (e.g., monthly), which were aggregated into a single comprehensive profile.

### Key Features & EDA Insights
Key takeaways from EDA:

- **Positive Correlations**:  
  - `Monthly_Inhand_Salary` (correlated with `Annual_Income`)  
  - `Amount_Invested_Monthly`

- **Negative Correlations**:  
  - `Num_of_Delayed_Payment`  
  - `Interest_Rate`  
  - `Outstanding_Debt`

- **Other Important Features**:  
  - `Credit_Mix`, `Payment_of_Min_Amount`, `Credit_History_Age`

A detailed correlation matrix and univariate/bivariate analysis were performed to guide feature selection.

### Data Cleaning and Transformation
- **Aggregation**: Condensed multiple monthly records per customer into a single profile.
- **Imputation**:  
  - Numerical: Mean/median  
  - Categorical: Mode
- **Feature Engineering**: Addressed multicollinearity (e.g., dropped `Annual_Income`).
- **Encoding**: One-hot or label encoding applied to categorical variables.
- **Scaling**: StandardScaler used for numerical features.

---

## Methodology

### Exploratory Data Analysis (EDA)
Conducted to explore data distributions, outliers, feature relationships, and dependencies to inform preprocessing and model development.

### Model Development
Tested various classification models:
- Logistic Regression  
- Gaussian Naive Bayes  
- Support Vector Machine (SVC)  
- Random Forest Classifier  
- Gradient Boosting Classifier

A pipeline combined preprocessing and model training. Hyperparameters were tuned via `GridSearchCV` with `StratifiedKFold`.

### Model Selection
**Random Forest Classifier** was selected for its superior performance across metrics like **F1-Score** and **Cohen's Kappa Score**—particularly important for imbalanced datasets.

### Model Interpretation
- **Feature Importance** from Random Forest
- **Partial Dependence Plots (PDP)** for marginal effects
- **Individual Conditional Expectation (ICE)** plots, including customized ICE visualizations

---

## Key Findings and Results

The best-performing model categorized credit scores accurately. Key predictive factors:

- **Credit Mix**  
- **Payment Timeliness**  
- **Interest Rates**  
- **Outstanding Debt**  
- **Minimum Payment Behavior**  
- **Credit History Age**

Insights such as "lower interest rates and reduced outstanding debt increase the probability of a 'Good' score" were confirmed by interpretability techniques (PDP, ICE).

---

## Conclusion and Value Proposition

The credit scoring model provides:
- **Accurate classification** into credit categories  
- **Actionable insights** for:
  - **Financial Institutions**: Improve lending decisions, reduce defaults
  - **Consumers**: Understand and improve their creditworthiness  

Random Forest’s robustness makes it a reliable baseline for future deployment and refinements.

---

## Repository Structure

# Jupyter Notebook with EDA, preprocessing, modeling
├── credit_score_analysis.ipynb 

├── Final_Report.pdf # Detailed written project report

├── Credit_Score_Presentation.pdf # Slide deck summarizing the project

├── Appendix.pdf # Supplementary charts, plots, and extras

└── readme.md # This README file



---

## Getting Started

### Prerequisites

Make sure Python 3.x and the following libraries are installed:

- pandas  
- numpy  
- scikit-learn  
- matplotlib  
- seaborn  
- jupyterlab or jupyter notebook  

You can install them using pip:

```bash
pip install pandas numpy scikit-learn matplotlib seaborn jupyterlab

