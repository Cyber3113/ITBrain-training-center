from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from common.permissions import IsCustomerOrAdmin
from app_products.serializers import ProductSerializer
from common.models import ProductModel


class ProductViewSet(viewsets.ModelViewSet):
    queryset = ProductModel.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        user = self.request.user

        if user.role == "superadmin" or user.role == "admin":
            return ProductModel.objects.all() 

        if user.role == "customer":
            return ProductModel.objects.filter(user__company=user.company)  

        return ProductModel.objects.none()
