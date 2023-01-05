from django.urls import path
from books.views import bookshome , aboutfun ,contactusfun,getBook,ShowBook,DeleteBook

urlpatterns = [
    path('home', bookshome, name="home"),
    path('about', aboutfun , name="about"),
    path('contact', contactusfun , name="contact"),
    path('book', getBook , name="book"),
    path('book/showbook/<int:id>', ShowBook , name="showbook"),
    path('book/deletebook/<int:id>', DeleteBook , name="deletebook"),

    
]