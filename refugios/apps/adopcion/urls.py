from django.urls import re_path
from refugios.apps.adopcion.views import index

urlpatterns = [
    re_path(r'^', index, name ="index"),
    ]