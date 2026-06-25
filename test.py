import os
import requests
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("COHERE_API_KEY")

headers = {
    "Authorization": f"Bearer {api_key}"
}

response = requests.get(
    "https://api.cohere.com/v1/models",
    headers=headers
)

print("Status:", response.status_code)
print(response.text)