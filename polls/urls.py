from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from accounts.views import CreateUser
from .views import CreateOptionApiView, CreatePollApiView, CreateVoteApiView, ListPollApiView

urlpatterns = [
    path("create-user", CreateUser.as_view(), name="create"),
    path("create-poll", CreatePollApiView.as_view(), name= "create-poll"),
    path("<str:pollId>/create-option", CreateOptionApiView.as_view(), name= "create-option"),
    path("<str:optionId>/vote", CreateVoteApiView.as_view(), name= "vote"),
    path("list-poll/<str:target>", ListPollApiView.as_view(), name= "list-poll"),
    path("obtain", TokenObtainPairView.as_view(), name="obtain"),
    path("obtain/refresh", TokenRefreshView.as_view(), name="refresh"),
]