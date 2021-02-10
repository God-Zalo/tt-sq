from django.shortcuts import render
from .serializers import  ClientSerializer, BillSerializer, ProductSerializer

from django.contrib.auth.models import User
from .models import Bill, Client, Product
from rest_framework import generics

# Create your views here.

class GetClients(generics.ListAPIView):
	serializer_class = ClientSerializer
	queryset = Client.objects.all()
