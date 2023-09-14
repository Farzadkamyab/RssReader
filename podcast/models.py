from django.db import models
from main.models import BaseModel
from author.models import PodcastAuthor, EpisodeAuthor

#--PODCAST--#
class Category(BaseModel):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Owner(BaseModel):
    name = models.CharField(max_length=50)
    email = models.EmailField(null=True, blank=True)

    def __str__(self):
        return f"{self.id}: {self.name}"