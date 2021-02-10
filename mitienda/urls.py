from django.urls import path
from .views import GetClients


urlpatterns = [
	path ('clients/', GetClients.as_view(), name='list-clients'),
]
