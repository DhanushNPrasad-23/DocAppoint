from django.urls import path
from .views import PatientAppointment
urlpatterns = [
    path('p_apoint/',PatientAppointment.as_view(),name='PatientAppointment'),
]
