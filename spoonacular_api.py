import requests
import os
from os.path import join, dirname
from dotenv import load_dotenv
import json

dotenv_path = join(dirname(__file__), 'spoonacular.env')
load_dotenv(dotenv_path)

spoonacular_key = os.environ['SPOONACULAR_KEY']
url = "https://api.spoonacular.com/recipes/search?apiKey={}".format(spoonacular_key)

response = requests.get(url)
json_body = response.json()
#print((json_body))
# print(json_body["results"][0])
# print(json_body["results"][0]["title"])

print(json.dumps(json_body["results"][0], indent=2))
# print(json_body["results"][0])
print(json_body["results"][0]["title"])


