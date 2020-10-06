from django.urls import path
from . import views

urlpatterns = [
    path('', views.workout_menu, name="workout_menu")
] 
