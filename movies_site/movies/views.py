from django.shortcuts import render
from rest_framework import viewsets
from .serializers import MovieSerializer
from .models import MovieData


class MovieViewSet(viewsets.ModelViewSet):
    queryset = MovieData.objects.all()
    serializer_class = MovieSerializer

class ActionViewSet(viewsets.ModelViewSet):
    queryset = MovieData.objects.filter(genre='action')
    serializer_class = MovieSerializer

class DramaViewSet(viewsets.ModelViewSet):
    queryset = MovieData.objects.filter(genre='drama')
    serializer_class = MovieSerializer
