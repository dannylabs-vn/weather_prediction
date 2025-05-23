# Weather Prediction Web App 

This project is a simple machine learning-powered web application that predicts the weather condition based on user input: **date**, **precipitation**, **temperature**, and **wind speed**. It uses a `DecisionTreeClassifier` and is built with **Flask**, **scikit-learn**, **Pandas**, and **Bootstrap**.

---

## Features

- Clean, responsive web interface (Bootstrap-based)
- Predicts weather conditions from user inputs
- Preprocessing includes outlier removal, transformation, and encoding
- Live model training on each prediction (can be optimized)
---

## Project Structure
```
weather_web_app/
├── app.py # Flask backend API
├── calculation.py # ML logic and data processing
├── dataset.csv # Original dataset
├── dataset_updated.csv # Extended dataset with recent dates
├── templates/
│ └── index.html # Frontend HTML interface
└── static/
└── style.css # Optional custom styling
```
---

## ML Model

- **Algorithm:** Decision Tree Classifier
- **Preprocessing:**
  - Outlier removal using IQR
  - Square root transformation of `precipitation` and `wind`
  - Date converted to UNIX timestamp
  - Label encoding of `weather`

---

## How to Run

Clone or download the project
```bash
git clone https://github.com/yourusername/weather_web_app.git
cd weather_web_app
pip install flask pandas scikit-learn numpy
python app.py
