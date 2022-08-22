from django.contrib import admin
from .models import dipendente, lavoratore, lavoro, esperienza, backup_person

# Register your models here.

admin.site.register(dipendente)
admin.site.register(lavoratore)
admin.site.register(lavoro)
admin.site.register(esperienza)
admin.site.register(backup_person)
