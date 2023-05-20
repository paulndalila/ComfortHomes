from django import forms
from django.contrib.auth.forms import AuthenticationForm

from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from .models import User, Customer,Owner

class CustomerSignUpForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}),label='First Name')
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}),label='Last Name')
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}),label='Username')
    phone = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}),label='Phone')
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}),label='email')
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}), label='Password')
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}), label='Confirm password')



    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('first_name', 'last_name', 'username', 'phone', 'email', 'password1', 'password2')

    @transaction.atomic
    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_customer = True
        if commit:
            user.save()
        customer = Customer.objects.create(user=user, first_name=self.cleaned_data.get('first_name'), last_name=self.cleaned_data.get('last_name'),username=self.cleaned_data.get('username'),phone=self.cleaned_data.get('phone'), email=self.cleaned_data.get('email'))
        return user





class OwnerSignUpForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}),label='email')
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}), label='Password')
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}), label='Confirm password')
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}),label='First Name')
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}),label='Username')
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}),label='Last Name')
    phone = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}),label='Phone')
    photo = forms.ImageField(widget=forms.ClearableFileInput(attrs={'class': 'form-control'}), label='Photo', required=False)

    id_number = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}),label='Id_Number')

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('first_name', 'last_name', 'username', 'phone', 'email','photo','id_number', 'password1', 'password2')

    @transaction.atomic
    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_owner = True
        if commit:
            user.save()
        owner = Owner.objects.create(user=user, first_name=self.cleaned_data.get('first_name'), last_name=self.cleaned_data.get('last_name'),username=self.cleaned_data.get('username'), email=self.cleaned_data.get('email'), phone=self.cleaned_data.get('phone'), photo=self.cleaned_data.get('photo'), id_number=self.cleaned_data.get('id_number'))
        return user
    
    
class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput())