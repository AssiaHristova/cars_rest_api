from django.contrib.auth.models import User, Group
from rest_framework import serializers

from accounts.models import Profile
from cars.models import UserCar


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'user_cars', 'user_brands']


class RegisterSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['password'])
        user.set_password(validated_data['password'])
        user.save()
        return user


class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.HyperlinkedRelatedField(view_name='user-detail', queryset=User.objects.all())

    class Meta:
        model = Profile
        fields = ['url', 'first_name', 'last_name', 'age', 'gender', 'user']
