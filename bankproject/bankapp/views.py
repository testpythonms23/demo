from django.shortcuts import render, get_object_or_404, redirect
from .models import Branch,Customer
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.models import  User
from .forms import CustomerForm

# Create your views here.
def index(request):
    return render(request, 'index.html')


def home(request):
    return redirect('/')


def allbranch(request, c_slug=None):
    branches = None
    c_page = None
    if c_slug != None:
        c_page = get_object_or_404(Branch, slug=c_slug)
        branches = Branch.objects.all().filter(district=c_page)
    else:
        branches = Branch.objects.all()
    return render(request, 'branch.html', {'branches': branches})


def login(request):
    return render(request, 'login.html')

def welcome(request):
    return render(request,'welcome.html')

def updatekyc(request):

    if request.method =="POST":
        fcust = CustomerForm(request.POST)
        if fcust.is_valid():
            fcust.save()
            messages.success(request, 'Your application sumitted successfully')
            return redirect('/')
    else:
        fcust = CustomerForm()
    return render(request,'kyc.html',{'fcust':fcust})

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Welcome {username}.Your login has been created successfully')
            return redirect('/login/')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})
