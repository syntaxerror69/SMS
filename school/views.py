from django.shortcuts import render,redirect
from .forms import StudentForm
from .models import Students

# Create your views here.

def homepage(req):
    form = StudentForm(req.POST or None)
    if req.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect(homepage)

    return render(req, 'home.html', {'form':form, 'students': Students.objects.all()})   


def deleteStudent(req, id):
    student = Students.objects.get(pk=id)   
    student.delete()  
    return redirect(homepage)

def editStudent(req, id):
    Student = Students.objects.get(pk=id)
    form = StudentForm(req.POST or None, instance=Student)

   
    if req.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect(homepage)
       
    return render(req, 'edit.html', {'form':form})

def searchStudent(req):
    if req.method == 'GET':
        search_query = req.GET.get('search')
        form = StudentForm(req.POST or None)
        #context 
        data = {
            'students' : Students.objects.filter(name__icontains=search_query),
            'form' : form
        }
    return render(req, 'home.html', data)   

def filtercity(req):
    if req.method == 'GET':
        search = req.GET.get('city')
        form = StudentForm()
        data = {
            'form': form,
            'students' : Students.objects.filter(city=search)
        } 
    return render(req, "home.html", data)       