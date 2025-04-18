# 🧪 Yeast Gene Expression: Predicting Synthetic Titer
A mini research-style project that simulates the prediction of protein titer based on gene expression data from yeast. This project mimics real-world fermentation R&D workflows — similar to those used in biotech applications like precision fermentation.

---

## 🔍 Project Objective

To explore the feasibility of predicting protein titer using gene expression data from the [UCI Yeast Dataset](https://archive.ics.uci.edu/dataset/110/yeast). Since the dataset does not contain a real titer value, we simulate a synthetic continuous target using biologically-inspired linear combinations.

This project mirrors goals similar to fermentation R&D labs like **Oobli**, where understanding signal in strain/process data can improve yield forecasting and optimization.

---

## 📦 Dataset

- **Source**: UCI Machine Learning Repository — Yeast Dataset (ID: 110)
- **Features**: 8 numerical biological features (e.g., `gvh`, `mcg`, `mit`, etc.)
- **Target**: Simulated protein titer, generated using a weighted sum + noise model

---

## 🔬 Workflow

1. **Data Loading & Cleaning**
   - Loaded yeast gene expression features via `ucimlrepo`
   - Dropped low-variance columns (`erl`)
   - Log-transformed skewed features (`mit`, `nuc`)

2. **Exploratory Data Analysis (EDA)**
   - Pairplots, boxplots, and heatmaps to understand feature distributions
   - Identified multicollinearity (e.g., `mcg` vs `gvh`) and skewness

3. **Target Simulation**
   - Simulated titer using `y = X @ weights + noise`
   - Ensured realistic variance and biological interpretation

4. **Model Training**
   - Linear Regression (R²: ~0.785)
   - Random Forest Regressor (R²: ~0.742)
   - Performance evaluated via RMSE and R²

5. **Feature Importance**
   - Extracted from Random Forest model
   - `gvh`, `mit`, and `mcg` were the most predictive features

---

## 📈 Results Summary

| Model              | R² Score | RMSE   |
|--------------------|----------|--------|
| Linear Regression  | 0.785    | 0.200  |
| Random Forest      | 0.742    | 0.219  |

- **Linear regression outperformed** Random Forest due to the synthetic target's linear nature.
- **Top predictors**: `gvh`, `mit`, `mcg`
- **Low-importance features**: `pox`, `nuc`, `vac`

---

## 🧰 Tools & Technologies

- Python, pandas, NumPy
- scikit-learn, seaborn, matplotlib
- ucimlrepo (for UCI dataset import)

---

## 📚 Use Case Inspiration

This project simulates a real R&D setting where predictive modeling is used to:
- Evaluate whether meaningful signals exist in historical strain/bioprocess data
- Identify influential variables before launching production-grade models
- Lay the groundwork for optimization in strain design or yield forecasting

---

## 📁 Repository Structure

