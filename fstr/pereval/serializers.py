from rest_framework import serializers
from .models import Coords, User, pereval_added, images, PerevalImage

class CoordsSerializer(serializers.ModelSerializer):
     class Meta:
         model = Coords
         fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = images
        fields = '__all__'

class PerevalSerializer(serializers.ModelSerializer):
     coords = CoordsSerializer()
     user = UserSerializer()
     images = ImageSerializer(many=True)

     class Meta:
         model = pereval_added
         fields = '__all__'

     def create(self, validated_data):
         coords_data = validated_data.pop('coords')
         user_data = validated_data.pop('user')
         images_data = validated_data.pop('images')

         coords = Coords.objects.create(**coords_data)
         user, created = User.objects.get_or_create(
             email=user_data.get('email'),
             defaults=user_data
         )

         pereval = pereval_added.objects.create(coords_id=coords, user=user, **validated_data)

         for image_data in images_data:
             image = images.objects.create(**image_data)
             PerevalImage.objects.create(pereval=pereval, images=image)
         return pereval