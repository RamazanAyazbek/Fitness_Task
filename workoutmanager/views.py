from django.shortcuts import render
from .models import Appointment, Trainer
from rest_framework import viewsets
from .serializers import AppointmentSerializer, TrainerSerializer



class AppointmentViewAPI(viewsets.ModelViewSet):
    serializer_class=AppointmentSerializer
    queryset=Appointment.objects.all()

class TrainerViewAPI(viewsets.ModelViewSet):
    serializer_class=TrainerSerializer
    queryset=Trainer.objects.all()


