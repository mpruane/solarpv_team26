from django.urls import path

from . import views

urlpatterns = [
	path('about/', views.about, name='about'),
	path('blank/', views.blank, name='blank'),
	path('contact/', views.contact, name='contact'),
	path('', views.index, name='index'),
	path('login/', views.login, name='login'),
	path('register/', views.register, name='register')
]