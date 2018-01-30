from django.shortcuts import render, get_object_or_404
from .models import Patient

# Create your views here.

def patient_index(request):
    all_patients = Patient.objects.all()
    patients_count = Patient.objects.count()
    return render(request, "patients/patients.html", {'all_patients': all_patients, 'patient_count': patients_count})


def patient_details(request, patient_id):
    patient = get_object_or_404(Patient, pk=patient_id)
    return render(request, "patients/patient_detail.html", {'patient': patient})
