
from django.contrib.auth.models import User
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import viewsets, generics, filters
from rest_framework import permissions
from rest_framework.permissions import AllowAny


from accounts.models import Profile
from accounts.serializers import UserSerializer, ProfileSerializer, RegisterSerializer
from cars.permissions import IsOwnerOrReadOnly


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter, DjangoFilterBackend]
    filter_fields = ('username', )
    search_fields = ('^username', )
    ordering_fields = ('username', )


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all().order_by('user_id')
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter, DjangoFilterBackend]
    filter_fields = ('first_name', 'last_name', 'age', 'gender', 'user')
    search_fields = ('^first_name', '^last_name', '^user__username',)
    ordering_fields = ('first_name', 'last_name', 'age', 'gender', 'user')

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer
