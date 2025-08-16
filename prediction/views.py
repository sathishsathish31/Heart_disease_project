import pickle
import numpy as np
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages

# Load your trained model (make sure it's in BASE_DIR or give full path)
#model = pickle.load(open("hot.pkl", "rb"))
model_path = 'prediction/ml_model/heart.pkl'
with open(model_path, 'rb') as file:
    model = pickle.load(file)
    

# ------------------- PREDICT PAGE -------------------
def predict_page(request):
    if request.method == "POST":
        try:
            fields = [
                'age','sex','cp','trestbps','chol','fbs',
                'restecg','thalach','exang','oldpeak','slope','ca','thal'
            ]
            vals = [float(request.POST[f]) for f in fields]
            input_data = np.array([vals])
            prediction = model.predict(input_data)[0]

            # redirect to result page with prediction
            return redirect("result", pred=prediction)

        except Exception as e:
            messages.error(request, f"Error: {str(e)}")
    return render(request, "predict.html")
    

def result_page(request, pred):
    # You can map prediction to a user-friendly message
    if int(pred) == 1:
        message = "⚠️ High Risk of Heart Disease"
    else:
        message = "✅ Low Risk of Heart Disease"
    
    return render(request, "result.html", {"prediction": pred, "message": message})

# ------------------- REGISTER PAGE -------------------
def register_page(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken")
        else:
            user = User.objects.create_user(username=username, password=password)
            user.save()
            messages.success(request, "Registration successful! Please login.")
            return redirect("login")
    return render(request, "register.html")

# ------------------- LOGIN PAGE -------------------
def login_page(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("predict")
        else:
            messages.error(request, "Invalid username or password")
    return render(request, "login.html")

# ------------------- LOGOUT PAGE -------------------
def logout_page(request):
    logout(request)
    return redirect("login")
#---------------About Page----------------------------
def about_page(request):
    return render(request, "about.html")