from django.shortcuts import redirect, render
from bookapp.models import Books , Authors

def index(request):
    context={
        "all_books" : Books.objects.all(), 
    }
    return render (request,'index.html',context)

def index2(request):
    context={
        "all_authors" : Authors.objects.all(),
    }
    return render (request,'index2.html',context)
def add(request):
    Books.objects.create(title=request.POST['title'],desc=request.POST['desc'])
    return redirect ('/')
def add2(request):
    Authors.objects.create(first_name=request.POST['firstname'],last_name=request.POST['lastname'],notes=request.POST['notes'])
    return redirect ('/authors')
def view(request , id):
    context={
        "all_books":Books.objects.get(id=id),
        "all":Books.objects.get(id=id).authors.all(),
        "all_authers":Authors.objects.all(),
    }
    request.session["id"]=id
    return render (request,'index3.html',context)
def adduth(request):
    a=Books.objects.get(id=request.session["id"])
    b = Authors.objects.get(id=int(request.POST["selects"]))
    a.authors.add(b)
    a.save()
    return redirect(f"books/{request.session['id']}")
def view2(request , id):
    context={
        "all_authors" : Authors.objects.get(id=id),
        "all":Authors.objects.get(id=id).books_authors.all(),
        "all_books":Books.objects.all(),
    }
    request.session["id2"]=id
    return render (request,'index4.html',context)
def addbook(request):
    a=Authors.objects.get(id=request.session["id"])
    b = Books.objects.get(id=int(request.POST["selects"]))
    a.books_authors.add(b)
    a.save()
    return redirect(f"authors/{request.session['id2']}")