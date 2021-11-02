import requests
import os
import json
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.environ.get("BitlyToken")
REQUEST_URL = "https://api-ssl.bitly.com/v4/bitlinks"
INPUT_URL = input("Enter your link: ")
HEADERS = {
    "Authorization": f"Bearer {TOKEN}"
}


def shorten_link(TOKEN, INPUT_URL):
    body = {
        "long_url": INPUT_URL
    }
    response = requests.post(REQUEST_URL, headers=HEADERS, json=body)
    response.raise_for_status()

    bitlink = json.loads(response.text)["id"]

    return bitlink


def count_clicks(TOKEN, INPUT_URL):
    count_url = f"{REQUEST_URL}/{INPUT_URL}/clicks/summary"
    params = {
        "unit": "day",
        "units": -1
    }
    response = requests.get(count_url, headers=HEADERS, params=params)
    response.raise_for_status()

    clicks_count = json.loads(response.text)["total_clicks"]

    return clicks_count


def is_bitlink(INPUT_URL):
    if "bit.ly" in INPUT_URL:
        try:
            clicks_count = count_clicks(TOKEN, INPUT_URL)
            print("Clicks", clicks_count)
        except requests.exceptions.HTTPError:
            print("ERROR")
    else:
        try:
            bitlink = shorten_link(TOKEN, INPUT_URL)
            print('Your bitlink:', bitlink)
        except requests.exceptions.HTTPError:
            print("ERROR")

is_bitlink(INPUT_URL)
