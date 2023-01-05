from django.shortcuts import render , redirect , get_object_or_404
from django.http import HttpResponse , JsonResponse , HttpResponseRedirect
from books.models import Book
# Create your views here.
def bookshome(request):
    booksinfo = [
		{"id":1, "name":"book1", "description":"book1_description"},
		{"id":2, "name":"book2", "description":"book2_description"},
		{"id":3, "name":"book3", "description":"book3_description"}
    ]
    return render(request,"books/bookshome.html",context={"booksinfo" : booksinfo})

def aboutfun(request):
    return render(request,"books/about.html")

def contactusfun(request):
    return render(request,"books/contactus.html")

def getBook(request):
   booklist = Book.objects.all()
   return render(request,"books/book.html",context={"booklist":booklist})

def ShowBook(request,id):
    
    # onebook = Book.objects.get(id=id)
    onebook = get_object_or_404(Book,pk=id)
    return render(request,"books/showbook.html",context={"onebook":onebook})


def DeleteBook(request,id):
    delbook = Book.objects.get(id=id)
    delbook.delete()
    return redirect("book")