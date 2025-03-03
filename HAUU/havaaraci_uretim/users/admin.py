from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *
from main.models import *

class KullaniciAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ('Ekstra Bilgiler', {'fields': ('takim', 'telefon_no', 'tc_no')}),
    )
    list_display = ('username', 'tc_no', 'telefon_no', 'takim', 'is_staff')

admin.site.register(Kullanici, KullaniciAdmin)

