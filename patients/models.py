from django.db import models

# Create your models here.
from django.urls import reverse
from django.utils import timezone


class Patient(models.Model):
    DOB = models.DateField(null=True)
    age = models.IntegerField(null=True)
    record_No = models.IntegerField(null=True)
    telephone = models.IntegerField(null=True)
    name = models.CharField(max_length=50)
    residence = models.CharField(max_length=50)
    next_of_kin = models.CharField(max_length=50)
    allergies = models.CharField(max_length=1000)
    medication_history = models.CharField(max_length=1000)
    date_added = models.DateTimeField(default=timezone.now)
    past_medical_history = models.CharField(max_length=1000)
    med = models.ForeignKey('medications.Medication', on_delete=models.PROTECT, null=True)
    doctor_assigned = models.ForeignKey('doctors.Doctor', on_delete=models.PROTECT, null=True)
    tests = models.CharField(max_length=1000, null=True)
    is_Contacted = models.BooleanField(default=False)
    is_treated = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse('patients:patient_detail', kwargs={'pk':self.pk})

    def __str__(self):
        return self.name + ' - ' + str(self.age)+ ' - ' + str(self.DOB)+ ' - ' + str(self.telephone)+ ' - ' + self.residence
