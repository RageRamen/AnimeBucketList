import requests
from collections import namedtuple
import json
import random

def print_anime_popularity():

    # Connection to Jikan API
    response = requests.get('https://api.jikan.moe/v4/anime', params={'letter': 'Bleach'})
    print("Status code: ", response.status_code)

    # Load json string
    data = response.json()
    print(data['data'][0]) #this is a list in a list

    # Create json string
    new_json = json.dumps(data, indent=4, sort_keys=True)
    #print(new_json)


def print_random_anime():
    # Connection to Jikan API
    response = requests.get('https://api.jikan.moe/v4/random/anime')
    print("Status code: ", response.status_code)

    # Load json string
    data = response.json()
    print(data['data'])

    # Create json string
    new_json = json.dumps(data, indent=4, sort_keys=True)
    print(new_json)


# List of Anime to watch/re-watch
# animeList = ["Naruto", "Bleach", "One Piece", "Jujutsu Kaisen", "My Hero Academia", "Demon Slayer"]

# Gives random anime to watch
# print(random.choice(animeList))

#print_random_anime()
print_anime_popularity()