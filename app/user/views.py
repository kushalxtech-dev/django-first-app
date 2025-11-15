from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action

# Example ViewSet - customize based on your models
class UserViewSet(viewsets.ModelViewSet):
    """
    Example ViewSet for User model.
    Replace with your actual model and serializer.
    """
    # queryset = User.objects.all()
    # serializer_class = UserSerializer
    
    def list(self, request):
        return Response({"message": "User list endpoint"})
    
    def retrieve(self, request, pk=None):
        return Response({"message": f"User detail for id: {pk}"})
    
    @action(detail=True, methods=['get'])
    def custom_action(self, request, pk=None):
        return Response({"message": f"Custom action for user {pk}"})
