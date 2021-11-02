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


def shorten_link(INPUT_URL):
    body = {
        "long_url": INPUT_URL
    }
    response = requests.post(REQUEST_URL, headers=HEADERS, json=body)
    response.raise_for_status()

    bitlink = json.loads(response.text)["id"]

    return bitlink


def count_clicks(INPUT_URL):
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
        clicks_count = count_clicks(INPUT_URL)
        return f"Clicks: {clicks_count}"
    else:
        bitlink = shorten_link(INPUT_URL)
        return f"Your bitlink: {bitlink}"


def main():
    try:
        is_bitlink(INPUT_URL)
        print(is_bitlink(INPUT_URL))
    except requests.exceptions.HTTPError:
        print("ERROR")


if __name__ == '__main__':
    main()

