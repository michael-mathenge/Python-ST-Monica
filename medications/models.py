from django.db import models

# Create your models here.
from _datetime import date, datetime

from django.urls import reverse


class Medication(models.Model):
    name = models.CharField(max_length=250)

    def get_absolute_url(self):
        return reverse('medications:index')

    def __str__(self):
        return self.name
