from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views import generic

from doctors.models import Doctor


class IndexView(generic.ListView):
    template_name = 'doctors/index.html'

    def get_queryset(self):
        return Doctor.objects.all()


class DoctorCreate(generic.CreateView):
    model = Doctor
    fields = ['name', 'specialty']


'''
def doctors_index(request):
    all_doctors = Doctor.objects.all()
    doctors_count = Doctor.objects.count()
    return render(request, "doctors/index.html", {'all_doctors': all_doctors, 'doctor_count': doctors_count})
'''
