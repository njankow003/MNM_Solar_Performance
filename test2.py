import requests
import json

response_API = requests.get('https://data.covid19india.org/state_district_wise.json')
#print(response_API.status_code)