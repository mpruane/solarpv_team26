from django.contrib import admin

from .models import Client, Location, Test_Standard, Product, Test_Sequence, UserTbl, Certificate, Service, Performance_Data, Product_Factory, Factory_Inspection, Expertise

admin.site.register(Client)
admin.site.register(Location)
admin.site.register(Test_Standard)
admin.site.register(Product)
admin.site.register(Test_Sequence)
admin.site.register(UserTbl)
admin.site.register(Certificate)
admin.site.register(Service)
admin.site.register(Performance_Data)
admin.site.register(Product_Factory)
admin.site.register(Factory_Inspection)
admin.site.register(Expertise)

# Register your models here.
