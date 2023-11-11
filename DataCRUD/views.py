

from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login

def index(request):
    if request.method == 'POST':
        fname= request.POST.get('firstname')
        lname= request.POST.get('lastname')
        email= request.POST.get('email')
        username= request.POST.get('username')
        password= request.POST.get('password')
        cPassword= request.POST.get('confirmPassword')
        if password!=cPassword:
            return HttpResponse('Not Match')
        else: 
            myuser =User.objects.create_user(first_name = fname, last_name=lname, email=email, username=username, password=password)
            myuser.save()
            return redirect('loginPage')
    return render(request, 'index.html')

def loginPage(request):
    if request.method=="POST":
        username=request.POST.get("username")
        pass1=request.POST.get("password")
        user=authenticate(request,username=username,password=pass1)
        
        if user is not None:
            login(request,user)
            return HttpResponse("username found")
        else:
            return HttpResponse("username not found")
    
    return render(request,"login.html")