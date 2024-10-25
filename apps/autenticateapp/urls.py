from django.urls import path
from .views import *

urlpatterns = [
    path('login/',LoginView.as_view(),name='login'),
    path('preg/',PateintRegView.as_view(),name='patientReg'),
    path('dreg/',DocRegView.as_view(),name='docreg'),
    path('change_password/',ChangePasswordView.as_view(),name='Change_password'),
    path('log_out/',LogoutView.as_view(),name='log_out'),
    path('appointment/',AppointmentView.as_view(),name='appointment'),
]
