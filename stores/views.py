from django.shortcuts import render
from rest_framework import generics
from .serializers import PizzeriaListSerializer, PizzeriaDetailSerializer
from .models import Pizzeria


class PizzeriaListAPIVIEW(generics.ListAPIView):
    queryset = Pizzeria.objects.all()
    serializer_class = PizzeriaListSerializer


class PizzeriaRetrieveAPIAPIView(generics.RetrieveAPIView):
    lookup_field = 'id'
    queryset = Pizzeria.objects.all()
    serializer_class = PizzeriaDetailSerializer
