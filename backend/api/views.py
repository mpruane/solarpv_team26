from rest_framework import generics
from ..models import Client, Location, Test_Standard, Product, Test_Sequence, UserTbl, Certificate, Service, Performance_Data, Product_Factory, Factory_Inspection, Expertise
from .serializers import ClientSerializer, LocationSerializer, Test_StandardSerializer, ProductSerializer, Test_SequenceSerializer, UserTblSerializer, CertificateSerializer, ServiceSerializer, Performance_DataSerializer, Product_FactorySerializer, Factory_InspectionSerializer, ExpertiseSerializer
class ClientListView(generics.ListAPIView): 
	queryset = Client.objects.all() 
	serializer_class = ClientSerializer
class ClientDetailView(generics.RetrieveAPIView): 
	queryset = Client.objects.all() 
	serializer_class = ClientSerializer

class LocationListView(generics.ListAPIView): 
	queryset = Location.objects.all() 
	serializer_class = LocationSerializer
class LocationDetailView(generics.RetrieveAPIView): 
	queryset = Location.objects.all() 
	serializer_class = LocationSerializer

class Test_StandardListView(generics.ListAPIView): 
	queryset = Test_Standard.objects.all() 
	serializer_class = Test_StandardSerializer
class Test_StandardDetailView(generics.RetrieveAPIView): 
	queryset = Test_Standard.objects.all() 
	serializer_class = Test_StandardSerializer

class ProductListView(generics.ListAPIView): 
	queryset = Product.objects.all() 
	serializer_class = ProductSerializer
class ProductDetailView(generics.RetrieveAPIView): 
	queryset = Product.objects.all() 
	serializer_class = ProductSerializer

class Test_SequenceListView(generics.ListAPIView): 
	queryset = Test_Sequence.objects.all() 
	serializer_class = Test_SequenceSerializer
class Test_SequenceDetailView(generics.RetrieveAPIView): 
	queryset = Test_Sequence.objects.all() 
	serializer_class = Test_SequenceSerializer

class UserTblListView(generics.ListAPIView): 
	queryset = UserTbl.objects.all() 
	serializer_class = UserTblSerializer
class UserTblDetailView(generics.RetrieveAPIView): 
	queryset = UserTbl.objects.all() 
	serializer_class = UserTblSerializer

class CertificateListView(generics.ListAPIView): 
	queryset = Certificate.objects.all() 
	serializer_class = CertificateSerializer
class CertificateDetailView(generics.RetrieveAPIView): 
	queryset = Certificate.objects.all() 
	serializer_class = CertificateSerializer

class ServiceListView(generics.ListAPIView): 
	queryset = Service.objects.all() 
	serializer_class = ServiceSerializer
class ServiceDetailView(generics.RetrieveAPIView): 
	queryset = Service.objects.all() 
	serializer_class = ServiceSerializer

class Performance_DataListView(generics.ListAPIView): 
	queryset = Performance_Data.objects.all() 
	serializer_class = Performance_DataSerializer
class Performance_DataDetailView(generics.RetrieveAPIView): 
	queryset = Performance_Data.objects.all() 
	serializer_class = Performance_DataSerializer

class Product_FactoryListView(generics.ListAPIView): 
	queryset = Product_Factory.objects.all() 
	serializer_class = Product_FactorySerializer
class Product_FactoryDetailView(generics.RetrieveAPIView): 
	queryset = Product_Factory.objects.all() 
	serializer_class = Product_FactorySerializer

class Factory_InspectionListView(generics.ListAPIView): 
	queryset = Factory_Inspection.objects.all() 
	serializer_class = Factory_InspectionSerializer
class Factory_InspectionDetailView(generics.RetrieveAPIView): 
	queryset = Factory_Inspection.objects.all() 
	serializer_class = Factory_InspectionSerializer

class ExpertiseListView(generics.ListAPIView): 
	queryset = Expertise.objects.all() 
	serializer_class = ExpertiseSerializer
class ExpertiseDetailView(generics.RetrieveAPIView): 
	queryset = Expertise.objects.all() 
	serializer_class = ExpertiseSerializer