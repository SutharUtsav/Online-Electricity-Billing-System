from django.contrib import admin
from Billing_System.models import Generate_Bill,Payment_Status
# Register your models here.

admin.site.register(Generate_Bill)
admin.site.register(Payment_Status)
