from django.shortcuts import render, redirect
from django.http import HttpResponse
from . models import bookstoremodel

# Create your views here.

def home(request):
    return HttpResponse("home page book")

def show_book(request):
    book = bookstoremodel.objects.all()
    
    return render(request,'show_book.html', {'book': book})


def borrow_book(request,id):
    book = bookstoremodel.objects.get(pk = id)
    if book.available_book:
        book.available_book = book.available_book - 1
        book.save()
        books = bookstoremodel.objects.all()
        return render(request,'show_book.html', {'book': books})
    else :
        return HttpResponse("Your request has send")
    
    
def search_book(request):
    print(request.POST.get('username'))
    if request.method == 'POST':
        book = request.POST.get('username')
    return render(request,'one_book.html', {'book': book})
    return HttpResponse("ok")

def search(request):
    if request.method == 'POST':
        try:
            name =  request.POST.get('username')
            book = bookstoremodel.objects.get(title=name)
            return render(request,'one_book.html',{'book': book})
        except:
            return HttpResponse('No book found')
    else:
        return render(request,'search.html')