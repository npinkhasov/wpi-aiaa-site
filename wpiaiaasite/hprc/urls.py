from django.urls import path

from . import views

app_name = "hprc"

urlpatterns = [
    path("", views.index, name="index")
]