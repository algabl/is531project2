from django.db import models

class Mousepad(models.Model):
    name = models.CharField(max_length=255)
    image = models.URLField()