
from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import UserSerializer, GroupSerializer, LivroSerializer, EmprestimoSerializer
from .models import Livro, Emprestimo
from rest_framework.decorators import action
from rest_framework import mixins
from rest_framework import generics
'''
VIEWS PADRÕES DO DJANGO REST FRAMEWORK PARA GERENCIAMENTO DE USUÁRIOS
'''


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

class LivroViewSet(mixins.CreateModelMixin, mixins.ListModelMixin, generics.RetrieveUpdateDestroyAPIView, viewsets.GenericViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Livro.objects.all()
    lookup_field = 'id'
    serializer_class = LivroSerializer
    permission_classes = [permissions.IsAuthenticated]
    # @action(detail=True, methods=['PUT'])
    # def update

class EmprestimoViewSet(mixins.CreateModelMixin, mixins.ListModelMixin, generics.RetrieveUpdateDestroyAPIView, viewsets.GenericViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Emprestimo.objects.all()
    serializer_class = EmprestimoSerializer
    permission_classes = [permissions.IsAuthenticated]