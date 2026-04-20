from django.apps import AppConfig


class ApiConfig(AppConfig):
    default_auto_field = 'django.db.BigAutoField' # не было перед фейловым запуском API сервера
    name = "api"
