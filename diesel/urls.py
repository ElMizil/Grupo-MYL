from django.urls import path
from . import views

urlpatterns = [
    path("diesel/nuevo/", views.diesel_create, name="diesel_create"),
    path("diesel/", views.diesel_list, name="diesel_list"),
]
