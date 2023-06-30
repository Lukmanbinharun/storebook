from django.shortcuts import render,redirect
from . forms import ragester
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.

def home(request):
    return render(request,'home.html')

def ragestation(request):
    if request.method == 'POST':
        form = ragester(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else: 
        form = ragester()
    return render(request,'ragestation.html' ,{'form' : form})

def userlogin(request):
    if  not request.user.is_authenticated:
        form = AuthenticationForm()
        if request.method == 'POST':
            form = AuthenticationForm(request=request, data = request.POST)
            if form.is_valid():
                name = form.cleaned_data['username']
                userpassword = form.cleaned_data['password']
                user = authenticate(username = name, password = userpassword)
                if user is not None:
                    login(request=request,user=user)
                    return redirect('profile')
        return render(request,'login.html',{'form': form})
    return redirect('profile')

def userlogout(request):
    logout(request)
    return redirect('login')

def profile(request):
    if  request.user.is_authenticated:
        return render(request,'profile.html')
    else:
        return redirect('login')