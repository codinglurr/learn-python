import requests

r = requests.get("https://api.kawalcorona.com/indonesia")

json = r.json()
data = json[0]

print("Nama \t : " + data['name'])
print("Positif\t : " + data['positif'])
print("Meninggal: " + data['meninggal'])
print("Sembuh \t : " + data['sembuh'])
