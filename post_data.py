import requests

# res = requests.post("http://127.0.0.1:5000/formularz", json={"klucz": "wartość", "kolucz2": 123})
#print(res.content)


res = requests.get("http://127.0.0.1:5000/formularz", json={"klucz": "wartość", "kolucz2": 123})
print(res.text)