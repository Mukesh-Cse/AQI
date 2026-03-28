#  Air Quality Index (AQI) Prediction System  
 

---

## Project Overview  
This project builds a **complete machine learning pipeline** to predict Air Quality Index (AQI) categories using historical pollution data. It transforms raw environmental data into actionable insights and a deployable application.

Unlike basic ML projects, this system goes beyond model training by including **data preprocessing, multi-model evaluation, feature analysis, and real-time prediction via a Streamlit web app**.

---

##  Problem Statement  
Air pollution is a major global issue, but traditional AQI calculation methods are static and fail to capture complex pollutant interactions.


---
##  Project Structure  


```
AQI-Prediction-System/
├── README.md
├── city_day.csv
├── notebook.ipynb
├── app.py
├── model.pkl
├── requirements.txt
├── AQI Report.pdf
└── images/
├── heatmap.png
├── feature_importance.png
├── confusion_matrix.png
```

##  Workflow  

1. Data Collection 
2. Data Cleaning & Preprocessing  
3. Exploratory Data Analysis  
4. Model Training (Multiple Algorithms)  
5. Model Evaluation & Comparison  
6. Feature Importance Analysis  
7. Deployment using Streamlit  


---

## Key Implementations  

###  Data Processing
- Handled missing values using **SimpleImputer (mean strategy)**  
- Encoded AQI categories using **LabelEncoder**  
- Removed irrelevant columns (City, Date)  
- Applied **feature scaling (StandardScaler)** for SVM & Logistic Regression  

###  Model Development
Implemented and compared multiple classifiers:
- Logistic Regression  
- Random Forest Classifier  
- Support Vector Machine (SVM)  
- K-Nearest Neighbors (KNN)  

### Model Evaluation
- Accuracy, Precision, Recall, F1-score  
- Confusion Matrix visualization  
- Comparative performance analysis  

**Best Model:** Random Forest (~82% accuracy)

###  Feature Insights
- PM2.5 and PM10 identified as most influential features  
- Correlation analysis performed between pollutants  

### Deployment 
- Built a **Streamlit web application**
- Users can upload `.csv / .xlsx` files  
- Model predicts AQI categories instantly  
- Downloadable prediction results  

---

##  Tech Stack  

- **Language:** Python 3.7  
- **Libraries:**  
  - pandas, numpy  
  - scikit-learn  
  - matplotlib, seaborn  
  - joblib  
  - streamlit  

- **Tools:**  
  - Jupyter Notebook  
  - VS Code  


---

## Results & Insights  

- Random Forest achieved highest accuracy (~82%)  
- Ensemble models outperformed linear models  
- PM2.5, PM10 strongly influence AQI levels  
- Confusion matrices show strong multi-class classification performance  


---



## How to Run  

```bash
# Clone repository
git clone https://github.com/your-username/AQI-Prediction-System.git

# Navigate to project
cd AQI-Prediction-System

# Install dependencies
pip install -r requirements.txt

# Run Streamlit app
streamlit run app.py
