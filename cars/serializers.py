from rest_framework import serializers

from cars.models import CarBrand, CarModel, UserCar


class CarBrandSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    brand_models = serializers.HyperlinkedRelatedField(many=True, read_only=True,
                                                       view_name='carmodel-detail')

    class Meta:
        model = CarBrand
        fields = ['id', 'name', 'user', 'brand_models']


class CarModelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CarModel
        fields = ['id', 'name', 'car_brand']


class UserCarSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = UserCar
        fields = ['id', 'first_reg', 'odometer', 'user', 'car_brand', 'car_model']
