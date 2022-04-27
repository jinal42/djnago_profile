from django.contrib import admin
from .models import User, User1 


# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
 list_display=('id','name','email','password','gender','hobby')



@admin.register(User1)
class UserAdmin1(admin.ModelAdmin):
 list_display=('id','name','email','password','gender','hobby')