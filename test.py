import requests
import json

url = 'https://api.stackexchange.com/2.2/search?order=desc&sort=activity&intitle=perl&site=stackoverflow'

data = requests.get(url)
if data.status_code == 200:
	data = data.json()
	for e in data['items']:
			print(e['title'])
			print(e['is_answered'])
			print(e['view_count'])
			print(e['answer_count'])
			print(e['last_activity_date'])


			