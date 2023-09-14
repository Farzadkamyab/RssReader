from django.db import models
from main.models import BaseModel

# Create your models here.
class PodcastAuthor(BaseModel):
    name = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.id}: {self.name}"

class EpisodeAuthor(models.Model):
    name = models.CharField(max_length=30)
    
    def __str__(self):
        return f"{self.id}: {self.name}"
    
