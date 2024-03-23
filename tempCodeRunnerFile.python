import requests

api_key = '4ae9400a1eda4f14b3e7227f24b74b44'

url = 'https://apimdev.wakefern.com/mockexample/V1/getItemDetails'
headers = {'Ocp-Apim-Subscription-Key': '{key}'.format(key=api_key)}

jsonData = requests.get(url, headers=headers).json()
print(jsonData)