from django.urls import path
from .views import PatientAppointment,PatientProfile
urlpatterns = [
    path('p_apoint/',PatientAppointment.as_view(),name='PatientAppointment'),
    path('p_profile/',PatientProfile.as_view(),name='p_profile'),
]
