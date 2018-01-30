from django.conf.urls import url

from . import views
from django.contrib import admin
from django.urls import path, include


app_name = 'patients'
urlpatterns = [
    # /patients/
    path('', views.patient_index, name='patient_index'),

    # /patients/id/ old_method >> url(r'^(?P<patient_id>[0-9]+)/$', views.patient_details, name='patient_detail')
    path('<int:patient_id>/', views.patient_details, name='patient_detail'),

    # /patients/id/treated
    #path('<int:patient_id>/treated/', views.patient_treated, name='patient_treated')
]
