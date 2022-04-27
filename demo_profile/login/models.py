

from django.db import models




CHOICES = [('male','Male'),('female','Female')]
CHOICES_hobby =[
    ('reading','Reading'),
    ('dance','Dance'),
    ('drawing','Drawing')
]   



# hobby=[('reading','Reading'),('dance','Dance'),('drawing','Drawing')]

# Create your models here.
class User(models.Model):
      name=models.CharField(max_length=70,null = True,blank = True )
      email=models.EmailField()
      password=models.CharField(max_length=100)
      # gender=models.CharField(max_length=20, default="male")
      gender=models.CharField(max_length=255, choices=CHOICES)
      # hobby=models.CharField(max_length=255, choices=CHOICES_hobby,default='dance')
     
      hobby = models.CharField(max_length = 255,null = True,blank = True )
 


      # Gender=models.CharField(label='Gender', widget=models.RadioSelect(choices=CHOICES))
  


# GENDER_CHOICES = (
#    ('M', 'Male'),
#    ('F', 'Female')
# )

# class Profile(models.Model):
#      gender = models.CharField(choices=GENDER_CHOICES, max_length=128)



class User1(models.Model):
 
      name=models.CharField(max_length=70)
      email=models.EmailField()
      password=models.CharField(max_length=100)
      # gender=models.CharField(max_length=20, default="male")
      gender=models.CharField(max_length=255, choices=CHOICES)
      # hobby=models.CharField(max_length=255, choices=CHOICES_hobby,default='dance')
     
      hobby = models.CharField(max_length = 255, choices=CHOICES_hobby,default='dance')
 
     