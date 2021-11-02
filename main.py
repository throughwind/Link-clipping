import requests
import os
import json
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.environ.get("BitlyToken")
REQUEST_URL = "https://api-ssl.bitly.com/v4/bitlinks"
INPUT_URL = input("Enter your link: ")


def shorten_link(TOKEN, INPUT_URL):
    body = {
        "long_url": INPUT_URL
    }
    headers = {
        "Authorization": f"Bearer {TOKEN}"
    }

    response = requests.post(REQUEST_URL, headers=headers, json=body)
    response.raise_for_status()

    bitlink = json.loads(response.text)["link"]

    return bitlink


def count_clicks(TOKEN, INPUT_URL):
    count_url = f"{REQUEST_URL}/{INPUT_URL}/clicks/summary"
    headers = {
        "Authorization": f"Bearer {TOKEN}"
    }
    params = {
        "unit": "day",
        "units": -1
    }
    response = requests.get(count_url, headers=headers, params=params)
    response.raise_for_status()

    clicks_count = json.loads(response.text)["total_clicks"]

    return clicks_count


try:
    clicks_count = count_clicks(TOKEN, INPUT_URL)
    print("Clicks", clicks_count)
    #bitlink = shorten_link(TOKEN, INPUT_URL)
    #print('Your bitlink', bitlink)
except requests.exceptions.HTTPError:
    print("ERROR")

#print(count_clicks(TOKEN, INPUT_URL))
