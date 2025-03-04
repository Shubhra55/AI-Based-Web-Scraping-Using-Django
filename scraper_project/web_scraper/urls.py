from django.urls import path
from .views import home, scrape

urlpatterns = [
    path("", home, name="home"),
    path("scrape/", scrape, name="scrape"),
]
