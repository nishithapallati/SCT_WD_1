# 🏠 House Price Prediction Using Machine Learning and Flask

A web-based House Price Prediction application built using **Linear Regression**, **Flask**, and the **Kaggle House Prices Dataset**. The application predicts house prices based on living area, number of bedrooms, and number of bathrooms, and displays the predicted value in both **USD ($)**.

---

## 📌 Project Overview

This project uses a **Linear Regression Machine Learning model** to estimate house prices. The model is trained on the Kaggle House Prices dataset and deployed through a Flask web application that allows users to enter property details and instantly receive a predicted house price.

---

## 🚀 Features

- Predict house prices using Machine Learning
- User-friendly Flask web interface
- Linear Regression model implementation
- Displays predicted price in:
  - US Dollars ($)
- Model trained using real-world housing data
- Responsive and clean UI

---

## 🛠️ Technologies Used

### Frontend
- HTML5
- CSS3

### Backend
- Python
- Flask

### Machine Learning
- Scikit-Learn
- Linear Regression

### Data Processing
- Pandas
- NumPy

### Dataset
- Kaggle House Prices Dataset

---

## 📊 Dataset

The model is trained using the Kaggle House Prices dataset.

Selected features:

| Feature | Description |
|----------|------------|
| GrLivArea | Above-ground living area (square feet) |
| BedroomAbvGr | Number of bedrooms |
| FullBath | Number of bathrooms |
| SalePrice | Target variable (house price) |

---

## 🧠 Machine Learning Workflow

1. Load Dataset
2. Data Preprocessing
3. Feature Selection
4. Train-Test Split
5. Train Linear Regression Model
6. Save Model using Pickle
7. Deploy Model with Flask
8. Predict House Prices

---

## 📂 Project Structure

```text
HousePricePrediction/
│
├── app.py
├── train_model.py
├── train.csv
├── house_price_model.pkl
│
├── templates/
│   └── index.html
│
├── static/
│   └── style.css
│
└── requirements.txt
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/your-username/HousePricePrediction.git

cd HousePricePrediction
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🏋️ Train the Model

```bash
python train_model.py
```

This creates:

```text
house_price_model.pkl
```

---

## ▶️ Run the Application

```bash
python app.py
```

Open your browser and visit:

```text
http://127.0.0.1:5000
```

---

## 🎥 Demo Video

The project demonstration video can be viewed here:

[Google Drive Link](https://drive.google.com/file/d/1N9PKWAxNy-3UILYho7wHJJ5EQfzBithw/view?usp=sharing)


---

## 📈 Sample Prediction

### Input

```text
Living Area : 2000 sq.ft
Bedrooms    : 3
Bathrooms   : 2
```

### Output

```text
USD : $245,678.90
```

---

## 🎯 Learning Outcomes

Through this project, I gained practical experience in:

- Machine Learning Model Development
- Linear Regression
- Data Preprocessing
- Model Evaluation
- Flask Web Development
- Model Deployment
- Frontend-Backend Integration
- Real-world Dataset Handling

---

## 📚 Future Enhancements

- Support additional housing features
- Improve prediction accuracy using advanced algorithms
- Add graphical data visualizations
- Deploy the application online
- Use live currency conversion rates

---

## 👨‍💻 Author

**Nishitha Pallati**

Machine Learning Internship Project

---

## ⭐ If you found this project useful, consider giving it a star!
