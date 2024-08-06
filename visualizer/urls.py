# analysis/urls.py
from django.urls import path
from . import views

app_name = 'visualizer'

urlpatterns = [
    path('', views.upload_file, name='upload'),
    path('results/<int:pk>/', views.file_analysis, name='results'),
]
