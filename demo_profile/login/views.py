from django.shortcuts import render,HttpResponseRedirect
from .forms import UserReg
from login.models import User


# Create your views here.



def add_data(request):
      if request.method == 'POST':
            fm = UserReg(request.POST)
            # if fm.is_valid():                # 1st method
            #  fm.save()

            if fm.is_valid():                  # 2nd method
              nm = fm.cleaned_data['name']
              em = fm.cleaned_data['email']
              pw = fm.cleaned_data['password']
              gen=fm.cleaned_data['gender']
              hb=fm.cleaned_data['hobby']
              reg = User(name=nm,email=em,password=pw,gender=gen,hobby=hb)
              fm.save()        
              fm=UserReg()


      else:
            fm=UserReg()
      stud =User.objects.all()   
      return render(request,'login/user_reg.html',{'form':fm,'stu':stud})


# delete :-
def dele(request,id):
 if request.method == "POST":
       pi=User.objects.get(pk=id)
       pi.delete() 
       return HttpResponseRedirect('/')