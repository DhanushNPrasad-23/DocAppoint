from django.shortcuts import render
from django.contrib.auth import authenticate,login,logout
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .serializers import *
from .models import *
from rest_framework.authtoken.models import Token
from django.shortcuts import get_object_or_404
from Dup import settings
from django.core.mail import send_mail
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import AllowAny




def send_order_confirmation_email(user_email,name):
    subject = f'Welcome {name}'
    message = 'Thank you for becoming Docfin family'
    email_from = settings.DEFAULT_FROM_EMAIL
    recipient_list = [user_email]  # List of recipients

    send_mail(subject, message, email_from, recipient_list)

# Create your views here.

class LoginView(APIView):
    permission_classes = [AllowAny]
    
    def post(self, request, *args, **kwargs):
        username = request.data['username']
        
        serial = LoginSerial(data=request.data)
        
        if serial.is_valid():
            user = serial.validated_data['user'] 
            
                
            
            login(request, user)
            
            token, created = Token.objects.get_or_create(user=user)
            if DoctorModel.objects.filter(user__username = username).exists():
                log = "Doctor"
            elif PatientModel.objects.filter(user__username = username).exists():
                log = "patient"
            else:
                log = "admin"
            
            return Response({
                'data': serial.data,
                'token': token.key,  
                'type' : log
            }, status=status.HTTP_200_OK)
        
        else:
            return Response({
                'data': 'invalid credentials, please try again'
            }, status=status.HTTP_406_NOT_ACCEPTABLE)
    
# =====================================================patient Reg =====================================================



class PateintRegView(APIView):
    
    def get(self,request,*args, **kwargs):
        obj = PatientModel.objects.all()
        serial = PatientRegSerializer(obj,many=True)
        return Response({
            'data' : serial.data,
            'status' : status.HTTP_200_OK
        })
        
    
    def post(self,request,*args, **kwargs):
        obj = request.data
        print(obj)
        if User.objects.filter(username=obj['username']).exists():            
            return Response({
                'data': 'Username already exists',
            }, status=status.HTTP_400_BAD_REQUEST)
        elif PatientModel.objects.filter(p_id = obj['p_id']).exists():
            return Response({
                'data': 'id already exists',
            }, status=status.HTTP_400_BAD_REQUEST)
            
        
        serail = PatientRegSerializer(data = obj)
        if serail.is_valid():
            serail.save()
            email = obj['email']
            name = obj['username']
            send_order_confirmation_email(email,name)
            data = serail.data
            stat = status.HTTP_201_CREATED
        else:
            data = serail.errors
            stat = status.HTTP_406_NOT_ACCEPTABLE
        return Response({
            'data' : data,
        },status=stat)    
    
    
# =========================================== Doc ==========================================
    

class DocRegView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get(self,request,*args, **kwargs):
        obj = DoctorModel.objects.all()
        serail = DocRegSerializer(obj,many = True)
        return Response({
            'data' : serail.data
        },status=status.HTTP_200_OK)
    
    def post(self,request,*args, **kwargs):
        try:
            obj = request.data
            print(obj)
            if User.objects.filter(username = obj['username']).exists():
                return Response({
                    'data': 'username already exists'
                },status=status.HTTP_400_BAD_REQUEST)
            serial = DocRegSerializer(data=obj)
            
            if serial.is_valid():
                serial.save()
                email = obj['email']
                name = obj['username']
                send_order_confirmation_email(email,name)
                data = serial.data
                stat = status.HTTP_200_OK
            else:
                data = serial.errors
                stat = status.HTTP_409_CONFLICT
            return Response({
                'data' : data
            },status=stat)    
        except Exception as e:
            print(e)
    

        
    
    # ===============================================CHANGE PASSWORD =========================================
    
    
    
class ChangePasswordView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    
    def post(self,request,*args, **kwargs):
        data = request.data
        user = request.user 
        print(user.username)
        current_password = data.get('current_password')
        new_password = data.get('new_password')

        if not current_password or not new_password:
            return Response({"error": "Current password and new password are required"}, status=status.HTTP_400_BAD_REQUEST)

        if not user.check_password(current_password):
            return Response({"error": "Current password is incorrect"}, status=status.HTTP_400_BAD_REQUEST)

        user.set_password(new_password)
        user.save()

        return Response({
            'message': "Password updated successfully"
        }, status=status.HTTP_200_OK)
            
    
class LogoutView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    def post(self,request,*args, **kwargs):
        try:
            print(request.user)
            user = request.user
            obj = Token.objects.get(user = user)
            obj.delete()
            return Response({
                'data' : 'logged out successfully'
            })
        except Token.DoesNotExist:
            return Response({
                'data' : 'you are already logged out'
            })
    
    
    
# ======================================================Appointment=====================================

class AppointmentView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    
    def get(self,request,*args, **kwargs):
        obj = AppointmentModel.objects.all()
        serial = AppointmentSerials(obj,many = True)
        
        return Response({
            'data' : serial.data
        },status=status.HTTP_200_OK)
    
    
    def post(self,request,*args, **kwargs):
        try:
            obj = request.data
            user_name = request.user
            user = User.objects.get(username = user_name)
            
            obj['user'] = user.id
            print(user.id)
            serial = AppointmentSerials(data = obj)
            if serial.is_valid():
                serial.save()
                data = 'data saved successfully'
            else:
                data = serial.errors
                
            return Response({
                'data' : data
            },status=status.HTTP_200_OK)                        
        except Exception as err:
            print(err)
            return Response({
                'data' :  str(err)
            },status=status.HTTP_400_BAD_REQUEST)
            


































    
    
    
    
    
    
    
    
    
    
    
 