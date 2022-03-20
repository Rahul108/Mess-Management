from rest_framework import serializers
from rest_framework.relations import PrimaryKeyRelatedField
from expense_app.models import CostCategory, MessEventNCostCategoryNUserCost, MessEvent

class CostCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CostCategory
        fields = '__all__'
    
class MessEventNCostCategoryNUserCostSerializer(serializers.ModelSerializer):
    class Meta:
        model = MessEventNCostCategoryNUserCost
        fields = '__all__'

class TotalMessCostSerialilzer(serializers.Serializer):
    mess_event_id = PrimaryKeyRelatedField(queryset = MessEvent.objects.all())
