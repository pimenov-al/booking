from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class ApiUser(AbstractUser): #создали модель юзера, наследуемся от готового класса питона
    ...


class Hotel(models.Model): #создали модель юзера, тоже наследуемся от готового класса питона
    name = models.CharField(max_length=128)


class Room(models.Model):   #класс "комната"
    num = models.PositiveIntegerField() #номер комнаты, будет >0 и не пустой
    # делаем связь с классом Хотел через внешний ключ
    hotel = models.ForeignKey(Hotel, related_name="rooms", on_delete=models.CASCADE)


class Booking(models.Model): #класс Бронирование
    room = models.ForeignKey(Room, related_name="bookings", on_delete=models.CASCADE)
    user = models.ForeignKey(ApiUser, related_name="bookings", on_delete=models.CASCADE)
