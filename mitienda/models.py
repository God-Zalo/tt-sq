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
	client_id = models.ForeignKey(Client, on_delete=models.PROTECT)
	company_name = models.CharField(max_length=100)
	nit = models.CharField(max_length=100)
	code = models.CharField(max_length=100)

	def __str__(self):
		return self.code + ' ' + self.company_name


class Product(models.Model):
	name = models.CharField(max_length=100)
	description = models.CharField(max_length=100)

	def __str__(self):
		return self.name
