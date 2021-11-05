import requests
import os
from os.path import join, dirname
from dotenv import load_dotenv
from urllib.parse import urlparse


INPUT_URL = input("Enter your link: ")
TOKEN = os.getenv("BITLY_TOKEN")
HEADERS = {
    "Authorization": f"Bearer {TOKEN}"
}
REQUEST_URL = "https://api-ssl.bitly.com/v4/bitlinks"


def shorten_link(INPUT_URL):
    body = {
        "long_url": INPUT_URL
    }
    response = requests.post(REQUEST_URL, headers=HEADERS, json=body)
    response.raise_for_status()
    bitlink = response.json()["link"]

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
    clicks_count = response.json()["total_clicks"]

    return clicks_count


def is_bitlink(INPUT_URL):
    parsed_url = urlparse(INPUT_URL)
    some_url = f"{REQUEST_URL}/{parsed_url.netloc}{parsed_url.path}"
    response = requests.get(some_url, headers=HEADERS)

    return response.ok


if __name__ == '__main__':
    dotenv_path = join(dirname(__file__), '.env')
    load_dotenv(dotenv_path)
    try:
        if is_bitlink(INPUT_URL):
            print(f"Counts: {count_clicks(INPUT_URL)}")
        else:
            print(f"Your billink: {shorten_link(INPUT_URL)}")
    except requests.exceptions.HTTPError:
        print("Input error")
