from django.conf.urls import url

from . import views
from django.contrib import admin
from django.urls import path, include


app_name = 'patients'
urlpatterns = [
    # /patients/
    path('', views.IndexView.as_view(), name='patient_index'),

    # /patients/id/ old_method >> url(r'^(?P<patient_id>[0-9]+)/$', views.patient_details, name='patient_detail'),
    path('<int:pk>/', views.DetailView.as_view(), name='patient_detail'),

    # Adding patient
    path('patient/add/', views.PatientCreate.as_view(), name='patient-add'),

    # /patients/id/treated
    #path('<int:patient_id>/treated/', views.patient_treated, name='patient_treated')
]
