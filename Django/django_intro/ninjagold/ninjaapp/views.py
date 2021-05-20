from django.shortcuts import redirect, render
from time import gmtime, strftime
import random
def index(request):
    if 'geust' not in request.session:
        request.session['count']=1
        request.session["geust"]=0
        return render(request,'index.html')
    else:
        context={
            "num":int(request.session['count'])
        }
        return render(request,'index.html',context)
def process(request):
    if request.POST['process'] == 'process1':
        request.session['count']+=1
        request.session['earn']=random.randint(10,20)
        request.session["geust"]+=request.session['earn']
        return redirect('/')
    elif request.POST['process'] == 'process2':
        request.session['count']+=1
        request.session['earn']= random.randint(5,10)
        request.session["geust"]+=request.session['earn']
        return redirect('/')
    elif request.POST['process'] == 'process3':
        request.session['count']+=1
        request.session['earn']=random.randint(2,5)
        request.session["geust"]+=request.session['earn']
        return redirect('/')
    elif request.POST['process'] == 'process4':
        request.session['count']+=1
        request.session['earn']=random.randint(-50,50)
        request.session["geust"]+=request.session['earn']
        return redirect('/')
    else:
        return redirect('/')