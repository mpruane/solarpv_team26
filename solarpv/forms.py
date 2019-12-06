from django import forms
from .models import UserTbl

class RegisterForm(forms.Form):
	#UserID = forms.CharField(max_length=20)
	FirstName = forms.CharField(max_length=50)
	#Middlename = forms.CharField(max_length=50)
	#Lastname = forms.CharField(max_length=50)
	#Jobtitle = forms.CharField(max_length=50)
	#Email = forms.CharField(max_length=50)
	#Officephone = forms.CharField(max_length=50)
	#Cellphone = forms.CharField(max_length=50)
	#Prefix = forms.CharField(max_length=50)
	#Isstaff = forms.CharField(max_length=50)
	#ClientID = forms.CharField(max_length=50)