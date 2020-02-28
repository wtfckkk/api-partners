from django.db import models
from django_mysql.models import JSONField


class Partner(models.Model):
    tradingName = models.CharField(max_length=60)
    ownerName = models.CharField(max_length=60)
    cnpj = models.CharField(unique=True, max_length=35)
    coverageArea = JSONField()
    address = JSONField()

