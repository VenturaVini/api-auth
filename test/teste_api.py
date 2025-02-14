import requests

# URL do endpoint
url_get = "http://localhost:7000/"
url_post = "http://localhost:7000/produtos/"

# Token JWT gerado no /auth/login
token = "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ2aW5pIiwiZXhwIjoxNzM5NTA2Mjg4fQ.IwfIJF6WpzhJ4vrR_8wRv73_patPGaHeJHpRAiutsDw"  # Substitua pelo token gerado

# Cabeçalhos da requisição
headers = {
    "Content-Type": "application/json",
    "Authorization": token
}

# ========== 1. Fazer o GET para listar os produtos ==========
print("\n=== Fazendo GET para listar produtos ===")
response_get = requests.get(url_get)
print(f"Status Code: {response_get.status_code}")
print("Response JSON:", response_get.json())

# ========== 2. Fazer o POST para adicionar um novo produto ==========
produto = {
    "id": 3,
    "nome": "xbox",
    "descricao": "novo",
    "preco": 1,
    "estoque": 1
}

print("\n=== Fazendo POST para adicionar produto ===")
response_post = requests.post(url_post, json=produto, headers=headers)
print(f"Status Code: {response_post.status_code}")
print("Response JSON:", response_post.json())

# ========== 3. Fazer o GET novamente para verificar se foi adicionado ==========
print("\n=== Fazendo GET novamente para verificar o produto ===")
response_get_novo = requests.get(url_get)
print(f"Status Code: {response_get_novo.status_code}")
print("Response JSON:", response_get_novo.json())
