from . import views
from django.urls import path, include

app_name = 'medications'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),

#add a medication
    path('medications/add/', views.MedicationCreate.as_view(), name="medication-add")
]