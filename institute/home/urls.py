from django.urls import path
from . import views
from . import home_view_example as home_example
app_name = "home"

urlpatterns = [
    path("", home_example.HomeView.as_view(), name="home"),
]
