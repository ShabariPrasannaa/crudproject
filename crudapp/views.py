from os import name
from django import forms
from django.shortcuts import render,redirect
from crudapp.models import Student
from crudapp.forms import StudentForm

# Create your views here.
def retrive_view(request):
    student = Student.objects.all()
    return render(request, 'crudApps/index.html', {'student':student})

def create_view(request):
    form = StudentForm()
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/check')
    return render(request, 'crudApps/create.html', {'form':form})

def delete_view(request,id):
    student = Student.objects.get(id=id)
    student.delete()
    return redirect('/check')    

def update_view(request,id):
    student = Student.objects.get(id=id)
    if request.method == 'POST':
        form = StudentForm(request.POST,instance=student)
        if form.is_valid():
            form.save()
            return redirect('/check')
    return render(request, 'crudApps/update.html', {'student':student})
