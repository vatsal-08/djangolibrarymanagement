from django.shortcuts import render
from .models import Book
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin


class BookListView(ListView):
    model = Book
    template_name = 'templates/base.html'


class BookDetailView(DetailView):
    model = Book


class BookUpdateView(LoginRequiredMixin, UpdateView):
    model = Book
    login_url = '/login'
