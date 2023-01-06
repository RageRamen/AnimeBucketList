import requests
from collections import namedtuple
import json
import random


def get_animedata(title):
    # Connection to Jikan API
    response = requests.get('https://api.jikan.moe/v4/anime', params={'limit': 1, 'letter': title})
    print("Status code: ", response.status_code)

    # Load json string
    data = response.json()

    # Information saved
    #for x in data['data']:
    #    title = x['title']
    #    score = x['score']
    #    season = x['season']
    #    year = x['year']
    #    image_url = x['images']['webp']['image_url']
    #    print(x['url'], x['title'], x['score'], x['season'], x['year'], x['images']['webp']['image_url'])

    return data

def print_anime(title):
    # Connection to Jikan API
    response = requests.get('https://api.jikan.moe/v4/anime', params={'limit': 5, 'letter': title})
    print("Status code: ", response.status_code)

    # Load json string
    data = response.json()
    for x in data['data']:
        print(x['url'], x['title'], x['score'], x['season'], x['year'], x['images']['webp']['image_url'])


def print_anime_popularity():
    # Connection to Jikan API
    response = requests.get('https://api.jikan.moe/v4/anime', params={'limit': 5, 'letter': 'Bleach'})
    print("Status code: ", response.status_code)

    # Load json string
    data = response.json()
    for x in data['data']:
        print(x['url'], x['title'])
    # print(data['data']) #this is a list in a list

    # Create json string
    new_json = json.dumps(data, indent=4, sort_keys=True)
    # print(new_json)


def print_random_anime():
    # Connection to Jikan API
    response = requests.get('https://api.jikan.moe/v4/random/anime')
    print("Status code: ", response.status_code)

    # Load json string
    data = response.json()
    print(data['data'])

    # Create json string
    new_json = json.dumps(data, indent=4, sort_keys=True)
    # print(new_json)

# List of Anime to watch/re-watch
# animeList = ["Naruto", "Bleach", "One Piece", "Jujutsu Kaisen", "My Hero Academia", "Demon Slayer"]

# Gives random anime to watch
# print(random.choice(animeList))

# print_random_anime()
# print_anime_popularity()
