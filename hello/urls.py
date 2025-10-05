from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("rohit", views.rohit, name="rohit"),
    path("<str:name>", views.greet, name="greet")
]