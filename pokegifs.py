import json
import requests 
import dotenv 
import os 

dotenv.load_dotenv() 

giphy_key = os.environ.get('GIPHY_API_KEY')
res = requests.get("http://pokeapi.co/api/v2/pokemon/pikachu/")
body = json.loads(res.content)
print(body["name"])
print(body["types"])
print(body["id"])

res_gif = requests.get(f"https://api.giphy.com/v1/gifs/search?api_key={giphy_key}&q=pikachu&rating=g")
print(res_gif)
print(res_gif.json().keys())
