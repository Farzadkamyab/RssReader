from django.urls import path
from .views import *

app_name = "podcast"

urlpatterns = [
    path("import/", GetRssFileView.as_view(), name="add-file"),
