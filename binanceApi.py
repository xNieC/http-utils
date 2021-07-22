import json

import requests
import pandas as pd

url = "https://api.binance.com/api/v3/exchangeInfo"

payload = {}
headers = {}
proxies = {
    'http': 'http://127.0.0.1:7890',
    'https': 'http://127.0.0.1:7890',
}

response = requests.request("GET", url, headers=headers, data=payload, proxies=proxies)

respBody = json.loads(response.text)
symbols = respBody['symbols']
df = pd.json_normalize(symbols)
df = pd.concat(
    [
        df,
        df.pop("filters").apply(
            lambda x: dict(
                i
                for d in x
                for i in d.items()
                if d["filterType"] in {"MAX_NUM_ORDERS","PRICE_FILTER", "LOT_SIZE"}
            )
        ).apply(pd.Series),
    ],
    axis=1,
).drop(columns="filterType")

print(df)
