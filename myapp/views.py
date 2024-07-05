from django.shortcuts import render, redirect
from myapp.models import Student

# Create your views here.

def home(request):
    std = Student.objects.all()
    return render(request, 'index.html', {'std': std})

def add_std(request):
    if request.method == "POST":
        roll = request.POST['roll']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['contact']
        address = request.POST['address']

        
        s = Student()
        s.roll = roll
        s.name = name
        s.email = email
        s.phone = phone
        s.address = address
        s.save()
        return redirect('/home/')
    return render(request, 'add_std.html')

def delete(request, roll):
    s = Student.objects.get(pk=roll)
    s.delete()
    return redirect("/home/")

def update(request, roll):
    s = Student.objects.get(pk=roll)
    return render(request, "update_std.html", {"std": s})

def do_update(request, roll):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['contact']
        address = request.POST['address']

        s = Student.objects.get(pk=roll)
        s.name = name
        s.email = email
        s.phone = phone
        s.address = address
        s.save()
        return redirect('/home/')

def add_image(request):
    return render(request,'add_image.html')