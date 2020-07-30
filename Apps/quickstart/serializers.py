from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Usuario


class UserSerializer(serializers.HyperlinkedModelSerializer):
    db_table = 'User'

    class Meta:
        model = User
        fields = '__all__'


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        db_table = 'Grupo'
        model = Group
        fields = '__all__'


class UsuarioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        db_table = 'Usuario'
        model = Usuario
        fields = '__all__'
