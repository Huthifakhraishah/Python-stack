from django import http
from django.shortcuts import redirect, render,HttpResponse
from .models import dojo, ninja
def index(request):
    context={
        "x" : dojo.objects.all(),
    }
    return render(request,"index.html",context)
def dojojo(request):
    dojo.objects.create(name =request.POST["name"],state =request.POST["state"],city =request.POST["city"])
    return redirect("/")
def ninjaja(request):
    ninja.objects.create(first_name =request.POST["first_name"],last_name =request.POST["last_name"],dojo =dojo.objects.get(name=request.POST["dojo"]))
    return redirect("/")
