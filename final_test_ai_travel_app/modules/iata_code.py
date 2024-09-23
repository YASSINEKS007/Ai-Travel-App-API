import requests
from final_test_ai_travel_app.modules.access_token import get_access_token


def get_geocode_and_iata(city: str):
    
    token = get_access_token()
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(
        f"https://test.api.amadeus.com/v1/reference-data/locations/cities?keyword={city}&max=1",
        headers=headers,
    )

    res = response.json()
    data = res["data"][0]
    return {
        "iataCode": data["iataCode"],
        "latitude": data["geoCode"]["latitude"],
        "longitude": data["geoCode"]["longitude"],
    }