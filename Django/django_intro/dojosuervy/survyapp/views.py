
from django.shortcuts import redirect, render, HttpResponse
def index(request):
    return render(request,'server.html')
# def indexresult(request):
#     return redirect('/thanks')
def indexresult(request):
    print("Got Post Info....................")
    name= request.POST['name']
    location = request.POST['location']
    favourite=request.POST['favourite']
    comment=request.POST['comment']
    radio=request.POST['radio']
    check=request.POST['check']
    context={
        'name':name ,
        'location':location,
        'favourite':favourite,
        'comment':comment,
        'radio':radio,
        'check':check
    }
    return render(request,"result.html",context)