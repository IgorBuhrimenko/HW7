from django.db import models

from datetime import timezone
# Create your models here.


class Log(models.Model):
    path = models.CharField(max_length=100)
    method = models.CharField(max_length=10)
    execution_time_sec = models.FloatField()
