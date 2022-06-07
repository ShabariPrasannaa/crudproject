from django.contrib import admin
from crudapp.models import Student

# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list = ['sno','sname','sclass','saddress']

admin.site.register(Student, StudentAdmin)
