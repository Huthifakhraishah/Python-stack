from django.shortcuts import render
def index(request):
    return render(request,"index.html")
def data(request):
    request.session["firstname"]=request.POST["firstname"]
    request.session["lastname"]=request.POST["lastname"]
    request.session["email"]=request.POST["email"]
    request.session["age"]=request.POST["age"]
    return render(request,"index.html")