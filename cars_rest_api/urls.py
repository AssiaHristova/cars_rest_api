
from django.urls import include, path
from rest_framework import routers
from accounts.views import UserViewSet, ProfileViewSet
from accounts.views import RegisterView
from cars import views

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'profiles', ProfileViewSet)
router.register(r'car-brands', views.CarBrandViewSet)
router.register(r'car-models', views.CarModelViewSet)
router.register(r'cars', views.UserCarViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('register/', RegisterView.as_view(), name='register'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

]

