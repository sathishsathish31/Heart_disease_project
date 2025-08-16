from django.urls import path
from . import views

urlpatterns = [
    path("", views.login_page, name="login"),
    path("register/", views.register_page, name="register"),
    
    path("logout/", views.logout_page, name="logout"),
    path("predict/", views.predict_page, name="predict"),
    path("result/<int:pred>/", views.result_page,name="result"),
    path("about/",views.about_page,name="about")
]