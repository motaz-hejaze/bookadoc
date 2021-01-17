from rest_framework
import serializers
from django.contrib.auth import get_user_model
from django.utils.translation import ugettext_lazy as _

UserModel = get_user_model()

class CustomUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = UserModel
        fields = ('id', 'email', 'password', 'user_type')
        read_only_fields = ('id',)
        write_only_fields = ('password',)
    
    def validate(self, data):
        if not data.get('user_type') or not data.get('email') or not data.get('password'):
            raise serializers.ValidationError(_("Please Provie atleast Email , User Type and Password"))
        return data