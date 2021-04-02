from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager
from django.core.validators import RegexValidator

# Create your models here.
class MyLogin_manager(BaseUserManager):
    def create_user(self,email,username,Phone_number,meter_no,password=None):
        if not email:
            raise ValueError("User must have an email")
        if not username:
            raise ValueError("User must have a username")
        if not Phone_number:
            raise ValueError("User must enter Phone number")
        if not meter_no:
            raise ValueError("User must enter meter_no")

        user    = self.model(
                            email=self.normalize_email(email),
                            username = username,
                            Phone_number=Phone_number,
                            meter_no = meter_no,
                            )
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self,email,username,Phone_number,meter_no,password):
        user    = self.create_user(
                            email=self.normalize_email(email),
                            username = username,
                            Phone_number=Phone_number,
                            password=password,
                            meter_no=meter_no,
                            
                            )  
        user.is_admin = True
        user.is_staff = True  
        user.is_superuser = True  
        user.save(using=self._db)
        return user



class Login(AbstractBaseUser):
    email               =models.EmailField(verbose_name="email",max_length=60,unique=True)
    username            =models.CharField(max_length=30 , unique=True)
    date_joined         =models.DateTimeField(verbose_name="date_joined",auto_now_add=True)
    last_login          =models.DateTimeField(verbose_name="last_login",auto_now=True)
    is_admin            =models.BooleanField(default=False)
    is_active           =models.BooleanField(default=True)
    is_staff            =models.BooleanField(default=False)
    is_superuser        =models.BooleanField(default=False)
    phone_regex        =RegexValidator(regex=r'^\d{9,13}$', message="Phone number must be entered in the format: '999999999'. Up to 13 digits allowed.")
    Phone_number        =models.CharField(validators=[phone_regex], max_length=17, blank=True) # validators should be a list
    meter_no            =models.CharField(max_length=10,unique=True, default=0)

    USERNAME_FIELD      ="email"
    REQUIRED_FIELDS     = ["username","Phone_number","meter_no"]

    objects = MyLogin_manager()

    def __str__(self):
        return "[ Email:"+self.email+" , User name:"+self.username+" ]"
    def has_perm(self,perm,obj=None):
        return self.is_admin
    def has_module_perms(self,app_lable):
        return True