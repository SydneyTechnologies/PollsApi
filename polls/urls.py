from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from accounts.views import CreateUser
from .views import CreateOptionApiView, CreatePollApiView, CreateVoteApiView, ListPublicPollsApiView, ListUserPollApiView
from rest_framework.documentation import include_docs_urls

urlpatterns = [
    path("docs/", include_docs_urls(title="POLLS ENDPOINTS")),
    path("create-user", CreateUser.as_view(), name="create"),
    path("create-poll", CreatePollApiView.as_view(), name= "create-poll"),
    path("<str:pollId>/create-option", CreateOptionApiView.as_view(), name= "create-option"),
    path("<str:optionId>/vote", CreateVoteApiView.as_view(), name= "vote"),
    path("list-poll/<str:target>", ListUserPollApiView.as_view(), name= "list-user-poll"),
    path("public-polls/>", ListPublicPollsApiView.as_view(), name= "list"),
    path("obtain", TokenObtainPairView.as_view(), name="obtain"),
    path("obtain/refresh", TokenRefreshView.as_view(), name="refresh"),
]