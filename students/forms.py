from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Record

class SignupUserForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    first_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class':'form-control'}))
    
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')
        
    def __init__(self, *args, **kwargs):
        super(SignupUserForm, self).__init__(*args, **kwargs)
        
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'
        
class AddRecordForm(forms.ModelForm):
    matric_no = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder':'Matric No', 'class':'form-control'}), label="")
    first_name =forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder':'First Name', 'class':'form-control'}), label="")
    last_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder':'Last Name', 'class':'form-control'}), label="")
    faculty = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder':'Faculty', 'class':'form-control'}), label="")
    department = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder':'Deparment', 'class':'form-control'}), label="")
    email =  forms.EmailField(required=True, widget=forms.TextInput(attrs={'placeholder':'Email', 'class':'form-control'}), label="")
    gpa = forms.FloatField(required=True, widget=forms.TextInput(attrs={'placeholder':'GPA', 'class':'form-control'}), label="")
    class Meta:
       model = Record
       exclude = ("user",) 