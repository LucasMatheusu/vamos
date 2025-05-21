import requests
requisiçao = requests.get('https://teste-4c935-default-rtdb.firebaseio.com/.json')
print(requisiçao)
print(requisiçao.json())
print(requisiçao.json())
import requests
informação = '{"Nome": "guil", "sobrenome": "candiotto", "idade": "23"}'
requisiçao = requests.patch('https://teste-4c935-default-rtdb.firebaseio.com/-OD6vAbJCKFM.json', data=informação)
print(requisiçao)
print(requisiçao.json())
import requests

requesiçao = requests.delete('https://teste-4c935-default-rtdb.firebaseio.com/-OD6vAbJCKFMOwgu6nYY.json')
print(requesiçao)
print(requesiçao.json())