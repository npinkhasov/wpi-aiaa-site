from django.urls import path

from . import views

app_name = "home"

urlpatterns = [
    path("", views.index, name="index"),
    path("subcommittees/", views.subcommittees, name="subcommittees"),
    path("events/", views.events, name="events"),
    path("about/", views.about, name="about"),
    path("jet-engine-proposal/", views.proposal, name="proposal"),
]
