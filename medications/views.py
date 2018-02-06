from medications.models import Medication
from django.views import generic

class IndexView(generic.ListView):
    template_name = 'medications/index.html'

    def get_queryset(self):
        return Medication.objects.all()

class DetailView(generic.DetailView):
    model = Medication
    template_name = 'medications/detail.html'

class MedicationCreate(generic.CreateView):
    model = Medication
    fields = ['name']


'''
def medications_index(request):
    all_medications = Medication.objects.all()
    medications_count = Medication.objects.count()
    return render(request, "medications/index.html", {'all_medications': all_medications, 'meds_count':medications_count})
'''
