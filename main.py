import requests
import os
import json
from dotenv import load_dotenv


load_dotenv()
TOKEN = os.environ.get("BitlyToken")
LONG_URL = os.environ.get("LongURL")

body = {
    "long_url": LONG_URL
}
headers = {
    "Authorization": f"Bearer {TOKEN}"
}

url = "https://api-ssl.bitly.com/v4/bitlinks"
response = requests.post(url, headers=headers, json=body)
response.raise_for_status()

date_response = json.loads(response.text)

print(date_response["link"])
