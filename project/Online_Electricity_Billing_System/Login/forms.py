from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from Login.models import Login
#our code

class registrationForm(UserCreationForm):
    email           =forms.EmailField(max_length=60,help_text='Required. Add valid email address')

    class Meta:
        model = Login
        fields = ("email","username","password1","password2","Phone_number","meter_no")
    def clean(self):
        super(registrationForm,self).clean()
        meter_no = self.cleaned_data.get('meter_no')
        
        if len(meter_no) < 5:
            self.errors['meter_no'] = self.error_class(['Minimum 5 characters required in meter number'])

class LoginAuthenticationForm(forms.ModelForm):

	password 	=forms.CharField(label='password',widget = forms.PasswordInput)

	class Meta:
		model = Login
		fields = ("email","password")

	def clean(self):
		if self.is_valid():
			email = self.cleaned_data['email']
			password = self.cleaned_data['password']
			if not authenticate(email=email,password=password):
				raise forms.ValidationError("Invalid Login")
class AccountUpdateForm(forms.ModelForm):
	class Meta:
		model = Login	
		fields = ('email','username','Phone_number',"meter_no")

	def clean_email(self):
		if self.is_valid():
			email = self.cleaned_data['email']
			try :
				login = Login.objects.exclude(pk=self.instance.pk).get(email=email)
			except Login.DoesNotExist:
				return email
		else:
			raise forms.ValidationError('Emailid  "%s" is already in use.' %email)
	def clean_username(self):
		if self.is_valid():
			username = self.cleaned_data['username']
			try :
				login = Login.objects.exclude(pk=self.instance.pk).get(username=username)
			except Login.DoesNotExist:
				return username
		else:
			raise forms.ValidationError('Username "%s" is already in use.' %username)
	def clean_phone_number(self):
		if self.is_valid():
			Phone_number = self.cleaned_data['Phone_number']
			try :
				login = Login.objects.exclude(pk=self.instance.pk).get(Phone_number=Phone_number)
			except Login.DoesNotExist:
				return Phone_number
			raise forms.ValidationError('Phone_number "%s" is already in use.' %Phone_number)
	def clean_meter_no(self):
		if self.is_valid():
			meter_no = self.cleaned_data['meter_no']
			try :
				login = Login.objects.exclude(pk=self.instance.pk).get(meter_no=meter_no)
			except Login.DoesNotExist:
				return meter_no
			raise forms.ValidationError('meter number "%s" is already in use.' %meter_no)