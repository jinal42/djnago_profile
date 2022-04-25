from django.db import models




CHOICES = [('Male','Male'),('female','Female')]

hobby=[('reading','Reading'),('dance','Dance'),('drawing','Drawing')]

# Create your models here.
class User(models.Model):
      name=models.CharField(max_length=70)
      email=models.EmailField(max_length=100)
      password=models.CharField(max_length=100)
      # gender=models.CharField(max_length=20, default="male")
      gender=models.CharField(max_length=10, choices=CHOICES)
      hobby=models.CharField(max_length=10, choices=hobby,default='dance')
      

      # Gender=models.CharField(label='Gender', widget=models.RadioSelect(choices=CHOICES))
  


# GENDER_CHOICES = (
#    ('M', 'Male'),
#    ('F', 'Female')
# )

# class Profile(models.Model):
#      gender = models.CharField(choices=GENDER_CHOICES, max_length=128)