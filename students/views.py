from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
def home(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        #Authenticate
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            messages.success(request, "Welcome, You have been logged in!")
            return redirect('home')
        else:
            messages.success(request, "Login Failed, Try again!!!")
            return redirect('home')
    else:
        return render(request, 'home.html', {})

def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out...")
    return redirect('home')

def signup_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            #Authenticate & Login
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "Signup Successful")
            return redirect('home')
    else:
        form = UserCreationForm()
            
    return render(request, 'signup.html', {'form':form,} )

