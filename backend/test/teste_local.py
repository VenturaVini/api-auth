import requests


<<<<<<< HEAD
url = 'http://localhost:7200'


requisicao = requests.get(url)
# print(requisicao.json())


def pegar_token(usuario, senha):
    url = 'http://localhost:7200/auth/login'
=======
url = 'http://localhost:7324'


requisicao = requests.get(url)
print(requisicao.json())


def pegar_token(usuario, senha):
    url = 'http://localhost:7324/auth/login'
>>>>>>> 7d14a31494c02b0fba424bfb6e11d352e0a8c0e1
    payload = {
        'username': usuario,
        'senha': senha
    }
    requisicao = requests.post(url, json=payload)
    return requisicao.json()


<<<<<<< HEAD
token = pegar_token('vini', '12')['access_token']
print(token)

# url_post = url + '/produtos/'

# payload = {
#     'id': 3,
#     'nome': 'Iphone 15 128GB',
#     'descricao': 'teste',
#     'preco': 4499.99,
#     'estoque': 17,
# }
=======
token = pegar_token('vini', '123')['access_token']

url_post = url + '/produtos/'

payload = {
    'id': 3,
    'nome': 'Iphone 15 128GB',
    'descricao': 'teste',
    'preco': 4499.99,
    'estoque': 17,
}
>>>>>>> 7d14a31494c02b0fba424bfb6e11d352e0a8c0e1

headers = {
    'Authorization': f'Bearer {token}',
    'Content-Type': 'application/json'
}

<<<<<<< HEAD
# requisicao_post = requests.post(url_post, json=payload, headers=headers)
# print(requisicao_post.json())


requisicao = requests.get(url)
# print(requisicao.json())

url_modificar = f'{url}/produtos/2'

deletar = requests.delete(url= url_modificar, headers= headers )
if deletar.status_code == 200:
    try:
        print(deletar.json())
    except ValueError as e:
        print("Erro ao decodificar JSON:", e)
        print("Conteúdo da resposta:", deletar.text)
else:
    print(f"Erro na requisição: {deletar.status_code}")
    print("Conteúdo da resposta:", deletar.text)


coletar = requests.get(url=url)

print(coletar.json())
=======
requisicao_post = requests.post(url_post, json=payload, headers=headers)
print(requisicao_post.json())


requisicao = requests.get(url)
print(requisicao.json())

>>>>>>> 7d14a31494c02b0fba424bfb6e11d352e0a8c0e1
