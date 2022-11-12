from django.urls import path

from . import views

app_name = "hprc"

urlpatterns = [
    path("", views.index, name="index"),
    path("sponsors/", views.sponsors, name="sponsors"),
    path("sponsors/package", views.sponsorpackage, name="sponsorpackage"),
    path("media/apr22", views.apr22, name="apr22"),
    path("media/mar22", views.mar22, name="mar22"),
    path("media/feb22", views.feb22, name="feb22"),
    path("media/decjan22", views.decjan22, name="decjan22"),
    path("media/nov21", views.nov21, name="nov21"),
    path("media/oct21", views.oct21, name="oct21"),
    path("media/sept21", views.sept21, name="sept21"),
    path("media/april21", views.april21, name="april21"),
    path("media/may21", views.may21, name="may21"),
    path("present/", views.present, name="present"),
    path("presentposters/", views.presentposters, name="presentposters"),
    path("construction", views.construction, name="construction"),
    path("donate", views.donate, name="donate"),
    path("team", views.team, name="team"),
    path("media", views.media, name="media"),
    path("capricornus", views.capricornus, name="capricornus"),
    path("aquila", views.aquila, name="aquila"),
    path("sirius", views.sirius, name="sirius"),
    path("goddard", views.goddard, name="goddard"),
    path("GOATS", views.goats, name="goats"),
    path("contact", views.contact, name="contact"),
]
