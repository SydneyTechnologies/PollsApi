from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from accounts.views import CreateUser
from .views import CreatePollApiView, ListPollApiView

urlpatterns = [
    path("create-user", CreateUser.as_view(), name="create"),
    path("create-poll", CreatePollApiView.as_view(), name= "create-poll"),
    path("list-poll/<str:target>", ListPollApiView.as_view(), name= "list-poll"),
    path("obtain", TokenObtainPairView.as_view(), name="obtain"),
    path("obtain/refresh", TokenRefreshView.as_view(), name="refresh"),
]