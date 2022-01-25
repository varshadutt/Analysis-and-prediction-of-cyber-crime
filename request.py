import requests

url = 'http://localhost:5000/results'
r = requests.post(url,json={'Rate of Total Cyber Crimes':3.3 , 'YEAR 2020':200, 'YEAR 2021':400})

print(r.json())