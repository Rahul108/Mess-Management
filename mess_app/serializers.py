from rest_framework import serializers
from mess_app.models import Mess

class MessSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mess
        fields = '__all__'