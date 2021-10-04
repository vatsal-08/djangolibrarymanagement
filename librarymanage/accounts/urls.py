from django.contrib.auth.views import LogoutView
from django.urls import path
from .views import *

urlpatterns = [
    path('/login', CustomLoginView.as_view(), name='login'),
    path('/signup', RegisterPage.as_view(), name='signup'),
    path('/forgotpass', LogoutView.as_view(next_page='login'), name='logout'),
]
