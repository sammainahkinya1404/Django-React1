from django.shortcuts import render
from django.http import HttpResponse

from .serializers import RoomSerializer
from .models import Room
from rest_framework import generics

# Create your views here.

class RoomView(generics.ListAPIView):
    queryset=Room.objects.all()
    serializer_class=RoomSerializer
    

    
