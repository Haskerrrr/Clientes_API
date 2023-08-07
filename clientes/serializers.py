from rest_framework import serializers
from clientes.models import Cliente
from clientes.validator import *

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'
    
    def validate(self, data):
        if not cpf_valid(data['cpf']):
            raise serializers.ValidationError({'cpf':'Número de CPF inválido'})

        if not nome_valid(data['nome']):
            raise serializers.ValidationError({'nome':'Não inclua números neste campo'})

        if not rg_valid(data['rg']):
            raise serializers.ValidationError({'rg':'O RG deve ter 9 dígitos'})

        if not celular_valid(data['celular']):
            raise serializers.ValidationError({'celular':'O celular deve seguir esse modelo: 00 0000-0000'})
        return data    
