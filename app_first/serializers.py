from rest_framework import serializers
from django.contrib.auth.models import User

from app_first.models import Adress


class AdressSerializers(serializers.ModelSerializer):
    """Сериализация adresa """
    adres = serializers.CharField(max_length=150)
    number_phon = serializers.CharField(max_length=150)
    x_re = serializers.FloatField(default=0)
    y_re = serializers.FloatField(default=0)
    start = serializers.CharField(max_length=150)
    stop = serializers.CharField(max_length=150)
    idi = serializers.IntegerField(default=0)

    class Meta:
        model = Adress
        fields = ("adres", "number_phon", "x_re", "y_re", "start", "stop", "idi")
