from django_filters import DateFromToRangeFilter, RangeFilter
from django_filters.rest_framework import FilterSet

from cars.models import UserCar


class UserCarFilter(FilterSet):
    first_reg = DateFromToRangeFilter()
    odometer = RangeFilter()

    class Meta:
        model = UserCar
        fields = ['first_reg', 'odometer', 'car_brand', 'car_model', 'user']

