from django.urls import path
from .views import *

app_name = "podcast"

urlpatterns = [
    path("import/", GetRssFileView.as_view(), name="add-file"),
    path("podcasts/", PodcastListView.as_view(), name="podcasts"),
    path("podcast/<int:pk>/", PodcastDetailView.as_view(), name="podcast-detail"),
    path("episodes/", EpisodeListView.as_view(), name="episodes"),
    path("episode/<int:pk>/", EpisodeDetailView.as_view(), name="episode-detail"),
]