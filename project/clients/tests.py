import requests


def buscar_endereco(cep):
    url = f"https://viacep.com.br/ws/{cep}/json/"
    response = requests.get(url)

    if response.status_code == 200:
        dados = response.json()
        if 'erro' in dados:
            return "CEP inválido"
        return {
            "rua": dados.get("logradouro"),
            "bairro": dados.get("bairro"),
            "cidade": dados.get("localidade"),
            "uf": dados.get("uf")
        }
    else:
        return "Erro na requisição"


# Teste
cep_teste = "01001000"
resultado = buscar_endereco(cep_teste)
print(resultado)