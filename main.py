import requests
import os
from dotenv import load_dotenv


load_dotenv()
TOKEN = os.environ.get("BitlyToken")
headers = {
    "Authorization": f"Bearer {TOKEN}"
}
url = "https://api-ssl.bitly.com/v4/user"
response = requests.get(url, headers=headers)
response.raise_for_status()

print(response.text)
