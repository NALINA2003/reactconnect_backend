from django.urls import path
from .views import create_course,get_course

urlpatterns=[
    path('create/',create_course,name=('create_course')),
    path('get/',get_course,name=('get_course'))
]