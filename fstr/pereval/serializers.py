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
    coords = CoordsSerializer(help_text="Координаты перевала")
    user = UserSerializer(help_text="Пользователь, добавивший перевал")
    images = ImageSerializer(many=True, help_text="Изображения перевала")

    class Meta:
        model = pereval_added
        fields = '__all__'
        
    def get_coords(self, obj):
        """Координаты перевала"""
        return CoordsSerializer(obj.coords_id).data

    def get_user(self, obj):
        """Пользователь, добавивший перевал"""
        return UserSerializer(obj.user).data

    def get_images(self, obj):
        """Изображения перевала"""
        pereval_images = PerevalImage.objects.filter(pereval=obj)
        return ImageSerializer([pereval_image.images for pereval_image in pereval_images], many=True).data


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