from django.urls import path
from django.shortcuts import render
from . forms import UserForm
from .views import create_user, CreateUser

urlpatterns = [
    # this should have a user creation
    # editing user feature like forgot password
    # amongst other view
    path("create-user", CreateUser.as_view(), name= "create"),

]