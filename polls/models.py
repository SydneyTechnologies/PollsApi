from argparse import ONE_OR_MORE
from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
# now time to make the models for the polls
class Poll(models.Model):
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE , null=True, blank=True)
    title = models.CharField(max_length=200, blank=True, null=True)
    question = models.TextField(blank=True, null=True)

    @property
    def get_poll_options(self):
        polls = Poll.option_set.all()
        return polls
    
    def __str__(self) -> str:
        return self.title


class Option(models.Model):
    parent = models.ForeignKey(Poll, on_delete=models.CASCADE)
    text = models.CharField(max_length=200, blank=True, null=True)
    @property
    def get_option_votes(self):
        votes = Option.vote_set.all()
        return len(votes)
    
    total_votes = models.IntegerField(editable=False, default=get_option_votes)
    
    def __str__(self) -> str:
        return self.text
    #def increas

class Vote(models.Model):
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, blank=True, null=True)

    option = models.ForeignKey(Option, on_delete=models.CASCADE)