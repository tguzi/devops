from django.db import models


class Demand(models.Model):
    # 需求表
    publishTime = models.DateTimeField('发布时间', auto_now=True)
    description = models.CharField(max_length=64)
    branch = models.CharField(max_length=64)
    developer = models.CharField(max_length=12)
    tester = models.CharField(max_length=12)


class Env(models.Model):
    # 环境表
    branch = models.CharField(max_length=32, default='')
    name = models.CharField(max_length=12)
    env = models.CharField(max_length=12)


class RelationDemandEnv(models.Model):
    """
        环境和需求关联表
    """
    demand = models.ForeignKey('Demand', on_delete=models.CASCADE, null=True)
    env = models.ForeignKey('Env', on_delete=models.CASCADE, null=True)