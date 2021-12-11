from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from expense_app.models import CostCategory, MessEventNCostCategoryNUserCost
from expense_app.serializers import CostCategorySerializer, MessEventNCostCategoryNUserCostSerializer

class CostCategoryViewSet(viewsets.ModelViewSet):
    queryset = CostCategory.objects.all()
    serializer_class = CostCategorySerializer
    permission_classes = [IsAuthenticated]

class MessEventNCostCategoryNUserCostViewSet(viewsets.ModelViewSet):
    queryset = MessEventNCostCategoryNUserCost.objects.all()
    serializer_class = MessEventNCostCategoryNUserCostSerializer
    permission_classes = [IsAuthenticated]