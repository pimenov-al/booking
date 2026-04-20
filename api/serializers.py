# совет гугла как исправить ошибку
# django.core.exceptions.ImproperlyConfigured: Requested setting INSTALLED_APPS, but settings are not configured. You must either define the environment variable DJANGO_SETTINGS_MODULE or call settings.configure() before accessing settings.
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'booking.settings')
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'your_project_name.settings')
django.setup()

# Now you can import your models and other Django modules
# from myapp.models import MyModel

# конец кода по испр ошибки---------------------

# создали сериалайзер
from rest_framework import serializers # импортировали базовую логику
from rest_framework import validators # импортировали валидатор

from api.models import ApiUser, Hotel, Room, Booking


# делаем сериализатор для билдера
# способ 1 - все пишем руками как в этом классе
# способ 2 - проще и быстрее как в классе Хотел, работает только с простыми данными
class UserSerializer(serializers.Serializer):
    # сначала напишем какие поля будем отдавать и получать от фронта
    # что будем сериализовать и десериализовать
    username = serializers.CharField(max_length=128, validators=[
        # проверяем что создаем уникального юзера
        validators.UniqueValidator(ApiUser.objects.all()) #все юзеры д.б. уникальные
    ])
    email = serializers.EmailField(validators=[
        # проверяем что емейл уникальный
        validators.UniqueValidator(ApiUser.objects.all())
    ])
    password = serializers.CharField(min_length=6, max_length=20, write_only=True)
    # flag write_only -  что нам не нужно забирать пароль


    def update(self, instance, validated_data):
        # здесь надо писать логику обновления юзера
        if email := validated_data.get("email"):
            instance.email = email
            instance.save(update_fields=["email"])
        if password := validated_data.get("password"):
            instance.set_password(password)
            instance.save(update_fields=["password"])
        return instance

    def create(self, validated_data):
        # здесь надо писать логику создания юзера
        user = ApiUser.objects.create(
            email=validated_data["email"],
            username=validated_data["username"],

        )
        #т.к. пароль будет зашифрованный, его обрабатываем отдельно
        user.set_password(validated_data["password"])
        user.save(update_fields=["password"]) #отдельно сохр поле псрд, чтоб оптимальнее
        return user


class HotelSerializer(serializers.ModelSerializer): #наследуемся от др класса ModelSerializer
    # сделаем одной строкой
    class Meta:
        model = Hotel
        # fields = ["name"] # можно перечислить поля
        fields = "__all__" # или сразу все взять
        # id отеля устанавлиает БД, мы его не знаем, оно только для чтения,
        # мы не ожидаем его от клиента
        extra_kwargs = {"id": {"read_only": True}}

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = "__all__"
        extra_kwargs = {"id": {"read_only": True}}

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = "__all__"
        extra_kwargs = {"id": {"read_only": True}}
