import requests
import json
from pprint import pprint

API_KEY = '2619421814940190'
heroes = ['Hulk', 'Captain America', 'Thanos']
intelligence_score = {}

def find_hero_id():
    for hero in heroes:
        response = requests.get(f'https://superheroapi.com/api/{API_KEY}/search/{hero}')
        # print(response.url)
        hero_intelligence = response.json()['results'][0]['powerstats']['intelligence']
        print(f'Интеллект {hero} - {hero_intelligence}')
        intelligence_score[hero] = int(hero_intelligence)

    print(intelligence_score)

    max_intelligence_score = max(intelligence_score, key=intelligence_score.get)
    print(f'Максимальный балл интеллекта у {max_intelligence_score} - {intelligence_score[max_intelligence_score]}')

