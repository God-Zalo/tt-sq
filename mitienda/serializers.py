from rest_framework import serializers
from .models import Client, Bill, Product

class ClientSerializer(serializers.ModelSerializer):
	class Meta:
		model = Client
		fields = ['document', 'first_name', 'last_name', 'email']


class BillSerializer(serializers.ModelSerializer):
	class Meta:
		model = Bill
		fields = ['client_id', 'company_name', 'nit', 'code']


class ProductSerializer(serializers.ModelSerializer):
	class Meta:
		model = Product
		fields = ['name', 'description']
