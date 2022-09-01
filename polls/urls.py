from django.urls import path
from django.views.generic import TemplateView
from django.shortcuts import HttpResponse
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


def index(request):
    return HttpResponse("This is the first end point testing connections")

urlpatterns = [
    path("", index, name="index"),
    path("obtain", TokenObtainPairView.as_view(), name="obtain"),
    path("obtain/refresh", TokenRefreshView.as_view(), name="refresh"),
]