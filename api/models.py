from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class ApiUser(AbstractUser): #создали модель юзера, наследуемся от готового класса питона
    ...


class Hotel(models.Model): #создали модель юзера, тоже наследуемся от готового класса питона
    name = models.CharField(max_length=128)

    # не было до файлового запуска апи сервера
    def __str__(self):
        return f"{self.id}: {self.name}"


class Room(models.Model):   #класс "комната"
    num = models.PositiveIntegerField() #номер комнаты, будет >0 и не пустой
    # делаем связь с классом Хотел через внешний ключ
    hotel = models.ForeignKey(Hotel, related_name="rooms", on_delete=models.CASCADE)

    # не было до файлового запуска апи сервера
    def __str__(self):
        return f"{self.hotel.name}. Room num: {self.num}"

class Booking(models.Model): #класс Бронирование
    room = models.ForeignKey(Room, related_name="bookings", on_delete=models.CASCADE)
    user = models.ForeignKey(ApiUser, related_name="bookings", on_delete=models.CASCADE)

    # не было до файлового запуска апи сервера
    def __str__(self):
        return f"{self.user.username}; {self.room.hotel.name}; {self.room.num}"
