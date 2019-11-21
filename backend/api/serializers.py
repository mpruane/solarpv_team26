from rest_framework import serializers
from ..models import Client, Location, Test_Standard, Product, Test_Sequence, UserTbl, Certificate, Service, Performance_Data, Product_Factory, Factory_Inspection, Expertise

class ProductSerializer(serializers.ModelSerializer): 
	class Meta: 
		model = Product
		fields = ['ModelNum', 'Name',	'Cell_technology', 'Cell_manufacturer', 'Number_of_cells', 'Number_of_cells_in_series', 'Number_of_series_strings', 'Number_of_diodes', 'Product_length', 'Product_width', 'Product_weight', 'Superstrate_type', 'Superstrate_manufacturer', 'Substrate_type', 'Substrate_manufacturer', 'Frame_type', 'Frame_adhesive', 'Encapsulant_type', 'Encapsulant_manufacturer', 'Junction_box_type', 'Junction_box_manufacturer']

class CertificateSerializer(serializers.ModelSerializer): 
	class Meta: 
		model = Certificate
		fields = ['Cert_number', 'ID', 'UserID', 'Report_number', 'Cert_issue_date', 'Test_Standard', 'LocationID', 'Product']

class ServiceSerializer(serializers.ModelSerializer): 
	class Meta: 
		model = Service
		fields = ['ServiceID', 'ServiceName', 'Description', 'Is_FI_required', 'FI_Frequency', 'TestStandardID']

class ClientSerializer(serializers.ModelSerializer): 
	class Meta: 
		model = Client
		fields = ['ClientID', 'ClientCode', 'ClientName', 'ClientType']

class LocationSerializer(serializers.ModelSerializer): 
	class Meta: 
		model = Location
		fields = '__all__'

class Test_StandardSerializer(serializers.ModelSerializer): 
	class Meta: 
		model = Test_Standard
		fields = '__all__'

class Test_SequenceSerializer(serializers.ModelSerializer): 
	class Meta: 
		model = Test_Sequence
		fields = '__all__'

class UserTblSerializer(serializers.ModelSerializer): 
	class Meta: 
		model = UserTbl
		fields = '__all__' 

class Performance_DataSerializer(serializers.ModelSerializer): 
	class Meta: 
		model = Performance_Data
		fields = '__all__'

class Product_FactorySerializer(serializers.ModelSerializer): 
	class Meta: 
		model = Product_Factory
		fields = '__all__'

class Factory_InspectionSerializer(serializers.ModelSerializer): 
	class Meta: 
		model = Factory_Inspection
		fields = '__all__'

class ExpertiseSerializer(serializers.ModelSerializer): 
	class Meta: 
		model = Expertise
		fields = '__all__'
