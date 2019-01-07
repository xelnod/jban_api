from rest_framework.serializers import ModelSerializer

from core.models import Build, User


class UserDetailsSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'preferred_class')


class BuildSerializer(ModelSerializer):
    class Meta:
        model = Build
        fields = '__all__'
