import requests

url = 'https://api-auth-vini.up.railway.app/'


coletar = requests.get(url=url)

print(coletar.json())

item_modificar = 2
url_modificar = f'{url}produtos/{item_modificar}'

alterar = requests.put(url= url_modificar)

