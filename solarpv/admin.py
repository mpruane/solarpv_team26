from django.contrib import admin

from .models import Client, Location, Product, Test_Standard, Certificate

admin.site.register(Client)
admin.site.register(Location)
admin.site.register(Product)
admin.site.register(Test_Standard)
admin.site.register(Certificate)


# Register your models here.
