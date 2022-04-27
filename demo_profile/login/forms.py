
from django.core import validators 
from django import forms
from .models import User, User1

CHOICES = [('male','Male'),('female','Female')]
# FRUIT_CHOICES= [
#     ('orange', 'Oranges'),
#     ('cantaloupe', 'Cantaloupes'),
#     ('mango', 'Mangoes'),
#     ('honeydew', 'Honeydews'),
#     ]
CHOICES_hobby =(
    ('reading','Reading'),
    ('dance','Dance'),
    ('drawing','Drawing')
)   





class UserReg(forms.ModelForm):
      gender=forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect()) #this 
    #   hobby = forms.MultipleChoiceField(widget = forms.CheckboxSelectMultiple,choices = CHOICES_hobby)
      hobby = forms.MultipleChoiceField(widget = forms.CheckboxSelectMultiple,choices = CHOICES_hobby)

      

      class Meta:
            model = User1
            fields = ['name','email','password','gender','hobby']

