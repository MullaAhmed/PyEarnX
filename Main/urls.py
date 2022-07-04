from django.urls import path,include
from .views import *
from rest_framework import routers


urlpatterns = [
    path("projectform/",ProjectFormApiView.as_view(),name="Form Create"),
    path("listprojectform/",ProjectFormListApiView.as_view(),name="Form Create"),
    path("projectform/<slug:project_name>/",ProjectFormDetailApiView.as_view(),name="Form Create"),

    ]