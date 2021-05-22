from django import http
from django.shortcuts import redirect, render,HttpResponse
from .models import user
def index(request):
    context={
        "x" : user.objects.all()
    }
    return render(request,"index.html",context)
def data(request):
    user.objects.create(first_name =request.POST["firstname"],secand_name =request.POST["lastname"],email_address =request.POST["email"],age =request.POST["age"])
    return redirect("/")
def get(request,id):
    contxt={
        "huti":user.objects.get(id=id)
    }
    return render(request,"qamarway.html",contxt)