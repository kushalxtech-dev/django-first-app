from django.urls import path, include
from rest_framework.routers import DefaultRouter
from hub.router import router
from . import views

# Register viewsets with the common router
router.register(r'accounts', views.AccountViewSet, basename='account')

urlpatterns = [
    path('', include(router.urls)),
]

