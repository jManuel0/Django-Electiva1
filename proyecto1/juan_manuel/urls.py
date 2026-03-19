from django.urls import path

from . import views

app_name = "juan_manuel"

urlpatterns = [
    path("", views.index, name="index"),
]
