from rest_framework import generics, permissions
from project.models import Project
from project.serializers import ProjectSerializer
from project.Filters import ProjectFilter
from rest_framework.filters import SearchFilter, OrderingFilter

import django_filters


class ProjectList(generics.ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    filter_backends = (SearchFilter, OrderingFilter,django_filters.rest_framework.DjangoFilterBackend)
    filter_class = ProjectFilter
    ordering_fields = ('name')
    search_fields = ('name')
    ordering=('time')

