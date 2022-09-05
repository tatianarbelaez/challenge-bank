import json
import requests

for day in range(1, 32):
    day_string = str(day)
    result_string = requests.get('https://api.tvmaze.com/schedule/web?date=2020-12-' + day_string).text
    with open('json/json_data_' + day_string + '.json', 'w') as outfile:
       json.dump(result_string, outfile)

