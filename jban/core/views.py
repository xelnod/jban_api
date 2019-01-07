from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from core.models import Build, User
from core.serializers import BuildSerializer, UserRegisterSerializer


class BuildViewSet(ModelViewSet):
    serializer_class = BuildSerializer
    queryset = Build.objects.all()


class RegisterView(generics.CreateAPIView):
    serializer_class = UserRegisterSerializer
    queryset = User.objects.all()

    def post(self, request, *args, **kwargs):
        result = super().post(request, *args, **kwargs)
        login(self.request, User.objects.get(id=result.data['id']))
        return result
