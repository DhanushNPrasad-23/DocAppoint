from django.urls import path
from .views import *

urlpatterns = [
    path('doc-appointment-view/',DoctorAppointmentView.as_view(),name='doc-appointment-view'),
    path('doc-appointment-view/<str:pat_name>/',DoctorAppointmentView.as_view(),name='doc-appointment-view'),
    path('docprofile/',DocProfile.as_view(),name='docprofile'),
]
