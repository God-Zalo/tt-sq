from django.db import models

# Create your models here.

class Client(models.Model):
	document = models.CharField(max_length=15)
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	email = models.EmailField(max_length=254)

	def __str__(self):
		return self.first_name + ' ' + self.last_name


class Bill(models.Model):
	id = models.AutoField(primary_key=True)
	client_id = models.ForeignKey(Client, on_delete=models.PROTECT)
	company_name = models.CharField(max_length=100)
	nit = models.CharField(max_length=100)
	code = models.CharField(max_length=100)

	def __str__(self):
		return str(self.id)


class Product(models.Model):
	name = models.CharField(max_length=100)
	description = models.CharField(max_length=100)

	def __str__(self):
		return self.name

class BillProduct(models.Model):
	bill_id = models.ForeignKey(Bill, on_delete=models.PROTECT)
	product_id = models.ManyToManyField(Product)

	def __str__(self):
		return str(self.bill_id)