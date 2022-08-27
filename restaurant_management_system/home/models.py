from django.db import models

class userDetails(models.Model):
    username = models.CharField(max_length=122)
    password = models.CharField(max_length=122)
