from django.shortcuts import redirect, render
import random 	             
def index(request):
    request.session['random']=random.randint(1, 100) 
    return render(request,'index.html')
def check(request):
    if request.session['random']==int(request.POST['name']):
        request.session['guess']=True
        return render(request,'check.html')
    elif request.session['random'] < int(request.POST['name']):
        request.session['guess']=False
        request.session['text']="number too high"
        return render(request,'check.html')
    else:
        request.session['guess']=False
        request.session['text']="number too low"
        return render(request,'check.html')


