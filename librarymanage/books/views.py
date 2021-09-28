from django.shortcuts import render
from .models import Book
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView

# Create your views here.


class BookListView(ListView):
    model = Book


class BookDetailView(DetailView):
    model = Book


class BookUpdateView(UpdateView):
    model = Book
