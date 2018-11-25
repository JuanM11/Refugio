from rest_framework import serializers
from .models import Tipo, Mascota, Adoptante

class TipoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tipo
        fields = ('__all__')

class MascotaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Mascota
        fields = ('__all__')
    
class AdoptanteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Adoptante
        fields = ('__all__')