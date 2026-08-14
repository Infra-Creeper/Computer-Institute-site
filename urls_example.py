"""
urls.py — Django URL configuration example for the homepage.

Add this to your project's urls.py or create a dedicated app.
"""

from django.urls import path
from . import views

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
]
