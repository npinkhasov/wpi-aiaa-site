from django.urls import path

from . import views

app_name = "hprc"

urlpatterns = [
    path("", views.index, name="index"),
    path("sponsors/", views.sponsors, name="sponsors"),
    path("sponsors/package", views.sponsorpackage, name="sponsorpackage"),
    path("media/nov21", views.nov21, name="nov21"),
    path("media/oct21", views.oct21, name="oct21"),
    path("media/sept21", views.sept21, name="sept21"),
    path("media/april21", views.april21, name="april21"),
    path("media/may21", views.may21, name="may21"),
    path("construction", views.construction, name="construction"),
    path("donate", views.donate, name="donate"),
    path("team", views.team, name="team"),
    path("media", views.media, name="media"),
    path("aquila", views.aquila, name="aquila"),
    path("sirius", views.sirius, name="sirius"),
    path("goddard", views.goddard, name="goddard"),
    path("GOATS", views.goats, name="goats"),
    path("contact", views.contact, name="contact"),
]
