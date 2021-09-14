from os import name
from django.contrib.auth.models import User
from django.db import models
from .validators import validate_CNPJ, validate_CPF, validate_phone
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

class Customer(models.Model):
    name = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    cpf = models.CharField("CPF", unique=True, max_length=14, validators=[validate_CPF])

    def __str__(self):
        return f"{self.user.username} - {self.cpf}"
    
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)     
    
class Docs(models.Model):
    user = models.ForeignKey(Customer, on_delete=models.CASCADE)
    doc = models.FileField(upload_to='meusarquivos/')        
    
   
class Company(models.Model):
    managers = models.ManyToManyField(User, related_name='company', blank=True, verbose_name='managers')
    name = models.CharField(max_length=30)
    cnpj = models.CharField('CNPJ', unique=True, max_length=14, validators=[validate_CNPJ])
    email = models.EmailField(max_length=50)
    phone_number = models.CharField("Phone", validators=[validate_phone], max_length=17, blank=True)
    

    class Meta:
        verbose_name_plural = 'Company'


    def __str__(self):
        return self.name


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)       