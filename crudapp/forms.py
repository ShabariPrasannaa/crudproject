from django import forms
from django.db.models import fields
from django.db.models.base import Model
from crudapp.models import Student

# Create your models here.
class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'

