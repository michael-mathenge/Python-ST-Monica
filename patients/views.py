from django.views import generic
from .models import Patient


class IndexView(generic.ListView):
    template_name = 'patients/index.html'

    def get_queryset(self):
        return Patient.objects.all()


class DetailView(generic.DetailView):
    model = Patient
    template_name = 'patients/detail.html'


class PatientCreate(generic.CreateView):
    model = Patient
    fields = ['name', 'age', 'telephone', 'residence', 'next_of_kin',
              'allergies', 'medication_history', 'past_medical_history']


"""
def patient_index(request):
    all_patients = Patient.objects.all()
    patients_count = Patient.objects.count()
    return render(request, "patients/index.html", {'all_patients': all_patients, 'patient_count': patients_count})


def patient_details(request, patient_id):
    patient = get_object_or_404(Patient, pk=patient_id)
    return render(request, "patients/detail.html", {'patient': patient})

 """
