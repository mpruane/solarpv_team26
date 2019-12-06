from django.db import models
from django.apps import apps

class Client(models.Model):
	ClientID = models.IntegerField(primary_key=True)
	ClientCode = models.IntegerField()
	ClientName = models.CharField(max_length=50)
	ClientType = models.CharField(max_length=50)

	def __str__(self):
 		return self.ClientName

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

class Test_Standard(models.Model):
	StandardID = models.IntegerField(primary_key=True)
	Standard_Name = models.CharField(max_length=50)
	Description = models.CharField(max_length=50)
	Published_Date = models.DateField()

	def __str__(self):
 		return self.name

class Certificate(models.Model):
	ID = models.IntegerField()
	Cert_number = models.IntegerField(primary_key=True)
	Report_number = models.IntegerField()
	Cert_issue_date = models.DateField()
	LocationID = models.ForeignKey(Location, on_delete=models.CASCADE)
	ContactID = models.ForeignKey(Client, on_delete=models.CASCADE)
	Test_Standard = models.ForeignKey(Test_Standard, on_delete=models.CASCADE)
	Product = models.ForeignKey(Product, on_delete=models.CASCADE)

	def __str__(self):
 		return self.name

class UserTbl(models.Model):
	UserID = models.AutoField(primary_key=True)
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
		return self.Firstname + " " + self.Lastname