from django.urls import path
from grocery import views 

urlpatterns = [
    path('grocery/', views.clothing, name="grocery")
    ]