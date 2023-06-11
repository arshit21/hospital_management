from django.forms import CharField, EmailField, PasswordInput, Form, Select, TextInput
from .models import User
from django.contrib.auth.forms import UserCreationForm

Department_Choices = [
    ('ENT', 'ENT'),
    ('Cardiology', 'Cardiology'),
    ('Neurology', 'Neurology'),
    ('Oncology', 'Oncology'),
    ('Orthopedics', 'Orthopedics'),
    ('Pediatrics', 'Pediatrics'),
]

Gender_Choices = [
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Other', 'Other'),
]

class StaffForm(Form):
    department = CharField(label='Department',widget=Select(choices=Department_Choices)) 

class UserRegisterForm(UserCreationForm):
    first_name = CharField(max_length=101)
    last_name = CharField(max_length=101)
    gender = CharField(label='Gender', widget=Select(choices=Gender_Choices))
    email = EmailField()
    
    class Meta:
        model = User
        fields = ['first_name','last_name', 'username', 'email', 'gender', 'password1', 'password2']

class UserLoginForm(Form):
    username = CharField(max_length=100)
    password = CharField(max_length=100, widget=PasswordInput)

class TextForm(Form):
    text = CharField(max_length=10000, widget=TextInput)
