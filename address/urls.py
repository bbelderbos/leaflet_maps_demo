from django.urls import path
from . import views

urlpatterns = [
    path("pick-address/", views.pick_address, name="pick_address"),
    path("pick-address/save/", views.save_address, name="address_save"),
]
