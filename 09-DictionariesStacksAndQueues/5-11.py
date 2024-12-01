from urllib.request import urlopen
import json

url = urlopen("https://api.nbp.pl/api/exchangerates/rates/A/EUR/last/10/?format=json")
dictionary = json.load(url)

