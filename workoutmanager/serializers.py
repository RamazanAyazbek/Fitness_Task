from .models import Client, Trainer, GymRoom, Schedule, Appointment
from rest_framework import serializers



class TrainerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Trainer
        fields='__all__'

class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Appointment
        fields='__all__'
        







