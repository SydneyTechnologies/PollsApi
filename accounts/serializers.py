from . models import MyUser
from rest_framework.serializers import ModelSerializer

class UserSerializer(ModelSerializer):
    class Meta:
        model = MyUser
        fields = ["email", "password"]