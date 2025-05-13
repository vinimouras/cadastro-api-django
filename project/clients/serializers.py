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

    def validate_cep(self, data):
        cep = data.get("cep")
        if cep:
            response = requests.get(f'https://viacep.com.br/ws/{cep}/json/')
            if response.status_code == 200:
                cep_data = response.json()
                data['street'] = cep_data.get('logradouro', '')
                data['neighborhood'] = cep_data.get('bairro', '')
                data['city'] = cep_data.get('localidade', '')
                data['uf'] = cep_data.get('uf', '')
        return data


    def create(self, validated_data):
        return Clients.objects.create(**validated_data)