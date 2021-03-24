from django.urls import path

from . import views

app_name = "hprc"

urlpatterns = [
    path("", views.index, name="index"),
    path("sponsors/", views.sponsors, name="sponsors"),
    path("sponsors/package", views.sponsorpackage, name="sponsorpackage"),
    path("construction", views.construction, name="construction"),
    path("team", views.team, name="team"),
    path("sirius", views.sirius, name="sirius"),
    path("goddard", views.goddard, name="goddard"),
    path("GOATS", views.goats, name="goats"),
]
