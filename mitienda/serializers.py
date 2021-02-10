from rest_framework import serializers
from .models import Client, Bill, Product, BillProduct

# Model Serializer would had been WAY easier

# Serialize Product
class ProductSerializer(serializers.Serializer):
	id = serializers.IntegerField(read_only=True)
	name = serializers.CharField(required=False, allow_blank=True, max_length=100)
	description = serializers.CharField(required=False, allow_blank=True, max_length=100)


	def create(self, validated_data):
		return Client.objects.create(**validated_data)


	def update(self, instance, validated_data):
		instance.name = validated_data.get('name', instance.name)
		instance.description = validated_data.get('description', instance.description)
		instance.save()
		return instance


class ProductSerializer2(serializers.Serializer):
	id = serializers.IntegerField(read_only=True)


# Serialize Bills-Products
class BillProductSerializer(serializers.Serializer):
	id = serializers.IntegerField(read_only=True)
	bill_id = serializers.CharField(required=True, allow_blank=True, max_length=100)
	product_id = ProductSerializer2(many=True)

	def create(self, validated_data):
		return Client.objects.create(**validated_data)


	def update(self, instance, validated_data):
		instance.bill_id = validated_data.get('bill_id', instance.bill_id)
		instance.product_id = validated_data.get('product_id', instance.product_id)
		instance.save()
		return instance


# Serialize Bills
class BillSerializer(serializers.Serializer):
	id = serializers.IntegerField(read_only=True)
	client_id = serializers.CharField(required=True, allow_blank=True, max_length=100)
	company_name = serializers.CharField(required=True, allow_blank=True, max_length=100)
	nit = serializers.CharField(required=True, allow_blank=True, max_length=100)
	code = serializers.CharField(required=True, allow_blank=True, max_length=100)


	def create(self, validated_data):
		return Client.objects.create(**validated_data)


	def update(self, instance, validated_data):
		instance.client_id = validated_data.get('client_id', instance.client_id)
		instance.company_name = validated_data.get('company_name', instance.company_name)
		instance.nit = validated_data.get('nit', instance.nit)
		instance.code = validated_data.get('code', instance.code)
		instance.save()
		return instance


# Serialize Clients
class ClientSerializer(serializers.Serializer):
	id = serializers.IntegerField(read_only=True)
	document = serializers.CharField(required=True, allow_blank=True, max_length=15)
	first_name = serializers.CharField(required=True, allow_blank=True, max_length=50)
	last_name = serializers.CharField(required=True, allow_blank=True, max_length=50)
	email = serializers.EmailField(required=True, allow_blank=True, max_length=254)


	def create(self, validated_data):
		return Client.objects.create(**validated_data)


	def update(self, instance, validated_data):
		instance.document = validated_data.get('document', instance.document)
		instance.first_name = validated_data.get('first_name', instance.first_name)
		instance.last_name = validated_data.get('last_name', instance.last_name)
		instance.email = validated_data.get('email', instance.email)
		instance.save()
		return instance
