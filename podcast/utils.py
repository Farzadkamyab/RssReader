import re
import datetime as dt
from .models import Podcast, Episode, Category, Generator, Image, Owner
from author.models import EpisodeAuthor, PodcastAuthor

class PodcastModel:
    def __init__(self, xml=None):
        self.xml = xml

class EpisodeModel:
    def __init__(self,podcast, title=None,author=None,guid=None,description=None,pubDate=None,link=None,itunes_title=None) -> None:
        self.title=title
        self.author=author
        self.guid=guid
        self.description=description
        self.pubDate=pubDate
        self.link=link
        self.itunes_title=itunes_title

class Parser:
    item_tag_pattern = re.compile("<item>((\n|.)*?)</item>")
    tag_pattern = re.compile("<([^\<\> ]*)(?:\s*(\S*)=\"([^\"]*?)\"[^\>]*)*>")
    key_value_pair_pattern = re.compile('([^ ]*?)=\"(.*?)\"')
