from .models import Users
from rest_framework import serializers

class Userserializers(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['id','name','email','age','phone_number','password']