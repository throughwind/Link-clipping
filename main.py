import requests
import os
import argparse
from dotenv import load_dotenv
from urllib.parse import urlparse


REQUEST_URL = "https://api-ssl.bitly.com/v4/bitlinks"


def shorten_link(input_url, headers):
    body = {
        "long_url": input_url
    }
    response = requests.post(REQUEST_URL, headers=headers, json=body)
    response.raise_for_status()
    bitlink = response.json()["link"]

    return bitlink


def count_clicks(input_url, headers):
    bitlink_pars = urlparse(input_url)
    count_url = f"{REQUEST_URL}/{bitlink_pars.netloc}{bitlink_pars.path}/clicks/summary"
    params = {
        "unit": "day",
        "units": -1
    }
    response = requests.get(count_url, headers=headers, params=params)
    response.raise_for_status()
    clicks_count = response.json()["total_clicks"]

    return clicks_count


def is_bitlink(input_url, headers):
    parsed_url = urlparse(input_url)
    some_url = f"{REQUEST_URL}/{parsed_url.netloc}{parsed_url.path}"
    response = requests.get(some_url, headers=headers)

    return response.ok


if __name__ == '__main__':
    load_dotenv()
    parser = argparse.ArgumentParser()
    parser.add_argument("input_url", nargs='?')
    args = parser.parse_args()
    input_url = args.input_url
    token = os.getenv("BITLY_TOKEN")
    headers = {
        "Authorization": f"Bearer {token}"
    }
    try:
        if is_bitlink(input_url, headers):
            print(f"Counts: {count_clicks(input_url, headers)}")
        else:
            print(f"Your billink: {shorten_link(input_url, headers)}")
    except requests.exceptions.HTTPError:
        print("Input error")
