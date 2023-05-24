from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import SignupUserForm, AddRecordForm
from .models import Record

# Create your views here.
def home(request):
    records = Record.objects.all()
    
    
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
        return render(request, 'home.html', {'records':records})

def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out...")
    return redirect('home')

def signup_user(request):
    if request.method == 'POST':
        form = SignupUserForm(request.POST)
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
        form = SignupUserForm()
            
    return render(request, 'signup.html', {'form':form,} )


def student_record(request, pk):
    if request.user.is_authenticated:
        #Look Up Records
        student_record = Record.objects.get(id=pk)
        return render(request, 'record.html', {'student_record':student_record})
    else:
        messages.success(request,"You must be logged in...")
        return redirect('home')
        
def add_student(request):
    form = AddRecordForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                add_record = form.save()
                messages.success(request, "Recorded Added Successfully...")
                return redirect('home')
        return render(request, 'add_student.html', {'form':form})
    else:
        messages.success(request, "You must be logged in to add records")
        return redirect('home')
        
def update_record(request, pk):
    if request.user.is_authenticated:
        current_record = Record.objects.get(id=pk)
        form = AddRecordForm(request.POST or None, instance=current_record)
        if form.is_valid():
            form.save()
            messages.success(request, "Recorded Updated Successfully...")
            return redirect('home')
        return render(request, 'update_record.html', {'form':form})
    else:
        messages.success(request, "You must be logged in to Update records")
        return redirect('home')
        
def delete_record(request, pk):
    if request.user.is_authenticated:
        delete_it = Record.objects.get(id=pk)
        delete_it.delete()
        messages.success(request, "Record Successfully deleted...")
        return redirect('home')
    else:
        messages.success(request, "You are not authenticated...")
        return redirect('home')