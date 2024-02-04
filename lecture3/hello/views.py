from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request,"hello/index.html")

def some(request):
    return HttpResponse("hello shakeel")

def greet(request,name):
    return render(request,"hello/greet.html",{
        "name":name
    })