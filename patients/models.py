from django.db import models

# Create your models here.
from django.utils import timezone


class Patient(models.Model):
    DOB = models.DateField
    age = models.IntegerField
    record_No = models.IntegerField
    telephone_no = models.IntegerField
    name = models.CharField(max_length=50)
    residence = models.CharField(max_length=50)
    next_of_kin = models.CharField(max_length=50)
    allergies = models.CharField(max_length=1000)
    medication_history = models.CharField(max_length=1000)
    date_added = models.DateTimeField(default=timezone.now)
    past_medical_history = models.CharField(max_length=1000)
    med = models.ForeignKey('medications.Medication', on_delete=models.PROTECT, null=True)
    doctor_assigned = models.ForeignKey('doctors.Doctor', on_delete=models.PROTECT, null=True)
    is_Contacted = models.BooleanField(default=False)
    is_treated = models.BooleanField(default=False)

    def __str__(self):
        return self.name + ' - ' + self.past_medical_history + ' - ' + self.med.name + ' - '+ self.doctor_assigned.name
