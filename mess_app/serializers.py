from rest_framework import serializers
from mess_app.models import Mess, MessNUser, MessEvent

class MessSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mess
        fields = '__all__'

class MessNUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MessNUser
        fields = '__all__'

class MessEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = MessEvent
        fields = '__all__'