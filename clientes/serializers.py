from rest_framework import serializers
from clientes.models import Cliente

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'
    
    def validate_cpf(self, cpf): #instanciei e trouxe o CPF
        if len(cpf) != 11: #Se o tamanho(len) do CPF for != (Não for igual)
            raise serializers.ValidationError('O CPF deve ter 11 dígitos') #Passando o erro que irá utilizar. 
        return cpf #Caso tenha 9 dígitos, irá retornar CPF

    def validade_nome(self, nome):
        if not name.isalpha():
            raise serializers.ValidationError('Não inclua números nesse campo')
        return nome

    def validate_rg(self, rg):
        if len(rg) != 9:
            raise serializers.ValidationError('O RG deve ter 9 dígitos')
        return rg 

    def validate_celular(self, celular):
        if len(celular) < 11:
            raise serializers.ValidationError('O celular deve ter 11 dígitos')
        return celular
    
