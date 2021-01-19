from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Projects
from .serializers import ProjectSerializer


class ProjectView(ModelViewSet):
    queryset = Projects.objects.all()
    serializer_class = ProjectSerializer