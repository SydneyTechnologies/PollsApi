from django.urls import path
from django.views.generic import TemplateView
from django.shortcuts import HttpResponse
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from accounts.views import CreateUser

urlpatterns = [
    path("create-user", CreateUser.as_view(), name="create"),
    path("obtain", TokenObtainPairView.as_view(), name="obtain"),
    path("obtain/refresh", TokenRefreshView.as_view(), name="refresh"),
]