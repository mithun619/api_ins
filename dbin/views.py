from .models import Player,Content
from rest_framework import viewsets
from dbin.serializer import PlayerSerializer,ContentSerializer


class PlayerView(viewsets.ModelViewSet):
	queryset=Player.objects.all()
	serializer_class=PlayerSerializer

class ContentView(viewsets.ModelViewSet):
	queryset=Content.objects.all()
	serializer_class=ContentSerializer