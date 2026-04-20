# сделаем файл с шаблонами
from django.db import router
from rest_framework.routers import DefaultRouter

from api.views import UserModelViewSet #, HotelModelViewSet, RoomModelViewSet, BookingModelViewSet
from booking.urls import urlpatterns
from django.urls import path, include

router1 = DefaultRouter()
router1.register('users', UserModelViewSet) # здесь регаем эндпоинт
# router.register('hotels', HotelsModelViewSet)
# router.register('rooms', RoomModelViewSet)
# router.register('bookings', BookingModelViewSet)

# в этой переменной будут храниться все шаблоны
# urlpatterns1 = [
#     # path("api-auth/", include("rest_framework.urls"))
# ]



urlpatterns1 = [
    path("", include(router1.urls)),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
]

urlpatterns1.extend(router1.urls)

# urlpatterns = [
#     # ...
#     path("api-auth/", include("rest_framework.urls"))
# ]