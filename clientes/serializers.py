from rest_framework import serializers
from clientes.models import Cliente

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'
    
    def validate_cpf(self, cpf): #instanciei e trouxe o CPF.
        if len(cpf) != 11: #Se o tamanho(len) do CPF for != (Não for igual)
            raise serializers.ValidationError('O CPF deve ter 11 dígitos') #Passando o erro que irá utilizar. 
        return cpf 