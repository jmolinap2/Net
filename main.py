from urllib.request import urlopen 
import json

url="https://api.jikan.moe/v4/top/anime"
response=urlopen(url)
data=json.loads(response.read())

for e in data['data']:
        print(e['title'])
        
