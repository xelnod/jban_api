from rest_framework.serializers import ModelSerializer

from core.models import Build


class BuildSerializer(ModelSerializer):
    class Meta:
        model = Build
        fields = '__all__'
