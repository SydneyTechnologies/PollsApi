from . models import Option, Poll, Vote
from rest_framework.generics import CreateAPIView, ListAPIView
from .serializers import PollSerializer, OptionSerializer, VoteSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .permissions import IsOwnerOrReadOnly

# Create your views here.
class CreatePollApiView(CreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    model = Poll
    serializer_class = PollSerializer

    def perform_create(self, serializer):
        if self.request.user.is_authenticated:
            serializer.save(author = self.request.user)
        return super().perform_create(serializer)

class CreateOptionApiView(CreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    model = Poll
    serializer_class = OptionSerializer
    queryset = Poll.objects.all()

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

class ListUserPollApiView(ListAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    model = Poll
    serializer_class = PollSerializer

    def get_queryset(self):
        result = Poll.objects.filter(author__email = self.kwargs["target"])
        return result

class ListPublicPollsApiView(ListAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Poll.objects.filter(public=True)
    serializer_class = PollSerializer

