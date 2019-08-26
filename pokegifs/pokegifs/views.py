
import json
import requests
import os
from random import randint
from django.http import JsonResponse

def pokegif(request, id):
    res = requests.get(f"http://pokeapi.co/api/v2/pokemon/{id}/")
    body = json.loads(res.content)
    name = body["name"] 
    poke_id = body['id']  
    poke_type = []
    for poketype in body['types']:
        poke_type.append(poketype['type']['name'])

    key = os.environ.get("GIPHY_KEY")
    url = "https://api.giphy.com/v1/gifs/search?api_key={}&q={}&rating=g".format(key,name)
    res2 = requests.get(url)
    gif_url = json.loads(res2.content)['data'][0]['url']

    context = {
        'id':poke_id,
        'name':name,
        'types': poke_type,
        'Gif_url': gif_url
    }

    return JsonResponse(context)