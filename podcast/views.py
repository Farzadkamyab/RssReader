from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import Podcast, Episode
from .serializer import PodcastSerializer, EpisodeSerializer
from .utils import Parser

# Create your views here.
class GetRssFileView(APIView):
    def post(self, request):
        file = request.FILES["xml"]
        file = file.read()
        Parser(rss_file=file.decode("utf-8"), save=True)
        return Response({"message":"Rss file save in database successfully."}, status.HTTP_201_CREATED)

