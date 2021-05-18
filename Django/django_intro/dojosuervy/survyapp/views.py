
from django.shortcuts import redirect, render, HttpResponse
def index(request):
    return render(request,'server.html')
def indexresult(request):
    request.session['name']= request.POST['name']
    request.session['location'] = request.POST['location']
    request.session['favourite']=request.POST['favourite']
    request.session['comment']=request.POST['comment']
    request.session['radio']=request.POST['radio']
    request.session['check']=request.POST['check']
    return redirect('/thanks')
def indexresult1(request):
    return render(request,"result.html")