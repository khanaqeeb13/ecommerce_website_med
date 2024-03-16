from django.urls import path
from . import views

urlpatterns = [
    path("0", views.sexual_wellness),
    path("4/", views.food_bevarges),
    path("9/", views.full_body_care),
    path("7/", views.paper_wipes),
    path("6/", views.pain_relif),
    path("1/", views.aryuveda),
    path("5/", views.homepathy),
    path("3/", views.drinks),
    path("2/", views.baby_products),
    path("8/", views.pet_supplies),
]
