from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from mess_app.models import Mess
from mess_app.serializers import MessSerializer

class MessViewSet(viewsets.ModelViewSet):
    queryset = Mess.objects.all()
    serializer_class = MessSerializer
    permission_classes = [IsAuthenticated]