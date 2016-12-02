from __future__ import unicode_literals

from django.conf import settings
from django.db import models


class English(models.Model):
    word = models.CharField(max_length=64)
    translation = models.CharField(max_length=256)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    rate = models.FloatField(default=0.0)


class Russian(models.Model):
    word = models.CharField(max_length=64)
    translation = models.CharField(max_length=256)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    rate = models.FloatField(default=0.0)
