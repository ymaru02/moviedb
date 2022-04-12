from rest_framework import serializers
from django.contrib.auth import get_user_model


User = get_user_model()


# 회원가입 과정(유효성 검사!) 중에 사용할 친구!
class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ('username', 'password', )
