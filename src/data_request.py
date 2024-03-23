import requests
from pprint import pprint
import pymysql


# Create cursor and connection
con = pymysql.connect(host = 'localhost', 
                      user = 'root', 
                      passwd = '2232')
cursor = con.cursor()


api_key = '4ae9400a1eda4f14b3e7227f24b74b44'

url = 'https://apimdev.wakefern.com/mockexample/V1/getStoreDetails'
headers = {'Ocp-Apim-Subscription-Key': '{key}'.format(key=api_key),
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'}

jsonData = requests.get(url, headers=headers).json()

f = open("stores.json", "a")
print(jsonData, file=f)
f.close()

#for item in jsonData:
#    sql = "INSERT INTO transactions (id, column2, ...) VALUES (%s, %s, ...)"
#    values = (item['value1'], item['value2'], ...)
#    cursor.execute(sql, values)

# Commit changes and close connection
#con.commit()

# Close cursor and connection
cursor.close()
con.close()