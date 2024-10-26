from django.shortcuts import render
from apps.autenticateapp.models import AppointmentModel,PatientModel
from apps.autenticateapp.serializers import AppointmentSerials,PatientRegSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from apps.autenticateapp.serializers import AppointmentSerials
from rest_framework import status
# Create your views here.


class PatientAppointment(APIView):
    
    
    def get(self,request,*args, **kwargs):
        id = request.user.username 
        obj  = AppointmentModel.objects.filter(user__username=id)
        serial = AppointmentSerials(obj,many=True)
        return Response({
            'data': serial.data
        },status=status.HTTP_200_OK)
    

class PatientProfile(APIView):
    
    def get(self,request,*args, **kwargs):
        try:
            
            user = request.user.username
            obj = PatientModel.objects.get(user__username = user)
            serial = PatientRegSerializer(obj)
            
            return Response({
                'data' : serial.data
            },status=status.HTTP_200_OK)
        except PatientModel.DoesNotExist:
            return Response({
                'data' : 'Patient Does Not Exist'
            },status=status.HTTP_404_NOT_FOUND)