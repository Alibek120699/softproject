from django.urls import path, include
from main import views

urlpatterns = [
    path('projects/', views.show_projects),
]