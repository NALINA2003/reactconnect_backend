from .models import Student
from .serializers import StudentSerializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(['POST'])
def create_student(request):
    name= request.data.get('name')
    parent_name = request.data.get('parent_name')
    age = request.data.get('age')
    phone_number = request.data.get('phone_number')
    email = request.data.get('email')
    course = request.data.get('course')
    v = StudentSerializers(data = request.data)
    if v.is_valid():
        v.save()
        return Response({'message':"student Added Successfully",'data':v.data},status = status.HTTP_201_CREATED)
    else:
         return Response(v.errors,status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET'])
def get_student(request):
    a = Student.objects.all()
    serializers = StudentSerializers(a,many =True)
    return Response({'message':"User obtained",'data':serializers.data},status=status.HTTP_201_CREATED)



