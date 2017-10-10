from rest_framework import serializers
from .models import Player,Content
#from django.contrib.auth.models import Player,Content

class PlayerSerializer(serializers.ModelSerializer):
	class Meta:
		model=Player
		fields=('Playername')


class ContentSerializer(serializers.ModelSerializer):
	class Meta:
		model=Content
		fields=('position','jno')
