from django.shortcuts import render
from .serializers import  ClientSerializer, BillSerializer, BillProductSerializer, ProductSerializer

from django.contrib.auth.models import User
from .models import Bill, Client, Product, BillProduct
from rest_framework import generics

# Create your views here.

class GetBills(generics.ListAPIView):
	serializer_class = BillSerializer
	queryset = Bill.objects.all()


class GetClients(generics.ListAPIView):
	serializer_class = ClientSerializer
	queryset = Client.objects.all()


class GetProducts(generics.ListAPIView):
	serializer_class = ProductSerializer
	queryset = Product.objects.all()

class GetBillsProducts(generics.ListAPIView):
	serializer_class = BillProductSerializer
	queryset = BillProduct.objects.all()
