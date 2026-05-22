from .models import Course
from .serializers import CourseSerializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['POST'])
def create_course(request):
    course= request.data.get('course')
    v = CourseSerializers(data = request.data)
    if v.is_valid():
        v.save()
        return Response({'message':"Course Added",'data':v.data},status = status.HTTP_201_CREATED)
    else:
         return Response(v.errors,status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_course(request):
    a = Course.objects.all()
    serializers = CourseSerializers(a,many =True)
    return Response({'message':"User obtained",'data':serializers.data},status=status.HTTP_201_CREATED)
