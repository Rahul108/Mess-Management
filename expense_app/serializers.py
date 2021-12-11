from rest_framework import serializers
from expense_app.models import CostCategory, MessEventNCostCategoryNUserCost

class CostCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CostCategory
        fields = '__all__'
    
class MessEventNCostCategoryNUserCostSerializer(serializers.ModelSerializer):
    class Meta:
        model = MessEventNCostCategoryNUserCost
        fields = '__all__'
