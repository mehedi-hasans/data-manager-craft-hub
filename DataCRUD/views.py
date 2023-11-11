

from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User

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
    return render(request, 'login.html')