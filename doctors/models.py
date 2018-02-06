from django.db import models


# Create your models here.
from django.urls import reverse


class Doctor(models.Model):
    name = models.CharField(max_length=50)
    specialty = models.CharField(max_length=250)

    def get_absolute_url(self):
        return reverse('doctors:index')

    def __str__(self):
        return self.name + ' - ' + self.specialty
