from django.urls import path
from .views import create_books,get_books,get_books_id,delete_books,update_books,mailSend


urlpatterns=[
    path('create/',create_books,name=('create_books')),
    path("get/",get_books,name=('get_books')),
    path("get/<int:pk>",get_books_id,name=('get_books_id')),
    path("delete/<int:pk>",delete_books,name=('delete_books')),
    path("update/<int:pk>",update_books,name=('update_books')),
    path("Contact/",mailSend,name=('contact'))
]