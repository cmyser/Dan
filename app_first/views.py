from django.shortcuts import render

# Create your views here.
from typing import Type, List

from django.shortcuts import render

# Create your views here.
from django.db.models import Q
from rest_framework.permissions import IsAuthenticated

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions

from django.contrib.auth.models import User

from app_first.models import Adress
from app_first.serializers import AdressSerializers


class Adresses(APIView):
    """Комнаты чата"""
    # permission_classes: List[Type[IsAuthenticated]] = [permissions.IsAuthenticated, ]

    def get(self, request):
        adds = Adress.objects.all()
        serializer = AdressSerializers(adds, many=True)
        return Response({"adds": serializer.data})

    def post(self, request):
        Adress.objects.create(adres=request.adres)
        return Response(status=201)