import email
from django.shortcuts import render
from . models import Option, Poll, Vote
from accounts.models import MyUser
from rest_framework.generics import CreateAPIView, ListAPIView, UpdateAPIView
from .serializers import PollSerializer, OptionSerializer, VoteSerializer

# Create your views here.
class CreatePollApiView(CreateAPIView):
    model = Poll
    serializer_class = PollSerializer

    def perform_create(self, serializer):
        if self.request.user.is_authenticated:
            serializer.save(author = self.request.user)
        return super().perform_create(serializer)

class CreateOptionApiView(CreateAPIView):
    model = Poll
    serializer_class = OptionSerializer

    def perform_create(self, serializer):
        poll = Poll.objects.get(identifier = self.kwargs["pollId"])
        if poll:
            serializer.save(parent = poll)
        return super().perform_create(serializer)

class CreateVoteApiView(CreateAPIView):
    model = Vote
    serializer_class = VoteSerializer

    def perform_create(self, serializer):
        option = Option.objects.get(identifier = self.kwargs["optionId"])
        if option:
            serializer.save(parent = option)
        return super().perform_create(serializer)

class ListPollApiView(ListAPIView):
    model = Poll
    serializer_class = PollSerializer

    def get_queryset(self):
        result = Poll.objects.filter(author__email = self.kwargs["target"])
        return result


