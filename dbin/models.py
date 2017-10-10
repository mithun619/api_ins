

from django.db import models

class Player(models.Model):
	Playername=models.CharField(max_length=100)

class Content(models.Model):
	position=models.CharField(max_length=100)
	jno=models.IntegerField()
