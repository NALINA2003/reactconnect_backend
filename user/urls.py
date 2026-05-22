from django.urls import path
from .views import create_user,get_user,get_user_id,update_user,delete_user,login_user

urlpatterns=[
    path("create/",create_user,name=('create_user')),
    path("get/",get_user,name=('get_user')),
    path("get/<int:pk>/",get_user_id,name=('get_user_id')),
    path("update/<int:pk>/",update_user,name=('update_user')),
    path("delete/<int:pk>",delete_user,name=('delete_user')),
    path('login/',login_user,name='login')

]