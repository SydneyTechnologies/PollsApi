from django.shortcuts import render,HttpResponse
from .forms import UserForm
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response

# Create your views here.
def create_user(request):
    user_creation_form = UserForm()
    context = {"form": user_creation_form}
    return render(request, "accounts/index.html", context)


class CreateUser(APIView):
    def get(self, request):
        user_creation_form = UserForm()
        context = {"form": user_creation_form}
        return render(request, "accounts/index.html", context)
    def post(self, request):
        user_creation_form = UserForm(request.POST)
        print(user_creation_form.errors)
        if user_creation_form.is_valid():
            user_creation_form.save()
            return Response(get_user_token(request.user))

def get_user_token(user):
    refresh = RefreshToken.for_user(user)
    return {
        'refresh': str(refresh),
        'access':str(refresh.access_token)
    }