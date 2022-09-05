import json
from uuid import uuid4
from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
# now time to make the models for the polls

class Option(models.Model):
    parent = models.ForeignKey("Poll", on_delete=models.CASCADE)
    text = models.CharField(max_length=200, blank=True, null=True)
    identifier = models.UUIDField(default=uuid4(), blank=True, null=True)
    
    @property
    def votes(self):
        votes = Vote.objects.filter(option = self)#Option.vote_set.all()
        return votes
    
    def count(self):
        votes = Vote.objects.filter(option = self)#Option.vote_set.all()
        return len(votes)

    def __str__(self) -> str:
        return self.text
    
class Poll(models.Model):
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE , null=True, blank=True, related_name="author")
    title = models.CharField(max_length=200, blank=True, null=True)
    question = models.TextField(blank=True, null=True)
    identifier = models.UUIDField(default=uuid4(), blank=True, null=True)
    @property
    def options(self):
        return Option.objects.filter(parent = self)
        
    def __str__(self) -> str:
        return self.title
    

class Vote(models.Model):
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, blank=True, null=True)
    option = models.ForeignKey(Option, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.author.email if self.author != None else "Vote" + str(self.id)