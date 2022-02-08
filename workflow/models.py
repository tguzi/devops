from django.db import models


class Branch(models.Model):
    publishTime = models.DateTimeField()
    description = models.CharField(max_length=64)
    branch = models.CharField(max_length=64)
    developer = models.CharField(max_length=12)
    tester = models.CharField(max_length=12)
    correlation = models.CharField(max_length=12)
