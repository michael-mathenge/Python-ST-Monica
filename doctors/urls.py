from . import views
from django.urls import path, include

app_name = 'doctors'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),

    # adding a doctor
    path('doctor/add/', views.DoctorCreate.as_view(), name="doctor-add")
]
