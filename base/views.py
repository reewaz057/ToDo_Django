from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Student

def home(request):
    new_obj = Student.objects.all()
    context = {'new': new_obj}
    return render(request, 'index.html', context)

def create(request):
    if request.method == "POST":
        name = request.POST.get('name')
        description = request.POST.get('description')
        status = request.POST.get('status')
        Student.objects.create(name=name, description=description, status=status)
        return redirect('home')
    return render(request, 'create.html')

def edit(request,pk):
    new_objs = Student.objects.get(id=pk)
    context = {"news":new_objs}
   
    if request.method == "POST":
        new_objs.name = request.POST.get('name')
        new_objs.description = request.POST.get('description')
        new_objs.status = request.POST.get('status')
        new_objs.save()
        return redirect('home')
    return render(request, 'edit.html',context)

def delete(request,pk):
    new_objs = Student.objects.get(id=pk)
    new_objs.delete()
    return redirect('home')

  
    
    