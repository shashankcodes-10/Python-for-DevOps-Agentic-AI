import requests
import pprint

url = "https://fake-json-api.mock.beeceptor.com/companies"

reponse = requests.get(url = url)

print(reponse) # this tell our reponse is working fine or not

print(reponse.json()) # this will print the data 

pprint.pprint(reponse.json()) # this will give data in a structured way