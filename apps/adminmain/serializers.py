from rest_framework import serializers
from apps.autenticateapp.models import DoctorModel,PatientModel


class DocRegUpdateSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', max_length=40)
    
    class Meta:
        model = DoctorModel
        fields = ['username', 'phone_number', 'email', 'specialization']
    
    def update(self, instance, validated_data):
        instance.phone_number = validated_data.get('phone_number', instance.phone_number)
        instance.email = validated_data.get('email', instance.email)
        instance.specialization = validated_data.get('specialization', instance.specialization)
        instance.save()
        
        return instance
    
    

class PatRegUpdateSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', max_length=40)
    
    class Meta:
        model = PatientModel
        fields = ['username', 'p_id', 'address', 'email','p_pno']
    
    def update(self, instance, validated_data):
        instance.p_id = validated_data.get('p_id', instance.p_id)
        instance.address = validated_data.get('address', instance.address)
        instance.email = validated_data.get('email', instance.email)
        instance.p_pno = validated_data.get('p_pno', instance.p_pno)
        instance.save()
        
        return instance

