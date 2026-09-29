from django.apps import AppConfig


class MyappConfig(AppConfig):
    name = 'myapp'
    default_auto_field = "django_mongodb_backend.fields.ObjectIdAutoField"
