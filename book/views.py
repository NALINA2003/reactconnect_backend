from .models import Books,Contact
from .serializers import Userserializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render
from learn.settings import EMAIL_HOST_USER
from django.core.mail import send_mail
import random
from .serializers import ContactSerializer

@api_view(['POST'])
def create_books(request):
    v = Userserializers(data = request.data)
    if v.is_valid():
        v.save()
        return Response({'message':"Books Added",'data':v.data},status = status.HTTP_201_CREATED)
    else:
        return Response(v.errors,status=status.HTTP_400_BAD_REQUEST)




@api_view(['PUT'])
def update_books(request,pk):
     a = Books.objects.get(pk = pk)
     v = Userserializers(a,data = request.data)
     if v.is_valid():
        v.save()
        return Response({'message':"Books Added",'data':v.data},status = status.HTTP_201_CREATED)
     else:
        return Response(v.errors,status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_books(request):
    author=request.query_params.get('author')
    journel= request.query_params.get('journel')
    date= request.query_params.get('date')
    a = Books.objects.all()
    if author:
        a=a.filter(author_name__exact=author)
    if journel:
        a = a.filter(general__contains=journel)
    if date:
        a = a.filter(date__exact=date)
    serializers = Userserializers(a,many =True,context={"request":request})
    return Response({'message':"Books obtained",'data':serializers.data},status=status.HTTP_201_CREATED)

@api_view(['GET'])
def get_books_id(request,pk):
     a = Books.objects.get(pk=pk)
     serializers = Userserializers(a)
     return Response({'message':"Books obtained",'serializers':serializers.data},status=status.HTTP_201_CREATED)


@api_view(['DELETE'])
def delete_books(request,pk):
    a=Books.objects.get(pk = pk)
    a.delete()
    return Response({'message':"Deleted Successfully"},status=status.HTTP_200_OK)

@api_view(['POST'])
def mailSend(request):
    email=request.data.get('email')
    name=request.data.get('name')
    otp=''
    for i in range(6):
        digit=random.randint(0,9)
        otp+=str(digit)

    serializer=ContactSerializer(data=request.data)
    if serializer.is_valid():
        subject="Welcome to Alo Infotech – You're In!"
        message=f"Hi {name},Thanks for subscribing to Alo Infotech news_letter!{otp}"
        recipient_list=[email]
        send_mail(subject,message,EMAIL_HOST_USER,recipient_list,fail_silently=True)
        serializer.save()
        return Response({'message': 'Contact created', 'Contact': serializer.data},status=status.HTTP_201_CREATED)
    return Response(serializer.error_messages,status=status.HTTP_400_BAD_REQUEST)