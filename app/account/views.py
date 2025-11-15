from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action

# Example ViewSet - customize based on your models
class AccountViewSet(viewsets.ModelViewSet):
    """
    Example ViewSet for Account model.
    Replace with your actual model and serializer.
    """
    # queryset = Account.objects.all()
    # serializer_class = AccountSerializer
    
    def list(self, request):
        return Response({"message": "Account list endpoint"})
    
    def retrieve(self, request, pk=None):
        return Response({"message": f"Account detail for id: {pk}"})
    
    @action(detail=True, methods=['get'])
    def custom_action(self, request, pk=None):
        return Response({"message": f"Custom action for account {pk}"})
