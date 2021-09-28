from django.contrib import admin
from django.urls import path
from .views import BookListView, BookDetailView, BookUpdateView
urlpatterns = [
    path('books/', BookListView.as_view(), name="book-list"),
    path('books/<int:pk>/', BookDetailView.as_view(), name="book-detail"),
    path('books/<int:pk>/edit', BookUpdateView.as_view(), name="book-edit"),
    path('books/<int:pk>/', BookDetailView.as_view(), name="book-borrow"),
]
