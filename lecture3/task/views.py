from django.shortcuts import render
from django  import forms
from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.


class newtaskform(forms.Form):
    task=forms.CharField(label="New Task")
    priority=forms.IntegerField(label="priority",min_value="1",max_value="10")


def index(request):
    if "task" not in request.session:
        request.session["task"]=[]
    return render(request,"task/index.html",{
        "task":request.session["task"]
    })

def add(request):
    if request.method =="POST":
        form=newtaskform(request.POST)
        if form.is_valid:
            tasks=form.cleaned_data["task"]
            request.session["task"]+=["task"]
            return HttpResponseRedirect(reverse("task:index"))
        else:
             return render(request,"task/add.html",{
        "form":form
        })
         
def add(request):
    return render(request,"task/add.html",{
        "form":newtaskform
    })
 
