from rest_framework import serializers
from mess_app.models import Mess, MessNUser, MessEvent
import secrets

class MessSerializer(serializers.ModelSerializer):

    def __code_generator(self, mess_name):
        code = mess_name[0:5].upper() + str(secrets.SystemRandom().randint(10000, 99999))
        return code

    def __check_unique(self, code, mess_name):
        data = Mess.objects.filter(code=code)
        checked_code = code
        while(len(data) > 0):
            checked_code = self.__code_generator(mess_name)
            data = Mess.objects.filter(code=checked_code)
        return checked_code
                

    def create(self, validated_data):
        new_code = self.__code_generator(validated_data['name'])
        validated_data['code'] = self.__check_unique(new_code, validated_data['name'])
        return super().create(validated_data)
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
