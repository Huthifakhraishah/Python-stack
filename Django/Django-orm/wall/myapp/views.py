from django.core.checks import messages
from django.http.response import HttpResponse
from django.shortcuts import render,redirect,HttpResponse
from myapp.models import Users,Messages,Comments
def index(request):
    if "user" in request.session:
        context={
                    "messages":Messages.objects.all().order_by("-created_at"),
                    "comments":Comments.objects.all().order_by("-created_at"),
                }
        return render(request,"post.html",context)
    else:
        return render(request,"log-reg.html")
def login(request):
    email =request.POST['email']
    passwd =request.POST['passwd']
    users =Users.objects.filter(email = email)
    if len(users) ==0:
        return redirect('/')
    user =users.first()
    if  user.password != passwd:
        return redirect('/')
    data={
        "first_name":user.first_name,
        "last_name":user.last_name,
        "password":user.password,
        "email":user.email,
    }
    request.session['u_id'] = user.id
    request.session['user'] = data
    return redirect("/")
def reg(request):
    first_name=request.POST["first_name"]
    last_name=request.POST["last_name"]
    email=request.POST["email"]
    passwd=request.POST["passwd"]
    if request.POST["first_name"] != "" and request.POST["last_name"] != "" and request.POST["passwd"] !="" and len(first_name)>2 and len(passwd)>5  :
        data={
        "first_name":first_name,
        "last_name":last_name,
        "password":passwd,
        "email":email,
        }
        user=Users.objects.create(first_name=first_name,last_name=last_name,email=email,password=passwd)
        request.session["user"]=data
        request.session['u_id'] = user.id
        return redirect("/")
    return redirect("/")
def welcome(request):
    if "user" in request.session:
        user=request.session["user"]
        return render(request,"post.html",user)
    return redirect("/")
def logout(request):
    if "user" in request.session:
        request.session.clear()
        return redirect("/")
    return redirect("/")
def posting(request):
    Messages.objects.create(message=request.POST["postM"], user = Users.objects.get(id = request.session['u_id']))
    return redirect("/")
def commenting(request,id):
    Comments.objects.create(comment=request.POST["postC"], user = Users.objects.get(id = request.session['u_id']),
    message=Messages.objects.get(id = id))
    return redirect("/")