from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login
from django.http import  HttpResponse

def signupform(request):
    if request.method =='POST':
        info = UserCreationForm(request.POST)
        
        if info.is_valid():
            info.save()
            u_name     = info.cleaned_data['username']
            u_password = info.cleaned_data['password1']
            user       = authenticate(username = u_name , password = u_password)
            login(request,user)
            return render(request,'info.html',{'user':user})
    else:
        info = UserCreationForm()
    return render(request,'signupform.html',{'form':info})
    
# def login_view(request):
#     username = request.POST['username']
#     password = request.POST['password']
#     user     = authenticate(request,username,password)
#     if user is not None:
#         login(request,user)
#         return RequestContext(request, {'foo': 'bar', })
#
