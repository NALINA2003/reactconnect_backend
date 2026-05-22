from .models import Users
from .serializers import Userserializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(['POST'])
def create_user(request):
    mail=request.data.get('email')
    age = request.data.get('age')
    phone_number = request.data.get('phone_number')
    passs=request.data.get('password')
    confirm=request.data.get('confirm')
    v = Userserializers(data = request.data)
    if len(phone_number) != 10:
        return Response({'message':"Invalid Phone Number"},status=status.HTTP_400_BAD_REQUEST)   
    if age < 18:
        return Response({'message':"Invalid Age"},status=status.HTTP_400_BAD_REQUEST)
    if Users.objects.filter(email=mail).exists():
        return Response({'message':"Email already exists"},status=status.HTTP_400_BAD_REQUEST)
    if passs!=confirm:
        return Response({'message':"Password doestnt match"},status=status.HTTP_400_BAD_REQUEST)
    if v.is_valid():
        v.save()
        return Response({'message':"User Added",'data':v.data},status = status.HTTP_201_CREATED)
    else:
        return Response(v.errors,status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def login_user(request):
    mail=request.data.get('email')
    password=request.data.get('password')  
    if Users.objects.filter(email=mail).exists():
        a=Users.objects.get(email=mail)
        seri=Userserializers(a)
        if a.password==password:
            return Response({'message':"login successfull",'data':seri.data},status = status.HTTP_201_CREATED)
        else:
            return Response({'message':"Password invalid"},status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response({'message':"Email not exists"},status=status.HTTP_400_BAD_REQUEST)
            



@api_view(['PUT'])
def update_user(request,pk):
     a = Users.objects.get(pk = pk)
     v = Userserializers(a,data = request.data)
     if v.is_valid():
        v.save()
        return Response({'message':"User Added",'data':v.data},status = status.HTTP_201_CREATED)
     else:
        return Response(v.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_user(request):
    a = Users.objects.all()
    serializers = Userserializers(a,many =True)
    return Response({'message':"User obtained",'data':serializers.data},status=status.HTTP_201_CREATED)

@api_view(['GET'])
def get_user_id(request,pk):
     a = Users.objects.get(pk=pk)
     serializers = Userserializers(a)
     return Response({'message':"User obtained",'serializers':serializers.data},status=status.HTTP_201_CREATED)


@api_view(['DELETE'])
def delete_user(request,pk):
    a=Users.objects.get(pk = pk)
    a.delete()
    return Response({'message':"Deleted Successfully"},status=status.HTTP_200_OK)
