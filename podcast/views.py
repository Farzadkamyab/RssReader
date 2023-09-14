from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import Podcast, Episode
from .serializer import PodcastSerializer, EpisodeSerializer
from .utils import Parser
from rest_framework.pagination import PageNumberPagination

# Create your views here.
class GetRssFileView(APIView):
    def post(self, request):
        file = request.FILES["xml"]
        file = file.read()
        Parser(rss_file=file.decode("utf-8"), save=True)
        return Response({"message":"Rss file save in database successfully."}, status.HTTP_201_CREATED)

class PodcastListView(APIView, PageNumberPagination):
    page_size = 10
    def get(self, request):
        query = Podcast.objects.all()
        res = self.paginate_queryset(query, request, view=self)
        ser_data = PodcastSerializer(instance=res, many=True)
        return self.get_paginated_response(ser_data.data)

class PodcastDetailView(APIView):
    def get(self, request, pk):
        query = Podcast.objects.get(pk=pk)
        ser_data = PodcastSerializer(instance=query)
        return Response(ser_data.data, status=status.HTTP_200_OK)

class EpisodeListView(APIView, PageNumberPagination):
    page_size = 10
    def get(self, request):
        query = Episode.objects.all()
        res = self.paginate_queryset(query, request, view=self)
        ser_data = EpisodeSerializer(instance=res, many=True)
        return self.get_paginated_response(ser_data.data)

class EpisodeDetailView(APIView):
    def get(self, request, pk):
        query = Episode.objects.get(pk=pk)
        ser_data = EpisodeSerializer(instance=query)
        return Response(ser_data.data, status=status.HTTP_200_OK)
