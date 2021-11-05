import requests
import os
import json
from dotenv import load_dotenv
from urllib.parse import urlparse

REQUEST_URL = "https://api-ssl.bitly.com/v4/bitlinks"


def shorten_link(INPUT_URL):
    body = {
        "long_url": INPUT_URL
    }
    response = requests.post(REQUEST_URL, headers=HEADERS, json=body)
    response.raise_for_status()
    bitlink = json.loads(response.text)["link"]

    return bitlink


def count_clicks(INPUT_URL):
    bitlink_pars = urlparse(INPUT_URL)
    count_url = f"{REQUEST_URL}/{bitlink_pars.netloc}{bitlink_pars.path}/clicks/summary"
    params = {
        "unit": "day",
        "units": -1
    }
    response = requests.get(count_url, headers=HEADERS, params=params)
    response.raise_for_status()
    clicks_count = json.loads(response.text)["total_clicks"]

    return clicks_count


def is_bitlink(INPUT_URL):
    url_pars = urlparse(INPUT_URL)
    some_url = f"{REQUEST_URL}/{url_pars.netloc}{url_pars.path}"
    response = requests.get(some_url, headers=HEADERS)

    return response.ok


if __name__ == '__main__':
    INPUT_URL = input("Enter your link: ")
    load_dotenv()
    TOKEN = os.getenv("BitlyToken")
    HEADERS = {
        "Authorization": f"Bearer {TOKEN}"
    }
    try:
        if is_bitlink(INPUT_URL):
            print(f"Counts: {count_clicks(INPUT_URL)}")
        else:
            print(f"Your billink: {shorten_link(INPUT_URL)}")
    except requests.exceptions.HTTPError:
        print("Input error")
