from django.urls import path
from .views import create_student,get_student

urlpatterns = [
    path('create/',create_student,name=('create_student')),
    path('get/',get_student,name=('get_student'))
]