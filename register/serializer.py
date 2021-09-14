from rest_framework import serializers
from register.models import Customer, Company, Docs

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer 
        fields = '__all__'


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'


class DocsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Docs
        fields = ['user', 'doc']    




       