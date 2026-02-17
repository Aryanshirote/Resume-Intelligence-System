from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name ="home"),
    path("login/", views.login, name="login"), 
    path("dasboard", views.dashboard, name ="dashboard")    
    # path('about/', views.about, name="about_us")
]