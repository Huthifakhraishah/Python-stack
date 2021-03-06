from django.http.response import HttpResponse
from django.shortcuts import render,redirect,HttpResponse
from myapp.models import User
from django.contrib import messages
import bcrypt
def index(request):
    if "user" in request.session:
        return redirect("/welcome")
    else:
        return render(request,"index.html")
def login(request):
        # username=request.POST["username"]
        # passwd=request.POST["passwd"]
        # if request.POST["username"] != "" and request.POST["passwd"] !="" and len(username)>2 and len(passwd)>10 and User.objects.filter(username=username) ==True:
        #     user=User.objects.get(username=username)
        #     if user.username == username  :
        #         data={
        #                 "username":user.username,
        #                 "password":user.password,
        #                 "email":user.email,
        #                 "address":user.address
        #         }
        #         request.session["user"]=data
        #         return redirect("/welcome")
        #         return redirect("/")
        #     return redirect("/")
        #         # for i in User.objects.all():
        #         #     if username==i.username and passwd==i.password:
        #         #         data={
        #         #             "username":i.username,
        #         #             "password":i.password,
        #         #             "email":i.email,
        #         #             "address":i.address
        #         #         }
        #         #         request.session["user"]=data
        #         #         return redirect("/welcome")
        # return redirect("/ssssssssss")
    errors = User.objects.basic_log(request.POST)
    if len(errors)>0:
        for key, value in errors.items():
                messages.error(request, value)
        return redirect('/')
    else:    
        username =request.POST['username']
        passwd =request.POST['passwd']
        users =User.objects.filter(username = username)
        if len(users) ==0:
            return redirect('/')
        user =users.first()
        if bcrypt.checkpw(request.POST['passwd'].encode(), user.password.encode()):
            data={
            "username":user.username,
            "password":user.password,
            "address":user.address,
            "email":user.email
            }
            request.session['user'] = data
            return redirect('/welcome')
def reg(request):
    errors = User.objects.basic_validator(request.POST)
    if len(errors)>0:
        for key, value in errors.items():
                messages.error(request, value)
        return redirect('/')
    else:  
        username=request.POST["username"]
        email=request.POST["email"]
        address=request.POST["address"]
        passwd=request.POST["passwd"]
        pw_hash = bcrypt.hashpw(passwd.encode(), bcrypt.gensalt()).decode()
        if request.POST["username"] != "" and request.POST["passwd"] !="" and len(username)>2 and len(passwd)>3  :
            data={
                "username":username,
                "password":passwd,
                "email":email,
                "address":address
            }
            user=User.objects.create(username=username,email=email,address=address,password=pw_hash)
            request.session["user"]=data
            return redirect("/welcome")
    return redirect("/")
def welcome(request):
    if "user" in request.session:
        user=request.session["user"]
        return render(request,"welcome.html",user)
    return redirect("/")
def logout(request):
    if "user" in request.session:
        request.session.clear()
        return redirect("/")
    return redirect("/")