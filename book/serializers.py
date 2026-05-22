from rest_framework import serializers
from .models import Books,Contact



class Userserializers(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = Books
        fields = '__all__'

    def get_image(self, obj):
        request = self.context.get('request')
        if obj.image:
            return request.build_absolute_uri(obj.image.url)
        return None
    
class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'