from .forms import UserForm
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from accounts.models import MyUser

# Create your views here.
def create_user(request):
    user_creation_form = UserForm()
    context = {"form": user_creation_form}
    return render(request, "accounts/index.html", context)


class CreateUser(APIView):
    def post(self, request):
        email = request.POST["email"]
        password = request.POST["password"]
        print(email)
        print(password)
        user = MyUser.objects.create_user(email, password=password)
        if user:
            return Response(get_user_token(request.user))
        else:
            return Response({"default": "Did not work"})


def get_user_token(user):
    refresh = RefreshToken.for_user(user)
    return {
        'refresh': str(refresh),
        'access':str(refresh.access_token)
    }