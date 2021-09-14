from rest_framework import viewsets, generics
from register.models import Customer, Company, Docs
from register.serializer import CustomerSerializer, CompanySerializer, DocsSerializer


class CustomerViewSet(viewsets.ModelViewSet):
    """Showing all Customers"""
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    
    

class CompanyViewSet(viewsets.ModelViewSet):
    """Showing all Companies"""
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


class DocsViewSet(viewsets.ModelViewSet):
    """Showing all Documents"""
    queryset = Docs.objects.all()
    serializer_class = DocsSerializer    


