from django.contrib import admin

# Register your models here.
from django.contrib import admin

# Register your models here.
from django.contrib import admin
from app_first.models import Adress


class AdressAdmin(admin.ModelAdmin):
    """Комнаты чата"""
    list_display = ("adres", "number_phon")

    # def invited_user(self, obj):
    #     return "\n".join([user.username for user in obj.invited.all()])



admin.site.register(Adress, AdressAdmin)
