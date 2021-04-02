from django.db import models
from django.conf import settings
from Login.models import Login


# Create your models here.

class Generate_Bill(models.Model):
	key = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
	bill_no = models.IntegerField(default=1)
	unit = models.IntegerField()
	amount = models.DecimalField(max_digits=6,decimal_places=2)
	month = models.DateField(verbose_name="paid_month",auto_now_add=True)

def __str__(self):
    return "[ Bill_no:"+self.bill_no+" , Date:"+self.month+" ]"

class Payment_Status(models.Model):
	key_id = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name = ('id')
    )
	date = models.ForeignKey(
		Generate_Bill,
		on_delete=models.CASCADE,
		verbose_name = ('month')
		)
	detail = models.TextField(blank=True)
	status = models.BooleanField(default=False)

def __str__(self):
    return "[ Username:"+self.key_id.username+" , Date:"+self.date.month+" , status:"+self.status+" ]"
    
    