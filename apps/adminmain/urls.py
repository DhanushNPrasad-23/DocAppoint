from django.urls import path
from .views import *

urlpatterns = [
    path('admin-doctor/',AdminDoctor.as_view(),name='admin-doctor'),
    path('admin-doctor/<str:username>/',AdminDoctor.as_view(),name='admin-doctor'),
    path('admin-patient/',AdminPatient.as_view(),name='admin-patient'),
    path('admin-patient/<str:username>/',AdminPatient.as_view(),name='admin-patient'),
    
    
]
