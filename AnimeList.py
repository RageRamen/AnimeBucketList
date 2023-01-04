import requests
from collections import namedtuple
import json
import random

# Connection to Jikan API
response = requests.get('https://api.jikan.moe/v4/random/anime')
print("Status code: ", response.status_code)

# Convert into json
data = response.json()
print(data['data']['url'])



# List of Anime to watch/re-watch
#animeList = ["Naruto", "Bleach", "One Piece", "Jujutsu Kaisen", "My Hero Academia", "Demon Slayer"]

# Gives random anime to watch
#print(random.choice(animeList))