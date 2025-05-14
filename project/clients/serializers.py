import requests
from .models import Clients
from rest_framework import serializers
from validate_docbr import CPF

class ClientsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clients
        fields = '__all__'

    def validate_cpf(self, value):
        cpf = CPF()

        if not cpf.validate(value):
            raise serializers.ValidationError("CPF inválido")
        return value

    def create(self, validated_data):
        cep = validated_data.get("cep")
        if cep:
            response = requests.get(f'https://viacep.com.br/ws/{cep}/json/')
            if response.status_code == 200:
                cep_data = response.json()
                validated_data['street'] = cep_data.get('logradouro', '')
                validated_data['neighborhood'] = cep_data.get('bairro', '')
                validated_data['city'] = cep_data.get('localidade', '')
                validated_data['uf'] = cep_data.get('uf', '')
        return Clients.objects.create(**validated_data)