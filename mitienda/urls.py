from django.urls import path
from .views import GetBills, GetBillDetail, GetClients, GetProducts, GetProductDetail, GetBillsProducts, GetBillsProductsDetail, GetClientDetail#, RegisterClient
from mitienda import views

urlpatterns = [
	path ('bills/', GetBills.as_view(), name='list-bills'),
	path ('bills/<int:pk>/', GetBillDetail.as_view(), name='detail-bill'),

	path ('clients/', GetClients.as_view(), name='list-clients'),
	path ('clients/<int:pk>/', GetClientDetail.as_view(), name='detail-client'),
#	path ('register/', views.RegisterClient, name='register-client'),

	path ('products/', GetProducts.as_view(), name='list-products'),
	path ('products/<int:pk>/', GetProductDetail.as_view(), name='detail-product'),

	path ('billsproducts/', GetBillsProducts.as_view(), name='list-bills-products'),
	path ('billsproducts/<int:pk>/', GetBillsProductsDetail.as_view(), name='detail-bills-product'),
]
