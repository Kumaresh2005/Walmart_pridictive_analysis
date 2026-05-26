# Walmart Predictive Sales Analysis using Python & Machine Learning

<p align="center">
  <img src="Screenshot%202026-05-21%20215826.png" width="1000" alt="Walmart Dashboard"/>
</p>

---

## Project Overview

This project focuses on predicting Walmart sales using Machine Learning and Data Analytics techniques. The analysis was performed using Python, Pandas, NumPy, Matplotlib, Seaborn, and Scikit-learn to uncover sales trends, customer behavior, and future sales predictions.

The project demonstrates end-to-end predictive analytics including:

- Data Cleaning
- Exploratory Data Analysis (EDA)
- Feature Engineering
- Machine Learning Model Building
- Sales Prediction
- Data Visualization

---

## Objectives

- Analyze Walmart sales data
- Identify important sales patterns
- Predict future sales using Machine Learning
- Perform exploratory data analysis
- Generate business insights from data
- Build predictive analytics skills

---

## Tools & Technologies Used

| Tool | Purpose |
|------|----------|
| Python | Data Analysis & Machine Learning |
| Pandas | Data Cleaning |
| NumPy | Numerical Operations |
| Matplotlib | Data Visualization |
| Seaborn | Statistical Visualization |
| Scikit-learn | Machine Learning |
| Jupyter Notebook | Development Environment |
| GitHub | Project Hosting |

---

## Dataset Information

The dataset contains Walmart sales-related information such as:

- Store Details
- Weekly Sales
- Holiday Events
- Temperature
- Fuel Price
- CPI
- Unemployment Rate

Dataset File:

```text
Walmart_Sales.csv
```

---

## Project Workflow

```text
Dataset
   ↓
Data Cleaning
   ↓
Exploratory Data Analysis
   ↓
Feature Engineering
   ↓
Machine Learning Model
   ↓
Sales Prediction
   ↓
Visualization & Insights
```

---

## Python Libraries Used

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score
```

---

## Exploratory Data Analysis (EDA)

Performed detailed analysis on:

- Weekly sales trends
- Holiday impact on sales
- Temperature vs Sales
- Fuel price impact
- Unemployment trends
- Store-wise performance

---

## Machine Learning Model

### Model Used

- Linear Regression

### Steps Performed

- Data preprocessing
- Feature selection
- Train-test split
- Model training
- Prediction generation
- Performance evaluation

---

## Model Evaluation Metrics

- Mean Absolute Error (MAE)
- Mean Squared Error (MSE)
- Root Mean Squared Error (RMSE)
- R² Score

---

## Key Business Insights

- Holiday seasons significantly increase sales
- Certain stores consistently outperform others
- Fuel prices and unemployment affect purchasing behavior
- Predictive models can estimate future sales trends

---

## Project Structure

```text
walmart-predictive-analysis/
│
├── README.md
├── Screenshot 2026-05-21 215826.png
├── Walmart_Sales.csv
└── main.py
```

---

## Sample Machine Learning Code

```python
X = df[['Temperature', 'Fuel_Price', 'CPI', 'Unemployment']]
y = df['Weekly_Sales']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = LinearRegression()

model.fit(X_train, y_train)

predictions = model.predict(X_test)
```

---

## Data Visualization Features

- Sales Trend Charts
- Correlation Heatmaps
- Store-wise Sales Analysis
- Holiday Sales Comparison
- Prediction Graphs

---

## Future Improvements

- Add advanced ML algorithms
- Deploy model using Flask or Streamlit
- Create real-time dashboard
- Add deep learning predictions
- Improve model accuracy

---

## Screenshots

### Dashboard Preview

<p align="center">
  <img src="Screenshot%202026-05-21%20215826.png" width="1000"/>
</p>

---

## Author

# Kumaresh Biswas

Aspiring Data Analyst & Machine Learning Enthusiast passionate about:
- Python
- Data Analytics
- Machine Learning
- Power BI
- SQL
- Data Visualization

---

## Connect With Me

- LinkedIn: https://www.linkedin.com/
- GitHub: https://github.com/
- Portfolio: https://kumaresh-portfolio-wmdj.vercel.app/

---

## ⭐ If you like this project, give it a star on GitHub!
