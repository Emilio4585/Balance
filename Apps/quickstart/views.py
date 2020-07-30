from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from Apps.quickstart.serializers import UserSerializer, GroupSerializer
from .models import Usuario


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class UsuarioViewSet(viewsets.ModelViewSet):
    """

    """
    queryset = Usuario.objects.all()
    serializer_class = Usuario
