from dataclasses import field
from pyexpat import model
from statistics import mode
from rest_framework.serializers import HyperlinkedModelSerializer, ModelSerializer
from . models import Poll, Option, Vote

class PollSerializer(ModelSerializer):
    class Meta:
        model = Poll
        fields = "__all__"

class OptionSerializer(ModelSerializer):
    class Meta:
        model = Option
        field = "__all__"

class VoteSerializer(ModelSerializer):
    class Meta:
        model = Vote
        fields = "__all__"