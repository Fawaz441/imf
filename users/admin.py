from django.contrib import admin
from .models import Student,Farmer,Company
# Register your models here.

admin.site.site_header = "Indus-Mega Farms"
admin.site.register(Student)
admin.site.register(Farmer)
admin.site.register(Company)
