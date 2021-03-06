from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from .views import BookListView, BookDetailView, BookUpdateView, BookDeleteView
urlpatterns = [
    path('books/', BookListView.as_view(), name="book-list"),
    path('books/<int:pk>/', BookDetailView.as_view(), name="book-detail"),
    path('books/<int:pk>/edit', BookUpdateView.as_view(), name="book-edit"),
    path('books/<int:pk>/borrow', BookDetailView.as_view(), name="book-borrow"),
    path('books/<int:pk>/delete', BookDeleteView.as_view(), name='book-delete')
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
