from django.contrib import admin
from payment.models import NetBanking,bhimUPI,MobileBanking,Cradit

# Register your models here.

admin.site.register(NetBanking)
admin.site.register(bhimUPI)
admin.site.register(MobileBanking)
admin.site.register(Cradit)
