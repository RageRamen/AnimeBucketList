import requests
import random

response = requests.get('https://raw.githubusercontent.com/jikan-me/jikan-rest/master/storage/api-docs/api-docs.json')
print(response.status_code)

# List of Anime to watch/re-watch
animeList = ["Naruto", "Bleach", "One Piece", "Jujutsu Kaisen", "My Hero Academia", "Demon Slayer"]

# Gives random anime to watch
print(random.choice(animeList))