import re
import datetime as dt
from .models import Podcast, Episode, Category, Generator, Image, Owner
from author.models import EpisodeAuthor, PodcastAuthor

class PodcastModel:
    def __init__(self, xml=None):
        self.xml = xml
