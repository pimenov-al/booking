# from django.shortcuts import render
from rest_framework import viewsets

from api.models import ApiUser
from api.serializers import UserSerializer


# т.н. вьюха)) - класс или функ, кот обрабатывает запросы пользователя

# Create your views here.

class UserModelViewSet(viewsets.ModelViewSet):
    # UserModelViewSet наследуется от ModelViewSet
    queryset = ApiUser.objects.all() # показываем всех юзеров
    http_method_names = ['post', 'path', 'get'] # другие методы тут не пишем,
                            # чтоб никто через api не удалил например наших юзеров
    serializer_class = UserSerializer # теперь логига сериалайзера будет тут исп-ся