from rest_framework import serializers
from .models import dipendente, lavoratore, lavoro, esperienza, backup_person

# serialaizers si usa per tornare un jason response con i dati e questo dobbiamo fare per tutti i classi
class dipendenteSerializer (serializers.ModelSerializer):
    class Meta:
        model = dipendente
        fields = '__all__'

class lavoratoreSerializer (serializers.ModelSerializer):
    class Meta:
        model = lavoratore
        fields = '__all__'

class lavoroSerializer (serializers.ModelSerializer):
    class Meta:
        model = lavoro
        fields = '__all__'
    
class esperienzaSerializer (serializers.ModelSerializer):
    class Meta:
        model = esperienza
        fields = '__all__'

class backup_personSerializer (serializers.ModelSerializer):
    class Meta:
        model = backup_person
        fields = '__all__'