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

class Image(BaseModel):
    title = models.CharField(max_length=100, null=True, blank=True)
    link = models.URLField(null=True, blank=True)
    url = models.URLField()

    def __str__(self):
        return f"{self.id}: {self.title}"

class Generator(BaseModel):
    name = models.CharField(max_length=100)
    hostname = models.CharField(max_length=150,null=True,blank=True)
    genDate = models.DateTimeField(null=True,blank=True)

    def __str__(self):
        return f"{self.id}: {self.name}"

class Podcast(BaseModel):
    title = models.CharField(max_length=100)
    language = models.CharField(max_length=50)
    itunes_type = models.CharField(max_length=50)
    copy_right = models.CharField(max_length=100)
    explicit = models.CharField(max_length=50)
    description = models.TextField() #We use description for itunes summary too.
    pubDate = models.DateTimeField(null=True,blank=True)
    last_build_date = models.DateTimeField(null=True,blank=True)
    link = models.URLField(null=True,blank=True)
    itunes_subtitle = models.TextField(null=True,blank=True)
    itunes_keywords = models.TextField(null=True, blank=True)
    category = models.ManyToManyField(Category)
    pod_generator = models.ForeignKey(Generator,on_delete=models.CASCADE)
    author = models.ForeignKey(PodcastAuthor,on_delete=models.SET_NULL, null=True)
    pod_image = models.OneToOneField(Image,on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.id}: {self.title}"
