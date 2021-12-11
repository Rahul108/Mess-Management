from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from mess_app.models import Mess, MessDuration, MessNUser
from mess_app.serializers import MessDurationSerializer, MessSerializer, MessNUserSerializer

class MessViewSet(viewsets.ModelViewSet):
    queryset = Mess.objects.all()
    serializer_class = MessSerializer
    permission_classes = [IsAuthenticated]

class MessNUserViewSet(viewsets.ModelViewSet):
    queryset = MessNUser.objects.all()
    serializer_class = MessNUserSerializer
    permission_classes = [IsAuthenticated]

class MessDurationViewSet(viewsets.ModelViewSet):
    queryset = MessDuration.objects.all()
    serializer_class = MessDurationSerializer
    permission_classes = [IsAuthenticated]