from django.db import models
from main.models import BaseModel
from author.models import PodcastAuthor, EpisodeAuthor

#--PODCAST--#
class Category(BaseModel):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
