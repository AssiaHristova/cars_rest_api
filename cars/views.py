
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import permissions, viewsets, filters

from cars.filters import UserCarFilter
from cars.models import CarBrand, CarModel, UserCar
from cars.permissions import IsOwnerOrReadOnly
from cars.serializers import CarBrandSerializer, CarModelSerializer, UserCarSerializer


class CarBrandViewSet(viewsets.ModelViewSet):
    queryset = CarBrand.objects.all()
    serializer_class = CarBrandSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter, DjangoFilterBackend]
    filter_fields = ('name', 'user')
    search_fields = ('^name', 'user__username')
    ordering_fields = ('name', 'user')

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CarModelViewSet(viewsets.ModelViewSet):
    queryset = CarModel.objects.all()
    serializer_class = CarModelSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter, DjangoFilterBackend]
    filter_fields = ('name', 'car_brand')
    search_fields = ('^name', 'car_brand__name')
    ordering_fields = ('name', 'car_brand')


class UserCarViewSet(viewsets.ModelViewSet):
    queryset = UserCar.objects.all()
    serializer_class = UserCarSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter, DjangoFilterBackend]
    filterset_class = UserCarFilter
    search_fields = ('car_brand__name', 'car_model', 'user__username')
    ordering_fields = ('car_brand', 'car_model', 'first_reg', 'odometer', 'user')

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
