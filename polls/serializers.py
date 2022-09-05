from rest_framework.serializers import Serializer
from rest_framework.serializers import HyperlinkedModelSerializer, ModelSerializer
from . models import Poll, Option, Vote

class OptionSerializer(ModelSerializer):
    class Meta:
        model = Option
        exclude = ["identifier"]

class PollSerializer(ModelSerializer):
    options = OptionSerializer(many=True, read_only=True)
    class Meta:
        model = Poll
        fields = "__all__"

class VoteSerializer(ModelSerializer):
    class Meta:
        model = Vote
        fields = "__all__"