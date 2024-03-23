import requests

api_key = '4ae9400a1eda4f14b3e7227f24b74b44'

url = 'https://apimdev.wakefern.com/mockexample/V1/getItemDetails'
headers = {'Ocp-Apim-Subscription-Key': '{key}'.format(key=api_key),
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'}

jsonData = requests.get(url, headers=headers).json()
print(jsonData)