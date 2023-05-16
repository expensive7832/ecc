from rest_framework import serializers
from .models import User
from django.contrib.auth.hashers import check_password
from rest_framework_simplejwt.tokens import RefreshToken

class userSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    class Meta:
        model = User
        fields = ["first_name", "last_name", "email", "password", "photo"]

class loginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["email", "password"]

    def checkInfo(self, data):

        user = User.objects.filter(email = data['email']).first()

        if user is None:
            return None

        else:
            encrypted_pwd = getattr(user, "password")
            check_pwd = check_password(data['password'], encrypted_pwd)
            
            if check_pwd:
                
                refresh = RefreshToken.for_user(user)

                return {
                    'refresh': str(refresh),
                    'access': str(refresh.access_token),
                }
            
            else:
                return None

        
