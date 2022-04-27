from http.client import HTTPResponse
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render,HttpResponseRedirect
from .forms import UserReg
from login.models import User, User1


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
            


          
              x =','.join(hb)
              y = str(x)
              print("44444444444444444444",y)


              reg = User(name=nm,email=em,password=pw,gender=gen,hobby=y)
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

def insert_data(request):
      if request.method == 'POST':
            name=request.POST['name']
            print("---------------",name)


            email=request.POST['email']
            print("---------------",email)

            password=request.POST['pwd']
            print("---------------",password)

            gender=request.POST['gen']
            print("---------------",gender)

            # hobby=request.POST['hobby']
            # print("---------------",hobby)
            # some_var = request.POST.getlist('checks[]')
            hobby = request.POST.getlist('hobby[]')
            print("------->>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>",hobby)

            x =''.join(hobby)
            hobby=str(x)
            print("***************************************",hobby)
            print("-----------------------------",request.POST)
            fm1=User1(name=name, email=email, password=password, gender=gender, hobby=hobby)
            fm1.save()

      return render(request,'login/reg.html') 

def get_data(request):
      get_d= User1.objects
      return render(request,'login/reg.html',{'gd':get_d})
