from django.shortcuts import render
from rest_framework import viewsets
from titanic.models import Titanic
from titanic.serializers import TitanicSerializer, UserSerializer
from titanic import TiML
from rest_framework.response import Response
from django.contrib.auth.models import User

# Create your views here.

class TitanicViewSet(viewsets.ModelViewSet):
    queryset = Titanic.objects.all().order_by('-id')
    serializer_class = TitanicSerializer
    def create(self, request, *args, **kwargs):
        super(viewsets.ModelViewSet, self).create(request, *args, **kwargs)
        ob = Titanic.objects.latest('id')
        y = TiML.pred(ob)
        return Response({"status": "Success", "Survived": y, 'tmp': args})  # Your override


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-id')
    serializer_class = UserSerializer
