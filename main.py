import requests
import os
import json
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.environ.get("BitlyToken")
REQUEST_URL = "https://api-ssl.bitly.com/v4/bitlinks"


def shorten_link(TOKEN, LONG_URL):
    body = {
        "long_url": LONG_URL
    }
    headers = {
        "Authorization": f"Bearer {TOKEN}"
    }

    response = requests.post(REQUEST_URL, headers=headers, json=body)
    response.raise_for_status()

    date_response = json.loads(response.text)

    return date_response["link"]


if __name__ == "__main__":
    LONG_URL = input("Enter your link: ")
    print('Битлинк', shorten_link(TOKEN, LONG_URL))
