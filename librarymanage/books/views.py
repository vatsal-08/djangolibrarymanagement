from django.shortcuts import render
from .models import Book
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy


class BookListView(ListView):
    model = Book
    template_name = 'templates/base.html'


class BookDetailView(DetailView):
    model = Book
    template_name = 'templates/book_detail.html'


class BookUpdateView(LoginRequiredMixin, UpdateView):
    model = Book
    login_url = '/login'
    field = ["available", "desc"]


class BookDeleteView(LoginRequiredMixin, DeleteView):
    model = Book
    login_url = '/login'
    template_name = 'templates/delete_post.html'
    success_url = reverse_lazy('book-list')
