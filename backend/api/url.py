from django.urls import path
from . import views
app_name = 'backend'
urlpatterns = [ 
	path('Client/', views.ClientListView.as_view(), name='client_list'), 
	path('Client/<pk>/', views.ClientDetailView.as_view(), name='client_detail'),
	path('Location/', views.LocationListView.as_view(), name='location_list'), 
	path('Location/<pk>/', views.LocationDetailView.as_view(), name='location_detail'),
	path('Test_Standard/', views.Test_StandardListView.as_view(), name='Test_Standard_list'), 
	path('Test_Standard/<pk>/', views.Test_StandardDetailView.as_view(), name='Test_Standard_detail'),
	path('Product/', views.ProductListView.as_view(), name='Product_list'), 
	path('Product/<pk>/', views.ProductDetailView.as_view(), name='Product_detail'),
	path('Test_Sequence/', views.Test_SequenceListView.as_view(), name='Test_Sequence_list'), 
	path('Test_Sequence/<pk>/', views.Test_SequenceDetailView.as_view(), name='Test_Sequence_detail'),
	path('UserTbl/', views.UserTblListView.as_view(), name='UserTbl_list'), 
	path('UserTbl/<pk>/', views.UserTblDetailView.as_view(), name='UserTbl_detail'),
	path('Certificate/', views.CertificateListView.as_view(), name='Certificate_list'), 
	path('Certificate/<pk>/', views.CertificateDetailView.as_view(), name='Certificate_detail'),
	path('Service/', views.ServiceListView.as_view(), name='Service_list'), 
	path('Service/<pk>/', views.ServiceDetailView.as_view(), name='Service_detail'),
	path('Performance_Data/', views.Performance_DataListView.as_view(), name='Performance_Data_list'), 
	path('Performance_Data/<pk>/', views.Performance_DataDetailView.as_view(), name='Performance_Data_detail'),
	path('Product_Factory/', views.Product_FactoryListView.as_view(), name='Product_Factory_list'), 
	path('Product_Factory/<pk>/', views.Product_FactoryDetailView.as_view(), name='Product_Factory_detail'),
	path('Factory_Inspection/', views.Factory_InspectionListView.as_view(), name='Factory_Inspection_list'), 
	path('Factory_Inspection/<pk>/', views.Factory_InspectionDetailView.as_view(), name='Factory_Inspection_detail'),
	path('Expertise/', views.ExpertiseListView.as_view(), name='Expertise_list'), 
	path('Expertise/<pk>/', views.ExpertiseDetailView.as_view(), name='Expertise_detail')
]
