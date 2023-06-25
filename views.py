from django.shortcuts import render
from nimean.models import jadwalModels
from rest_framework.response import Response
from nimean.serializers import jadwalSerializer
from rest_framework import viewsets


# rest_framework
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
class jadwalViews(viewsets.ModelViewSet):
    queryset = jadwalModels.objects.all()
    serializer_class = jadwalSerializer
