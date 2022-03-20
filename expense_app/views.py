from rest_framework import viewsets, mixins, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from expense_app.models import CostCategory, MessEventNCostCategoryNUserCost
from expense_app.serializers import CostCategorySerializer, MessEventNCostCategoryNUserCostSerializer, TotalMessCostSerialilzer
from expense_app.services import MessCostPerUserFetchService
from mess_app.models import MessEvent
class CostCategoryViewSet(viewsets.ModelViewSet):
    queryset = CostCategory.objects.all()
    serializer_class = CostCategorySerializer
    permission_classes = [IsAuthenticated]

class MessEventNCostCategoryNUserCostViewSet(viewsets.ModelViewSet):
    queryset = MessEventNCostCategoryNUserCost.objects.all()
    serializer_class = MessEventNCostCategoryNUserCostSerializer
    permission_classes = [IsAuthenticated]

class TotalCostOfMess(viewsets.GenericViewSet, mixins.ListModelMixin):
    queryset = MessEvent.objects.all()

    def get_serializer_class(self):
        if self.action == "list":
            return TotalMessCostSerialilzer
        else:
            raise Exception('Only GET Method Allowed')
        
    def list(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.GET)
        if serializer.is_valid():
            mess_data = MessCostPerUserFetchService.get_users_mess_cost(serializer.validated_data['mess_event_id'].id)
            print(mess_data)
            return Response(data=mess_data)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)