from django.urls import path
from .views import GetBills, GetClients, GetProducts, GetBillsProducts


urlpatterns = [
	path ('bills/', GetBills.as_view(), name='list-bills'),
	path ('clients/', GetClients.as_view(), name='list-clients'),
	path ('products/', GetProducts.as_view(), name='list-products'),
	path ('billsproducts/', GetBillsProducts.as_view(), name='list-bills-products'),
]
