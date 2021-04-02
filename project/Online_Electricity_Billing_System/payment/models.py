from django.db import models
from django.core.validators import RegexValidator
from Billing_System.models import Generate_Bill
from django.conf import settings
from Login.models import Login


# Create your models here.
class NetBanking(models.Model):
    customer_no = models.CharField(max_length = 255)
    # meter_no = models.CharField(max_length = 255)
    bill_no = models.IntegerField()
    bill_amount = models.DecimalField(max_digits=6,decimal_places=2)
    bank_name_regex = RegexValidator(regex = r'^[atozAtoZ ]$',message="Invalid Bank Name")
    bank_name = models.CharField(validators=[bank_name_regex],max_length = 255)
    branch_code = models.CharField(max_length = 255)
    account_no = models.CharField(max_length = 255)

class bhimUPI(models.Model):
    customer_no = models.CharField(max_length = 255)
    # meter_no = models.CharField(max_length = 255)
    bill_no = models.IntegerField()
    bill_amount = models.DecimalField(max_digits=6,decimal_places=2)
    upi_id = models.CharField(max_length = 255)

class MobileBanking(models.Model):
    customer_no = models.CharField(max_length = 255)
    # meter_no = models.CharField(max_length = 255)
    bill_no = models.IntegerField()
    bill_amount = models.DecimalField(max_digits=6,decimal_places=2)
    #phone_regex = RegexValidator(regex=r'^\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    mobile_no = models.CharField(max_length=17, blank=True) # validators should be a list
    #validators=[phone_regex],
    ssn = models.CharField(max_length=9)

class Cradit(models.Model):
    customer_no = models.CharField(max_length = 255)
    # meter_no = models.CharField(max_length = 255)
    bill_no = models.IntegerField()
    bill_amount = models.DecimalField(max_digits=6,decimal_places=2)
    card_number = models.PositiveIntegerField()
    cvv = models.PositiveIntegerField()
    expiry_date = models.CharField(max_length=7)
    