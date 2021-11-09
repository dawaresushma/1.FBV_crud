from django.shortcuts import render, redirect
from .models import Laptop
from .forms import LaptopForm
# Create your views here.

def home(request):
    template_name='fapp/display.html'
    context={}
    return render(request,template_name,context)

def add_laptop(request):
    form=LaptopForm()
    if request.method=='POST':
        form=LaptopForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('display')
    template_name='fapp/add_laptop.html'
    context={'form':form}
    return render(request,template_name,context)


def display(request):
    obj=Laptop.objects.all()
    template_name='fapp/display.html'
    context={'obj':obj}
    return render(request,template_name,context)

def update(request,id):
    obj=Laptop.objects.get(id=id)
    form=LaptopForm(instance=obj)
    if request.method=='POST':
        form=LaptopForm(request.POST,instance=obj)
        if form.is_valid():
            form.save()
            return redirect('display')
    template_name='fapp/add_laptop.html'
    context={'form':form}
    return render(request,template_name,context)

def delete(request,id):
    obj=Laptop.objects.get(id=id)
    obj.delete()
    return redirect('display')
