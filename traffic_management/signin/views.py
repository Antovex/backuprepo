from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.
def home(request):
    return HttpResponse("Hello home")

def signin(request):
    return render(request, 'signin/login.html')

def signup(request):
    if request.method == "POST":
        username = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']

        myuser = User.objects.create_user(username, email, password)
        myuser.save()

        messages.success(request, "Your account has been successfully created")
        return redirect('signin')

    return render(request, 'signin/register.html')

def signout(request):
    pass