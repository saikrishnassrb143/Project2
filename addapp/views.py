from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return render(request,'home.html')
def add(request):
    x=request.POST["t1"]
    y=request.POST["t2"]
    i=int(x)
    j=int(y)
    z=i+j
    res=HttpResponse("The sum is: "+str(z))
    return res
def sub(request):
    x=request.POST["t1"]
    y=request.POST["t2"]
    i=int(x)
    j=int(y)
    z=i-j
    res=HttpResponse("The sum is: "+str(z))
    return res

def div(request):
    x=request.POST["t1"]
    y=request.POST["t2"]
    i=int(x)
    j=int(y)
    z=i/j
    res=HttpResponse("The sum is: "+str(z))
    return res

def mul(request):
    x=request.POST["t1"]
    y=request.POST["t2"]
    i=int(x)
    j=int(y)
    z=i*j
    res=HttpResponse("The sum is: "+str(z))
    return res



