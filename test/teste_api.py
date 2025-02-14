import requests

url = 'https://api-auth-vini.up.railway.app/'


coletar = requests.get(url=url)

print(coletar.json())

item_modificar = 2
url_modificar = f'{url}produtos/{item_modificar}'

token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ2aW5pIiwiZXhwIjoxNzM5NTM0MzMwfQ.IkyrsgBLacsMNiA-76NmP0lmDT6q9BeLE2yWjyckkjI'

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




coletar = requests.get(url=url)

print(coletar.json())