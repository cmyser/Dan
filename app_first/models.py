from django.db import models

# Create your models here.
from django.db import models
from django.shortcuts import reverse
import hashlib
from django.utils.text import slugify
from time import time


class Adress(models.Model):
    adres = models.CharField(max_length=150, db_index=True)
    number_phon = models.CharField(max_length=150)
    x_re = models.FloatField(default=0)
    y_re = models.FloatField(default=0)
    start = models.CharField(max_length=150)
    stop = models.CharField(max_length=150)
    idi = models.IntegerField(default=0)


# class Services(models.Model):
#     ''' таблица с услугами'''
#