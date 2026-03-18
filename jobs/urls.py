from django.urls import path
from . import views

urlpatterns = [
    path('<int:pk>/', views.job_detail, name='job_detail'),
]
