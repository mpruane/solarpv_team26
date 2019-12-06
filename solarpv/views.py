from django.shortcuts import render
from .models import UserTbl
from .forms import RegisterForm


def about(request):
	return render(request, 'solarpv/about.html')

def blank(request):
	return render(request, 'solarpv/blank.html')

def contact(request):
	return render(request, 'solarpv/contact.html')

def index(request):
	return render(request, 'solarpv/index.html')

def login(request):
	return render(request, 'solarpv/login.html')

def register(request):
	form = RegisterForm()
	context = {'form' : form}
	return render(request, 'solarpv/register.html')

def testandcert(request):
	return render(request, 'solarpv/testandcert.html')