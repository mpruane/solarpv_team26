from django.db import models

class Client(models.Model):
	ClientID = models.IntegerField(primary_key=True)
	ClientCode = models.IntegerField() 
	ClientName = models.CharField(max_length=50)
	ClientType = models.CharField(max_length=50) 

	def __str__(self):
		return self.name

class Location(models.Model):
	LocationID = models.IntegerField(primary_key=True)
	Address1 = models.CharField(max_length=50)
	Address2 = models.CharField(max_length=50)
	City = models.CharField(max_length=50)
	State = models.CharField(max_length=50)
	Postalcode = models.IntegerField()
	Country = models.CharField(max_length=50)
	Phonenumber = models.IntegerField()
	Faxnumber = models.IntegerField()
	ClientID = models.ForeignKey(Client, on_delete=models.CASCADE)

	def __str__(self):
		return self.name

class Test_Standard(models.Model):
	StandardID = models.IntegerField(primary_key=True)
	Standard_Name = models.CharField(max_length=50)
	Description = models.CharField(max_length=50)
	Published_Date = models.DateField()

	def __str__(self):
		return self.name

class Product(models.Model):
	ModelNum = models.IntegerField(primary_key=True)
	Name = models.CharField(max_length=50)
	Cell_technology = models.CharField(max_length=50)
	Cell_manufacturer = models.CharField(max_length=50)
	Number_of_cells = models.IntegerField()
	Number_of_cells_in_series = models.IntegerField()
	Number_of_series_strings = models.IntegerField()
	Number_of_diodes = models.IntegerField()
	Product_length = models.FloatField()
	Product_width = models.FloatField()
	Product_weight = models.FloatField()
	Superstrate_type = models.CharField(max_length=50)
	Superstrate_manufacturer = models.CharField(max_length=50)
	Substrate_type = models.CharField(max_length=50)
	Substrate_manufacturer = models.CharField(max_length=50)
	Frame_type = models.CharField(max_length=50)
	Frame_adhesive = models.CharField(max_length=50)
	Encapsulant_type = models.CharField(max_length=50)
	Encapsulant_manufacturer = models.CharField(max_length=50)
	Junction_box_type = models.CharField(max_length=50)
	Junction_box_manufacturer = models.CharField(max_length=50)

	def __str__(self):
		return self.name
#-------------
class Test_Sequence(models.Model):
	SequenceID = models.IntegerField(primary_key=True)
	Sequence_Name= models.CharField(max_length=50)

	def __str__(self):
		return self.name

class UserTbl(models.Model):
	UserID = models.IntegerField(primary_key=True)
	Firstname = models.CharField(max_length=50)
	Middlename = models.CharField(max_length=50)
	Lastname = models.CharField(max_length=50)
	Jobtitle = models.CharField(max_length=50)
	Email = models.EmailField() 
	Officephone = models.IntegerField()
	Cellphone = models.IntegerField()
	Prefix = models.CharField(max_length=50)
	Isstaff = models.BooleanField()
	ClientID = models.ForeignKey(Client, on_delete=models.CASCADE)

	def __str__(self):
		return self.name

class Certificate(models.Model):
	Cert_number = models.IntegerField(primary_key=True)
	ID = models.IntegerField() 
	UserID = models.ForeignKey(UserTbl, on_delete=models.CASCADE)
	Report_number = models.IntegerField()
	Cert_issue_date = models.DateField()
	Test_Standard = models.ForeignKey(Test_Standard, on_delete=models.CASCADE)
	LocationID = models.ForeignKey(Location, on_delete=models.CASCADE)
	Product = models.ForeignKey(Product, on_delete=models.CASCADE)

	def __str__(self):
		return self.name

class Service(models.Model):
	ServiceID = models.IntegerField(primary_key=True)
	ServiceName = models.CharField(max_length=50)
	Description = models.CharField(max_length=250)
	Is_FI_required = models.BooleanField()
	FI_Frequency = models.IntegerField()
	TestStandardID = models.ForeignKey(Test_Standard, on_delete=models.CASCADE)

	def __str__(self):
		return self.name

class Performance_Data(models.Model):
	ModelNum = models.ForeignKey(Product, on_delete=models.CASCADE)
	Test_Sequence = models.ForeignKey(Test_Sequence, on_delete=models.CASCADE)
	Max_system_voltage = models.FloatField()
	Open_circuit_voltage_VOC = models.FloatField()
	Short_circuit_current_ISC = models.FloatField()
	Voltage_at_max_power_VMP = models.FloatField()
	Current_at_max_power_IMP = models.FloatField()
	Max_power_output_PMP = models.FloatField()
	Fill_factor_FF = models.FloatField()

	def __str__(self):
		return self.name

class Product_Factory(models.Model):
	LocationID = models.ForeignKey(Location, on_delete=models.CASCADE)
	ProductID = models.ForeignKey(Product, on_delete=models.CASCADE)
	Contact = models.ForeignKey(Client, on_delete=models.CASCADE)

	def __str__(self):
		return self.name

class Factory_Inspection(models.Model):
	ID = models.IntegerField(primary_key=True)
	ReportNum = models.IntegerField()
	Date = models.DateField()
	Inspection_sequence = models.IntegerField()
	Findings = models.CharField(max_length=50)
	LocID = models.ForeignKey(Location, on_delete=models.CASCADE)
	Inspector = models.ForeignKey(Client, on_delete=models.CASCADE)
	Cert_number = models.ForeignKey(Certificate, on_delete=models.CASCADE)

	def __str__(self):
		return self.name

class Expertise(models.Model):
	Certification = models.CharField(max_length=50)
	StandardID = models.ForeignKey(Test_Standard, on_delete=models.CASCADE)
	UserID = models.ForeignKey(UserTbl, on_delete=models.CASCADE)

	def __str__(self):
		return self.name