from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from mess_app.models import Mess, MessEvent, MessNUser
from mess_app.serializers import MessEventSerializer, MessSerializer, MessNUserSerializer

class MessViewSet(viewsets.ModelViewSet):
    queryset = Mess.objects.all()
    serializer_class = MessSerializer
    permission_classes = [IsAuthenticated]

class MessNUserViewSet(viewsets.ModelViewSet):
    queryset = MessNUser.objects.all()
    serializer_class = MessNUserSerializer
    permission_classes = [IsAuthenticated]
    filterset_fields = ['mess', 'user']

class MessEventViewSet(viewsets.ModelViewSet):
    queryset = MessEvent.objects.all()
    serializer_class = MessEventSerializer
    permission_classes = [IsAuthenticated]