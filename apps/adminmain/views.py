from django.shortcuts import render
from apps.autenticateapp.models import PatientModel,DoctorModel
from apps.autenticateapp.serializers import PatientRegSerializer,DocRegSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework.authentication import TokenAuthentication
from rest_framework import status
from .serializers import DocRegUpdateSerializer,PatRegUpdateSerializer
# Create your views here.\
    
    
class AdminDoctor(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get(self,request,username=None,*args, **kwargs):
        if username:
            obj = DoctorModel.objects.get(user__username = username)
            serial = DocRegUpdateSerializer(obj)
        else:
            obj = DoctorModel.objects.all()
            serial = DocRegUpdateSerializer(obj,many=True)
        return Response({
            'data' : serial.data
        },status=status.HTTP_200_OK)
    
    
    def post(self,request,username,*args, **kwargs):
        data = request.data
        if DoctorModel.objects.filter(user__username = username).exists():
            user = DoctorModel.objects.get(user__username = username)
            serials = DocRegUpdateSerializer(user,data=data,partial=True)
            if serials.is_valid():
                serials.save()
                result = serials.data
            else:
                result = serials.errors 
            return Response({
                'data' : result
            },status=status.HTTP_200_OK)           
        else:
            user = "Invalid Username Please Give the Correct UserName"
            return Response({
                'data' : 'User Not Found Please Enter Valid User'
            },status=status.HTTP_404_NOT_FOUND)
            
            
class AdminPatient(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    
    def get(self,request,username=None,*args, **kwargs):
        
        if username:
            obj = PatientModel.objects.get(user__username = username)
            serial = PatRegUpdateSerializer(obj)
        else:
            obj = PatientModel.objects.all()
            serial = PatRegUpdateSerializer(obj,many=True)
        return Response({
            'data' : serial.data
        },status=status.HTTP_200_OK)
        
    
    def post(self,request,username=None,*args, **kwargs):
        data = request.data
        user = request.user
        
        if username:
            userr = PatientModel.objects.get(user__username = username)
        else:
            userr = PatientModel.objects.get(user__username = user)
        obj = PatRegUpdateSerializer(userr,data = data,partial = True)
        
        if obj.is_valid():
            obj.save()
            return Response({
                'data' : 'Edited successfully',
                'details' : obj.data
            },status=status.HTTP_200_OK)
        else:
            return Response({
                'data': obj.errors
            },status=status.HTTP_400_BAD_REQUEST)
            
