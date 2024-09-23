import requests
import os

def get_access_token():
    data = {
        "grant_type": os.getenv("grant_type"),
        "client_id": os.getenv("client_id"),
        "client_secret": os.getenv("client_secret"),
    }
    headers = {"Content-Type": "application/x-www-form-urlencoded"}

    response = requests.post(
        "https://test.api.amadeus.com/v1/security/oauth2/token",
        data=data,
        headers=headers,
    )

    res = response.json()
    return res.get("access_token")

