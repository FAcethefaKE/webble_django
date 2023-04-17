from django.contrib.auth.views import LoginView
from django.urls import path
from . import views

urlpatterns = [
    path('', LoginView.as_view(), name='login'),
    path('sign_up/', views.sign_up, name='sign_up'),
    path('books', views.book_list, name='books'),
]
