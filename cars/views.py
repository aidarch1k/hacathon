from django.shortcuts import render

# Create your views here.
from rest_framework import generics

from .models import Car
from .serializers import CarDetailSerializer, CarsListSerializer


class CarCreateView(generics.CreateAPIView):
    serializer_class = CarDetailSerializer

class CarsListView(generics.ListAPIView):
    serializer_class = CarsListSerializer
    queryset = Car.objects.all()

class CarDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CarDetailSerializer
    queryset = Car.objects.all()
