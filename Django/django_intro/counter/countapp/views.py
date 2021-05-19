from django.shortcuts import redirect, render

def index(request):
    if 'count' in request.session:
        request.session["count"]+=1
        return render(request,'home.html')
    
    else:
        request.session['count'] =0
        return render(request,'home.html')
def destroy(requset):
    requset.session.clear()
    return redirect('/')

def addtwo(request):
    request.session["count"]+=1
    return redirect("/")

def inp(request):
    request.session['count'] += int(request.POST['inp'])-1
    return redirect('/')