from .models import *
from rest_framework.serializers import ModelSerializer
class appointmentserializer(ModelSerializer):
    class Meta:
        model = appointment
        fields = '__all__'
class ServiceSerializer(ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'
class TransactionSerializer(ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'