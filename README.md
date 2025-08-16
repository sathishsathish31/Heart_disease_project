❤️ Heart Disease Prediction using Django & Machine Learning

This project is a web-based application that predicts the likelihood of heart disease based on medical input data. It combines Machine Learning (KNN Model) with Django framework to provide an interactive and user-friendly prediction system.


---

🚀 Features

🔹 Machine Learning Integration

Built with K-Nearest Neighbors (KNN) Algorithm.

Uses 8 medical input features (such as age, cholesterol, blood pressure, etc.).

Provides accurate predictions whether a person is at risk of Heart Disease.


🔹 Django Web Application

User-friendly interface built with HTML, CSS, and animations for smooth experience.

Dynamic prediction form to input patient details.

Result page with styled animations to display prediction outcome clearly.


🔹 Static & Informative Pages

Home Page – Overview of the project.

About Page – Explains the project, ML model, and use cases.

Result Page – Displays prediction results with animations.


🔹 Mobile Friendly

The app can run on mobile devices (via local IP address).

Responsive design with CSS styles for better accessibility.


🔹 GitHub Integration

Structured project files for easy deployment.

Clean and reusable code.



---

🛠️ Tech Stack

Frontend: HTML, CSS, JavaScript (with animations)

Backend: Django (Python)

Machine Learning: Scikit-learn (KNN Classifier)

Database: SQLite (default Django database)

Version Control: Git & GitHub



---

📂 Project Structure

heart_prediction/
│── manage.py
│── db.sqlite3
│── requirements.txt
│── README.md
│
├── heart_app/                  # Django App
│   ├── templates/              # HTML Files (home, about, result)
│   ├── static/                 # CSS, JS, Images
│   ├── views.py                # Handles logic & ML model
│   ├── urls.py                 # Routes
│   └── models.py               # Database models
│
├── ml_model/                   # ML files
│   ├── knn_model.pkl           # Trained KNN model
│   └── preprocessing.py        # Data preparation


---

⚙️ How to Run

1. Clone the repository



git clone https://github.com/sathishsathish31/heart_prediction.git
cd heart_prediction

2. Create and activate virtual environment



python -m venv venv
venv\Scripts\activate   # On Windows
source venv/bin/activate  # On Mac/Linux

3. Install dependencies



pip install -r requirements.txt

4. Run the server



python manage.py runserver

5. Open in browser



http://127.0.0.1:8000/


---

📊 Input Features Explanation

Feature	Description

Age	Age of the person
Sex	Gender (Male/Female)
Chest Pain Type	Type of chest pain (4 categories)
Resting BP	Resting blood pressure
Cholesterol	Serum cholesterol in mg/dl
Fasting Blood Sugar	>120 mg/dl (1 = true; 0 = false)
Resting ECG	Electrocardiographic results
Max HR	Maximum heart rate achieved



---

🎯 Future Enhancements

Add more ML models (Random Forest, Logistic Regression).

Deploy the project on Heroku / Render / PythonAnywhere for online access.

Add user authentication (Login/Register) to save predictions.

Visualize predictions with charts (Power BI or Chart.js).



---

👨‍💻 Author

Sathees Kumar K

💼 Aspiring Data Analyst & Frontend Developer

🌟 Interested in ML, Data Analytics, and Web Development

🔗 LinkedIn:[https://www.linkedin.com/in/sathees-kumar-k-23b3aa354]| GitHub:[GitHub:https://github.com/sathishsathish31] 
Email:[sathishkumar63800@gmail.com] | [6380094770]  
  



---
