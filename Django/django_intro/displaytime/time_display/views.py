from django.shortcuts import render
from time import gmtime, strftime
def index(request):
    request.session["time"]=strftime("%Y-%m-%d %H:%M %p", gmtime())
    return render(request,'index.html')