from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.exceptions import ValidationError



class CreateUserForm(UserCreationForm):
  username = forms.CharField(required=True, max_length=30, ) 
  email = forms.EmailField(required=True)
    
  class Meta:
    model = User
    fields = ['username', 'email', 'password1', 'password2']
    
    
    def clean(self):
        cleaned_data = super.clean()
        if User.objects.filter(username=cleaned_data["username"].exists()):
            raise ValidationError("این نام کاربری از قبل موجود است!")
        elif User.objects.filter(email=cleaned_data["email"].exists()):
            raise ValidationError("این ایمیل از قبل موجود است!")
    