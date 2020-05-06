from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Livro, Emprestimo

'''
SERIALIZERS PADRÕES DO DJANGO REST FRAMEWORK PARA GERENCIAMENTO DE USUÁRIOS
'''
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


#Serializer dos sistema
class LivroSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Livro
        lookup_field = 'id'
        fields = ['id', 'titulo', 'autor', 'edicao', 'quantidade']

class EmprestimoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Emprestimo
        livro = serializers.PrimaryKeyRelatedField(queryset=Livro.objects.all())
        lookup_field = 'id'
        fields = ['id', 'nome', 'telefone', 'livro', 'data_emprestimo', 'data_devolucao']