from django.shortcuts import render
from .serializers import  ClientSerializer, BillSerializer, BillProductSerializer, ProductSerializer

from django.contrib.auth.models import User
from .models import Bill, Client, Product, BillProduct

#NON Abstract API Views
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import authentication, permissions, status
from django.http import Http404, HttpResponse

from django.views.generic import TemplateView

from django.views.decorators.csrf import csrf_exempt

from django.utils.decorators import method_decorator


# ----------------------------------------------------> Products CRUD ORM
class GetProducts(APIView):
	def get(self, request, format=None):
		products = Product.objects.all()
		serializer = ProductSerializer(products, many=True)
		return Response(serializer.data)


	def post(self, request, format=None):
		serializer = ProductSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GetProductDetail(APIView):
	

	def get_object(self, pk):
		try:
			return Product.objects.get(pk=pk)
		except Product.DoesNotExist:
			raise Http404


	def get(self, request, pk, format=None):
		product = self.get_object(pk)
		serializer = ProductSerializer(product)
		return Response(serializer.data)


	def put(self, request, pk, format=None):
		product = self.get_object(pk)
		serializer = ProductSerializer(product, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_404_BAD_REQUEST)


	def delete(self, request, pk, format=None):
		product = self.get_object(pk)
		product.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)


# ----------------------------------------------------> Clients CRUD RAW
class GetClients(APIView):
	def get(self, request, format=None):
		clients = Client.objects.raw(
			'''
			SELECT * FROM mitienda_client
			'''
			)
		serializer = ClientSerializer(clients, many=True)
		return Response(serializer.data)


	def post(self, request, format=None):
		serializer = ClientSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GetClientDetail(APIView):
	

	def get_object(self, pk):
		try:
			client = Client.objects.get(pk=pk)
			return client
		except Client.DoesNotExist:
			raise Http404


	def get(self, request, pk, format=None):
		client = self.get_object(pk)
		serializer = ClientSerializer(client)
		return Response(serializer.data)


	def put(self, request, pk, format=None):
		client = self.get_object(pk)
		serializer = ClientSerializer(client, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_404_BAD_REQUEST)


	def delete(self, request, pk, format=None):
		client = self.get_object(pk)
		client.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)



# ----------------------------------------------------> Bills CRUD RAW
class GetBills(APIView):
	def get(self, request, format=None):
		bills = Bill.objects.all()
		serializer = BillSerializer(bills, many=True)
		return Response(serializer.data)


	def post(self, request, format=None):
		serializer = BillSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GetBillDetail(APIView):
	

	def get_object(self, pk):
		try:
			return Bill.objects.get(pk=pk)
		except Bill.DoesNotExist:
			raise Http404


	def get(self, request, pk, format=None):
		bill = self.get_object(pk)
		serializer = BillSerializer(bill)
		return Response(serializer.data)


	def put(self, request, pk, format=None):
		bill = self.get_object(pk)
		serializer = BillSerializer(bill, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_404_BAD_REQUEST)


	def delete(self, request, pk, format=None):
		bill = self.get_object(pk)
		bill.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)


# ----------------------------------------------------> BillsProducts CRUD RAW
class GetBillsProducts(APIView):
	def get(self, request, format=None):
		bills_products = BillProduct.objects.all()
		serializer = BillProductSerializer(bills_products, many=True)
		return Response(serializer.data)


	def post(self, request, format=None):
		serializer = BillProductSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GetBillsProductsDetail(APIView):
	

	def get_object(self, pk):
		try:
			return BillProduct.objects.get(pk=pk)
		except BillProduct.DoesNotExist:
			raise Http404


	def get(self, request, pk, format=None):
		bill_product = self.get_object(pk)
		serializer = BillProductSerializer(bill_product)
		return Response(serializer.data)


	def put(self, request, pk, format=None):
		bill_product = self.get_object(pk)
		serializer = BillProductSerializer(bill_product, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_404_BAD_REQUEST)


	def delete(self, request, pk, format=None):
		bill_product = self.get_object(pk)
		bill_product.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)



class CreateUser(TemplateView):
	@method_decorator(csrf_exempt)
	def dispatch(self, request, *args, **kwargs):
		return super(CreateUser, self).dispatch(request, *args, **kwargs)


	def get(self, request):
		return render(request, 'mitienda/register.html')


	def post(self, request, format=None):
		username = request.POST.get('username', False)
		pasword = request.POST.get('password', False)

		return render(request, 'mitienda/register.html')

