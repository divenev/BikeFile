from rest_framework import serializers
from BikeFile.bike.models import Bike, TypeBike, GalleryBike


class TypeBikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeBike
        fields = ['name']


class GalleryBikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = GalleryBike
        fields = ['img_url']


class BikeSerializer(serializers.ModelSerializer):
    type_bike = TypeBikeSerializer()
    img = GalleryBikeSerializer()

    class Meta:
        model = Bike
        fields = ['id', 'frame_number', 'type_bike', 'brand', 'model', 'tire_size',
                  'frame_size', 'status', 'img', 'doc_img', 'price_for_sale',
                  'description', 'location', 'owner']

    def create(self, validated_data):
        # Обработка на полето 'type_bike'
        type_bike_data = validated_data.pop('type_bike', None)
        if type_bike_data:
            type_bike_name = type_bike_data.get('name')
            try:
                type_bike = TypeBike.objects.get(name__istartswith=type_bike_name)
            except TypeBike.DoesNotExist:
                # To create a bike type, by name. Without the raise row
                # type_bike = TypeBike.objects.create(name=type_bike_name)
                msg = ('There is no \'Type bicy\' filled')
                raise serializers.ValidationError(msg)
            validated_data.update({'type_bike': type_bike})

        # Обработка на полето 'img'
        img_data = validated_data.pop('img', None)
        if img_data:
            img_url = img_data.get('img_url')
            # Ако има изображение, създаваме ново
            if img_url:
                img = GalleryBike.objects.create(img_url=img_url)
                validated_data.update({'img': img})
        else:
            validated_data.pop('img')

        return Bike.objects.create(**validated_data)

    def update(self, instance, validated_data):
        # Обработка на полето 'type_bike'
        type_bike_data = validated_data.pop('type_bike', None)
        if type_bike_data:
            type_bike_name = type_bike_data.get('name')
            try:
                type_bike = TypeBike.objects.get(name__istartswith=type_bike_name)
            except TypeBike.DoesNotExist:
                msg = ('There is no \'Type bicycle\' filled')
                raise serializers.ValidationError(msg)
            instance.type_bike = type_bike

        # Обработка на полето 'img'
        img_data = validated_data.pop('img', None)
        if img_data:
            img_url = img_data.get('img_url')
            if img_url:
                # Ако има ново изображение, създаваме ново или актуализираме съществуващо
                img, created = GalleryBike.objects.update_or_create(
                    id=instance.img.id if instance.img else None,
                    defaults={'img_url': img_url}
                )
                instance.img = img
            else:
                # Ако няма изображение, изтриваме текущото изображение
                if instance.img:
                    img_id = instance.img.id
                    GalleryBike.objects.filter(id=img_id).update(img_url=None)

        # Актуализиране на останалите полета
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        # Записваме актуализираните данни
        instance.save()
        return instance

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        type_bike = representation.pop('type_bike')
        if type_bike:
            # type_bike = {('type_bike', type_bike['name'])}
            type_bike = {('type_bike', type_bike[key]) for key in type_bike}
            representation.update(type_bike)
        img = representation.pop('img')
        if img:
            # img = {('img', img['img_url'])}
            img = {('img', img[key]) for key in img}
            representation.update(img)
        return representation