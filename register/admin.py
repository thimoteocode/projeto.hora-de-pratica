from django.contrib import admin

from .models import Customer, Company, Docs

class DocsInlineAdmin(admin.TabularInline):
    model = Docs
    extra = 1

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ("name", "cpf")
    inlines = [DocsInlineAdmin]


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ("name", "cnpj", "email", "phone_number")


 