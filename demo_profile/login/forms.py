
from django.core import validators 
from django import forms
from .models import User
CHOICES = [('Male','Male'),('female','Female')]
FRUIT_CHOICES= [
    ('orange', 'Oranges'),
    ('cantaloupe', 'Cantaloupes'),
    ('mango', 'Mangoes'),
    ('honeydew', 'Honeydews'),
    ]


class UserReg(forms.ModelForm):
      gender=forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect()) #this 
      class Meta:
            model = User
            fields = ['name','email','password','gender','hobby']

      