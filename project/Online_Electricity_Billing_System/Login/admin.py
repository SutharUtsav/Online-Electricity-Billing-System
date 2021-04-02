from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from Login.models import Login
# Register your models here.

class LoginAdmin(UserAdmin):
    list_display = ('email','username','Phone_number','date_joined','last_login','is_admin')
    search_fields = ('email','username')
    redonly_fields =('date_joined','last_login',)

    filter_horizontal   =()
    list_filter         =(['email','username','is_admin'])
    list_filter         =(['email','username','date_joined'])
    fieldsets           =()
admin.site.register(Login,LoginAdmin)
