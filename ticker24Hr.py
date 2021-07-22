import json

import requests
import pandas as pd

url = "https://api.binance.com/api/v3/ticker/24hr"

payload = {}
headers = {}
proxies = {
    'http': 'http://127.0.0.1:7890',
    'https': 'http://127.0.0.1:7890',
}

response = requests.request("GET", url, headers=headers, data=payload, proxies=proxies)

respBody = json.loads(response.text)
symbols = respBody
df = pd.json_normalize(symbols)


print(df.sort_values(by='count', ascending=False))
