from django.shortcuts import render
from django.views.generic import ListView, DetailView
from rest_framework import viewsets
from .models import Book
from .serializers import BookSerializer

class BookListView(ListView):
    model = Book
    template_name = 'books/book_list.html'
    context_object_name = 'books'
class BookDetailView(DetailView):
    model = Book
    template_name = 'books/book_detail.html'
    context_object_name = 'book'

class BookViewSet(viewsets.ModelViewSet):

    queryset = Book.objects.all()
    serializer_class = BookSerializer