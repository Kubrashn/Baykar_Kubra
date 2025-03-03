from rest_framework import serializers
from .models import *

class ParcaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parca  
        fields = '__all__'  


class UcakSerializer(serializers.ModelSerializer):
    eksik_parcalar = serializers.SerializerMethodField()

    def get_eksik_parcalar(self, obj):
        gerekli_parcalar = {'Kanat', 'Gövde', 'Kuyruk', 'Aviyonik'}
        mevcut_parcalar = set(obj.parcalar.values_list('parca_adi', flat=True))
        eksikler = gerekli_parcalar - mevcut_parcalar
        return list(eksikler) if eksikler else "Tamamlandı"
    
    class Meta:
        model = Ucak
        fields = '__all__'


class TakimSerializer(serializers.ModelSerializer):
    class Meta:
        model = Takim
        fields = '__all__'