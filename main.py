import requests
import os
import json
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.environ.get("BitlyToken")
REQUEST_URL = "https://api-ssl.bitly.com/v4/bitlinks"
LONG_URL = input("Enter your link: ")


def shorten_link(TOKEN, LONG_URL):
    body = {
        "long_url": LONG_URL
    }
    headers = {
        "Authorization": f"Bearer {TOKEN}"
    }

    response = requests.post(REQUEST_URL, headers=headers, json=body)
    response.raise_for_status()

    bitlink = json.loads(response.text)["link"]

    return bitlink


try:
    bitlink = shorten_link(TOKEN, LONG_URL)
    print('Битлинк', bitlink)
except requests.exceptions.HTTPError:
    print("ERROR")
