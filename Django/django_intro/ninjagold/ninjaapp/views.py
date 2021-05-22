from django.shortcuts import redirect, render
from time import gmtime, strftime
import random
def index(request):
    if 'geust'  in request.session:
        return render(request,'index.html')
    
    else :
        request.session["geust"]=0
        request.session["li"]=[]
        return redirect("/")

def process(request):
    if request.POST['process'] == 'process1':
        request.session["time"]=strftime("%Y-%m-%d %H:%M %p", gmtime())
        request.session['earn']=random.randint(10,20)
        request.session["geust"]+=request.session['earn']
        x= f"{request.session['geust']} earn from the farm at time {request.session['time']}"
        request.session["li"].append(x)
        request.session.save()
        return redirect('/')
    elif request.POST['process'] == 'process2':
        request.session['earn']= random.randint(5,10)
        request.session["time"]=strftime("%Y-%m-%d %H:%M %p", gmtime())
        request.session["geust"]+=request.session['earn']
        x= f"{request.session['geust']} earn from the Cave at time {request.session['time']}"
        request.session["li"].append(x)
        request.session.save()
        return redirect('/')
    elif request.POST['process'] == 'process3':
        request.session['earn']=random.randint(2,5)
        request.session["time"]=strftime("%Y-%m-%d %H:%M %p", gmtime())
        request.session["geust"]+=request.session['earn']
        x= f"{request.session['geust']} earn from the farm at time {request.session['time']}"
        request.session["li"].append(x)
        request.session.save()
        return redirect('/')
    elif request.POST['process'] == 'process4':
        request.session['earn']=random.randint(-50,50)
        request.session["time"]=strftime("%Y-%m-%d %H:%M %p", gmtime())
        request.session["geust"]+=request.session['earn']
        x= f"{request.session['geust']} earn from the Casino at time {request.session['time']}"
        request.session["li"].append(x)
        request.session.save()
        return redirect('/')
    else:
        return redirect('/')
