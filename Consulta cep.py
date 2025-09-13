import requests

def consulta_cep(cep):
    response = requests.get(f'https://viacep.com.br/ws/{cep}/json/')
    data = response.json()
    if 'erro' not in data:
        print('CEP: ', data['cep'])
        print('Logradouro: ', data['logradouro'])
        print('Complemento: ', data['complemento'])
        print('Bairro: ', data['bairro'])
        print('Localidade: ', data['localidade'])
        print('UF: ', data['uf'])
        print('IBGE: ', data['ibge'])
        print('GIA: ', data['gia'])
    else:
        print('CEP inválido')

consulta_cep('')  
