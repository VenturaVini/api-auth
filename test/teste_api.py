import requests

# URL do endpoint
url_get = "https://api-auth-vini.up.railway.app/"
url_post = "https://api-auth-vini.up.railway.app/produtos/"

# Token JWT gerado no /auth/login

token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ2aW5pIiwiZXhwIjoxNzM5NTA3MzkxfQ.tMgCWsi57w3bcGVoa7zdl79f3-Q9Pb1eXcngrRxV-Qc"  # Substitua pelo token gerado
token = 'Bearer ' + token

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
    "nome": "Drew",
    "descricao": "Drewwwwwwwwwwwwwwwwwwww",
    "preco": 105483484.76,
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
