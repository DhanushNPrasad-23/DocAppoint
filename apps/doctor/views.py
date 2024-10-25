from django.shortcuts import render
from apps.autenticateapp.models import AppointmentModel,DoctorModel
from apps.autenticateapp.serializers import AppointmentSerials,DocRegSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class DoctorAppointmentView(APIView):
    
    def get(self,request,*args, **kwargs):
        try:
            username = request.user.username
            obj = AppointmentModel.objects.filter(doc_name = username)
            serial = AppointmentSerials(obj,many=True)
            return Response({
                'data' : serial.data,
            },status=status.HTTP_200_OK)
        except Exception as err:
            print(err)
            return Response({
                'data' : 'data is not provided{err}'
            },status=status.HTTP_200_OK)     
    
    def post(self, request,pat_name, *args, **kwargs):
        try:
            user = AppointmentModel.objects.get(pat_name = pat_name)
            user.delete()  
            
            return Response({
                'data': 'Data deleted successfully'
            }, status=status.HTTP_200_OK)
        except AppointmentModel.DoesNotExist:
            return Response({
                'error': 'Data not found'
            }, status=status.HTTP_404_NOT_FOUND)
        except Exception as err:
            print(err)
            return Response({
                'error': str(err)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            
            
class DocProfile(APIView):
    
    
    def get(self,request,*args, **kwargs):
        try:
            user = request.user.username
            
            obj = DoctorModel.objects.get(user__username = user)
            serail = DocRegSerializer(obj)
            
            return Response({
                'data' : serail.data
            },status=status.HTTP_200_OK)
        except DoctorModel.DoesNotExist:
            return Response({
                'data' : 'Doctor Does Not Exist'
            },status=status.HTTP_400_BAD_REQUEST)
        except Exception as err:
            print(err,request.user.username)
            
