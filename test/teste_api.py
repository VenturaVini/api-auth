import requests


separador = '-----------------------------------------------------------------------------------'

url = 'https://api-auth-vini.up.railway.app/'

coletar = requests.get(url=url)

print(coletar.json())


print(separador)


url_modificar = f'{url}produtos/'

token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ2aW5pIiwiZXhwIjoxNzM5NTM1MzgyfQ.UZsnc03AzMQXDriZdv3RXkmP6X1r8eLGM3UX49C1u_A'

# Cabeçalhos
headers = {
    "Content-Type": "application/json",
    "Authorization": token
}

dados = {
    'id' : 2,
    'nome': 'Iphone 15 128gb',
    'descricao': 'Lacrado 128GB 5G',
    'preco': 4500,
    'estoque': 26
}

alterar = requests.put(url= url_modificar, headers= headers, json= dados )

print(alterar.json())


print(separador)


coletar = requests.get(url=url)

print(coletar.json())