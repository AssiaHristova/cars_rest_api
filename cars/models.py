from django.db import models
from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone
from django_filters import DateFromToRangeFilter, NumberFilter
from django_filters.rest_framework import FilterSet

from cars.manager import SoftDeleteManager
UserModel = get_user_model()


class SoftDeleteModel(models.Model):

    deleted_at = models.DateTimeField(null=True, default=None)
    objects = SoftDeleteManager()
    all_objects = models.Manager()

    def soft_delete(self):
        self.deleted_at = timezone.now()
        self.save()

    def restore(self):
        self.deleted_at = None
        self.save()

    class Meta:
        abstract = True


class CarBrand(SoftDeleteModel):
    name = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(UserModel, related_name='user_brands', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['created_at']


class CarModel(SoftDeleteModel):
    name = models.CharField(max_length=30)
    car_brand = models.ForeignKey(CarBrand, related_name='brand_models', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['created_at']


class UserCar(SoftDeleteModel):
    car_brand = models.ForeignKey(CarBrand, on_delete=models.CASCADE)
    car_model = models.CharField(max_length=20)
    first_reg = models.DateField()
    odometer = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(UserModel, related_name='user_cars', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.first_reg.year) + '' + str(self.car_brand) + '' + str(self.car_model)

    class Meta:
        ordering = ['created_at']

