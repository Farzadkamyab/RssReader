from django.contrib import admin
from .models import Podcast, Episode, Category, Generator, Image, Owner, PodcastAuthor, EpisodeAuthor

# Register your models here.
admin.site.register(Podcast)
admin.site.register(Episode)
admin.site.register(Category)
admin.site.register(Generator)
admin.site.register(Image)
admin.site.register(Owner)
admin.site.register(PodcastAuthor)
admin.site.register(EpisodeAuthor)