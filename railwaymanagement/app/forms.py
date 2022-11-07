from django.forms import ModelForm
import django.forms as forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from crispy_forms import helper
from crispy_forms.layout import Submit
from app.models import *

class RegisterForm(ModelForm):
    confirm_password = forms.CharField(widget=forms.PasswordInput(),required=True)
    email = forms.EmailField(widget=forms.EmailInput(),required=True)
    first_name = forms.CharField(widget=forms.TextInput(),required=True)
    helper = helper.FormHelper()
    helper.add_input(Submit('Register','Register',css_class='btn btn-primary w-100'))
    helper.form_method = 'post'
    helper.form_action = '/register/'


    class Meta:
        model = User
        fields = ['first_name', 'email' , 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }



class LoginForm(ModelForm):

    email = forms.EmailField(widget=forms.EmailInput(),required=True)
    helper = helper.FormHelper()
    helper.add_input(Submit('Login','Login',css_class='btn btn-primary w-100'))
    helper.form_method = 'post'
    helper.form_action = '/login/'

    class Meta:
        model = User
        fields = ['email' , 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }
        

class AddBookingForm(ModelForm):
    helper = helper.FormHelper()
    helper.add_input(Submit('Add','Add',css_class='btn btn-primary w-100'))
    helper.form_method = 'post'
    helper.form_action = '/admin/addbooking/'

    class Meta:
        model = Train
        fields = ['name', 'from_station', 'to_station', 'departure_time', 'arrival_time', 'total_seats', 'price']
        widgets = {
            'departure_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'arrival_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }



class EditBookingForm(ModelForm):
    helper = helper.FormHelper()
    helper.add_input(Submit('Edit','Edit',css_class='btn btn-primary w-100'))
    helper.form_method = 'post'
    helper.form_action = '/admin/edit/'
    helper.form_id = 'edit-train-form'

    class Meta:
        model = Train
        fields = ['name', 'from_station', 'to_station', 'departure_time', 'arrival_time', 'total_seats', 'price']
        widgets = {
            'departure_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'arrival_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }
