from django.db import models

class Mousepad(models.Model):
    name = models.CharField(max_length=255)
    image = models.URLField()

    class Meta:
    # Set the custom table name without the app prefix
        db_table = 'mousepad'