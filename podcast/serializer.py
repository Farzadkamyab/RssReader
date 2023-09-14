from rest_framework.serializers import Serializer, ModelSerializer
from .models import Podcast, Episode

class PodcastSerializer(ModelSerializer):
    class Meta:
        model = Podcast
        fields = "__all__"
