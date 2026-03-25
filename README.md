# FUTURE_ML_01

# 📊 Sales Forecasting using Machine Learning

## 🚀 Project Overview

This project focuses on predicting future sales using historical transaction data.
It involves data preprocessing, feature engineering, and building a machine learning model to forecast upcoming sales trends.

---

## 🎯 Objectives

* Analyze historical sales data
* Perform data cleaning and preprocessing
* Extract useful time-based features
* Build a forecasting model
* Visualize actual vs predicted sales

---

## 🛠️ Technologies Used

* Python 🐍
* Pandas
* NumPy
* Matplotlib
* Scikit-learn

---

## 📂 Dataset

The dataset contains transaction-level sales data with features such as:

* Invoice Date
* Quantity
* Price
* Total Sales

---

## ⚙️ Steps Performed

### 1. Data Loading

* Loaded dataset using Pandas

### 2. Data Cleaning

* Handled missing values
* Converted date column to datetime format

### 3. Feature Engineering

Extracted:

* Year
* Month
* Day
* Day of Week
* Hour

---

### 4. Data Aggregation

* Grouped data into **daily sales**

---

### 5. Model Building

* Used **Linear Regression**
* Features used:

  * Time index
  * Month
  * Day of week

---

### 6. Forecasting

* Predicted future sales for user-defined number of days

---

### 7. Visualization

* Plotted:

  * Actual Sales
  * Forecasted Sales

---

## 📈 Output

* Line graph showing:

  * Historical sales (blue)
  * Forecasted sales (orange dashed)

---

1. Clone the repository:
git clone https://github.com/Kanishk-32/FUTURE_ML_01.git

2. Navigate to project folder:
cd FUTURE_ML_01

3. Install dependencies:
pip install pandas numpy matplotlib scikit-learn openpyxl

4. Run the script:
python main.py

Make sure the dataset file (data.xlsx) is in the same folder as main.py.

## 📌 Future Improvements

* Use advanced models (ARIMA, Prophet, LSTM)
* Add Streamlit frontend
* Improve accuracy with more features

---

## 💡 Key Learnings

* Time series data handling
* Feature engineering techniques
* Machine learning model building
* Data visualization

---

## 👨‍💻 Author

**Kanishk Gupta**

---

## ⭐ If you like this project

Give it a star on GitHub ⭐
