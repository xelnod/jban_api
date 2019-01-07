from django.contrib.auth import authenticate
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from core.models import Build
from core.serializers import BuildSerializer


def get_self(request):
    if request.user.is_authenticated:
        username = request.user.username
    else:
        username = 'ХЗ кто'
    return JsonResponse({"username": username})


class BuildViewSet(ModelViewSet):
    serializer_class = BuildSerializer
    queryset = Build.objects.all()
