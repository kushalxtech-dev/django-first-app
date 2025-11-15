from django.urls import include, path
from rest_framework.routers import DefaultRouter
from hub.router import router
from . import views

# Register viewsets with the common router
router.register(r'users', views.UserViewSet, basename='user')

urlpatterns = [
    path('api/', include(router.urls)),
]

