from django.urls import path
from django.views.generic import TemplateView
from django.shortcuts import HttpResponse


def index(request):
    return HttpResponse("This is the first end point testing connections")

urlpatterns = [
    path("", index, name="index")
]