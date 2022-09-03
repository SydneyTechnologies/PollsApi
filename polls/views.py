import email
from typing import List
from django.shortcuts import render
from . models import Option, Poll
from rest_framework.generics import CreateAPIView, ListAPIView, UpdateAPIView
from .serializers import PollSerializer, OptionSerializer, VoteSerializer

# Create your views here.
class CreatePollApiView(CreateAPIView):
    model = Poll
    serializer_class = PollSerializer

class CreateOptionApiView(CreateAPIView):
    model = Poll
    serializer_class = OptionSerializer

    def perform_create(self, serializer):
        option_parent = Option.objects.get(id = self.kwargs["poll-id"])
        if option_parent:
            serializer.save(parent = option_parent)
        return super().perform_create(serializer)

class ListPollApiView(ListAPIView):
    model = Poll
    serializer_class = PollSerializer

    def get_queryset(self):
        result = Poll.objects.filter(author__email = self.kwargs["target"])
        return result


