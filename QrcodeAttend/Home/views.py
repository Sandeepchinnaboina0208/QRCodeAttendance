from django.db.models import Q
from django.shortcuts import render, redirect
from .models import Login,Contact
def home(request):
    return render(request,'Home/home.html')

def login(request):
    return render(request,'Home/login.html')

def register(request):
    return render(request,'Home/register.html')

def home2(request):
    return render(request,'Home/home2.html')

def contactus(request):
    return  render(request,'Home/contact.html')

def about(request):
    return render(request,'Home/about.html')

def checklogin(request):
    name = request.POST["username"]
    password = request.POST["pwd"]
    flag = Login.objects.filter(Q(username=name) & Q(password=password))
    print(flag)

    if flag:
        return redirect('Home-home2')
    else:
        return redirect('Home-login')

def addregister(request):
    if request.method == 'POST':
        name = request.POST['username']
        password = request.POST['pwd']
        new_id =Login(username=name, password=password)
        new_id.save()
        return redirect('Home-home')

def contactsave(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message=request.POST['message']
        new_id = Contact(name=name,email=email,message=message)
        new_id.save()
        return redirect('Home-home2')

