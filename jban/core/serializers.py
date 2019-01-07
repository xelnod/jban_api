from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework.serializers import ModelSerializer
from rest_framework.validators import UniqueValidator

from core.models import Build, User


class UserDetailsSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'preferred_class')


class BuildSerializer(ModelSerializer):
    class Meta:
        model = Build
        fields = '__all__'


class UserRegisterSerializer(ModelSerializer):
    username = serializers.CharField(validators=[UniqueValidator(User.objects.all())])
    password = serializers.CharField()
    preferred_class = serializers.CharField()

    def validate(self, attrs):
        if attrs.get('password') != self.context['request'].data.pop('password2'):
            raise ValidationError({'password2': 'Passwords mismatch'})
        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            preferred_class=validated_data['preferred_class']
        )
        user.set_password(validated_data['password'])
        user.save()

        return user

    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'preferred_class')
