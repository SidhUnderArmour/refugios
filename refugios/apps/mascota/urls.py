from django.urls import re_path
from refugios.apps.mascota.views import index, mascota_view

urlpatterns = [
    re_path(r'^', index, name ="index"),
    re_path(r'^nuevo/', mascota_view, name ="mascota_crear"),
]
