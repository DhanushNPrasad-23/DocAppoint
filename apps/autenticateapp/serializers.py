from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .models import *

class DisplaySerial(serializers.ModelSerializer):
    
    class Meta:
        model = DisplayModel
        fields = '__all__'
    
    def create(self,validated_data):
        user = DisplayModel.objects.create(**validated_data)
        return user
    

class LoginSerial(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)
    

    def validate(self, data):
        username = data.get('username')
        password = data.get('password')

        user = authenticate(username=username, password=password)
        if not user:
            raise serializers.ValidationError("Invalid credentials")
        
        data['user'] = user
        return data
    
    
# ==================================================== Registrations ===========================================   
    
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']
        extra_kwargs = {'password': {'write_only': True}} 

    def create(self, validated_data):
        username = validated_data.get('username')
        password = validated_data.get('password')
        
        user = User.objects.create_user(username=username, password=password)
        return user
        
        
        
# =============================================PatientReg ======================================================



class PatientRegSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', max_length=40)
    password = serializers.CharField(source='user.password', write_only=True, max_length=40)  

    class Meta:
        model = PatientModel
        fields = ['username', 'password', 'p_id', 'address', 'email', 'p_pno']

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        
        user = User.objects.create_user(**user_data)
        
        patient = PatientModel.objects.create(user=user, **validated_data)

        return patient

# =====================================DocReg===================================================================

class DocRegSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source = 'user.username',max_length = 40)
    password = serializers.CharField(source = 'user.password',write_only=True,max_length=50)
    
    class Meta:
        model = DoctorModel
        fields = ['username','password','phone_number','email','specialization']
    
    def create(self, validated_data):
        user_data = validated_data.pop('user')
        
        user = User.objects.create_user(**user_data)
        
        doc = DoctorModel.objects.create(user=user,**validated_data)
    
        return doc
    
# ==================================================CHECK SERIALIZER =====================================


class AppointmentSerials(serializers.ModelSerializer):
    
    
    class Meta:
        model = AppointmentModel
        fields = ['user','appointment_date','doc_name','email','age','gender','description','pat_name']
        
    def create(self, validated_data):
        user_data = validated_data.pop('user')
        doc_name = validated_data['doc_name']
        pat_name = validated_data['pat_name']
        if AppointmentModel.objects.filter(doc_name = doc_name,pat_name = pat_name).exists():
            raise serializers.ValidationError({'detail': 'An appointment with this doctor and patient already exists.'})
               
        user = AppointmentModel.objects.create(user = user_data,**validated_data)
        return user
    