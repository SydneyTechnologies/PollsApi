from dataclasses import fields
from rest_framework import serializers
from rest_framework.serializers import HyperlinkedModelSerializer, ModelSerializer
from . models import Poll, Option, Vote


class VoteSerializer(serializers.StringRelatedField):

    class Meta:
        model = Vote
        fields = "__all__"

class OptionSerializer(ModelSerializer):
    count = serializers.IntegerField(read_only=True)
    class Meta:
        model = Option
        exclude = ["parent", "identifier"]


class PollSerializer(ModelSerializer):
    options = OptionSerializer(many=True, read_only=True)
    class Meta:
        model = Poll
        fields = "__all__"


