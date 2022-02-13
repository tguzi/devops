from django.db import models


class Demand(models.Model):
    publishTime = models.DateTimeField()
    description = models.CharField(max_length=64)
    branch = models.CharField(max_length=64)
    developer = models.CharField(max_length=12)
    tester = models.CharField(max_length=12)
    correlation = models.CharField(max_length=12)
    status = models.CharField(max_length=12)


class Env(models.Model):
    branch = models.CharField(max_length=32)
    name = models.CharField(max_length=12)
    config = models.CharField(max_length=64)
    env = models.CharField(max_length=12)
    demands = models.CharField(max_length=64)
