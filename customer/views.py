from django.http import JsonResponse
from rest_framework import permissions, status
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from customer.models import Customer, CustomerInteraction
from customer.serializers import CustomerSerializer, CustomerInteractionSerializer


class CustomerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows customer to be viewed or edited.
    """
    queryset = Customer.objects.all().order_by('-created_at')
    serializer_class = CustomerSerializer
    permission_classes = [permissions.IsAuthenticated]
    filterset_fields = ['email', 'first_name']

    def get_serializer_context(self):
        return {"request": self.request}

    @action(methods=["GET"], detail=True)
    def interactions(self, request, pk):
        customer = self.get_object()
        interactions = customer.get_interactions()
        data = CustomerInteractionSerializer(interactions, many=True).data
        return Response(data=data, status=status.HTTP_200_OK)


class CustomerInteractionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows customer interactions to be created.
    """
    queryset = CustomerInteraction.objects.all().order_by('-created_at')
    serializer_class = CustomerInteractionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_context(self):
        return {"request": self.request}