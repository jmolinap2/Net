from urllib.request import urlopen 
import json
url='https://www.omdbapi.com/?i=tt3896198&apikey=634e1136'

response=urlopen(url)
data=json.loads(response.read())

dic=dict()
dic["Peliculas"]=[]
dic["Fecha"]=[]
pelis=[]

print(data)
for i in data:
    print(i)
    
    
       
    break
