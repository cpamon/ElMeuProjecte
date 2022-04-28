from django.contrib import admin
from .models import Aplicacio, RefMapaWMS, RefCapa, RefMapa, RefMapaCapa

# Register your models here.
admin.site.register(Aplicacio)
admin.site.register(RefMapaWMS)
admin.site.register(RefCapa)
admin.site.register(RefMapa)
admin.site.register(RefMapaCapa)