from django.shortcuts import render
from apps.autenticateapp.models import AppointmentModel
from apps.autenticateapp.serializers import AppointmentSerials
from rest_framework.views import APIView
from rest_framework.response import Response
from apps.autenticateapp.serializers import AppointmentSerials
from rest_framework import status
# Create your views here.


class PatientAppointment(APIView):
    
    
    def get(self,request,*args, **kwargs):
        id = request.user.username 
        obj  = AppointmentModel.objects.filter(user__username=id)
        print(obj[0])
        serial = AppointmentSerials(obj)
        
        return Response({
            'data': serial.data
        },status=status.HTTP_200_OK)