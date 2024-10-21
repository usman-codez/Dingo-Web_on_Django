from django import forms
from django.forms import PasswordInput

from .models import Udata
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class UserAuthen(forms.ModelForm):
    class Meta:
        model = Udata
        fields = ['message','name','email','sub']

        widgets = {
            'message': forms.Textarea(attrs={"class":"form-control w-100", "name":"message",
                                             "id":"message", "cols":"30", "rows":"9",
                    "onfocus":"this.placeholder = ''", "onblur":"this.placeholder = 'Enter Message'",
                    "placeholder":'Enter Message'}),
            'name': forms.TextInput(attrs={"class":"form-control", "name":"name", "id":"name",
                                           "type":"text", "onfocus":"this.placeholder = ''",
                    "onblur":"this.placeholder = 'Enter your name'", "placeholder":'Enter your name'}),
            'email': forms.EmailInput(attrs={"class": "form-control", "name": "email", "id": "email",
                                           "type": "email", "onfocus": "this.placeholder = ''",
                                           "onblur": "this.placeholder = 'Enter your email'",
                                           "placeholder": 'Enter your email'}),
            'sub': forms.TextInput(attrs={"class":"form-control", "name":"sub", "id":"subject",
                                          "type":"text", "onfocus":"this.placeholder = ''",
                    "onblur":"this.placeholder = 'Enter Subject'", "placeholder":'Enter Subject'}),
        }

class SignUp(UserCreationForm):
    password2 = forms.CharField(label='Password (again)',widget=PasswordInput() )
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']
        labels = {'email': 'Email'}




