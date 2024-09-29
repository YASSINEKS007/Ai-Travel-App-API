import requests
from final_test_ai_travel_app.modules.access_token import get_access_token
from final_test_ai_travel_app.modules.iata_code import get_geocode_and_iata
from pprint import pprint


def get_activities(city: str):
    geocode_data = get_geocode_and_iata(city=city)
    latitude, longitude = geocode_data['latitude'], geocode_data['longitude']

    token = get_access_token()
    headers = {"Authorization": f"Bearer {token}"}

    url = f"https://test.api.amadeus.com/v1/shopping/activities?latitude={
        latitude}&longitude={longitude}&radius=10000"
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        raise Exception(f"Error: Received status code {response.status_code}")

    result = response.json()

    if 'data' not in result:
        raise Exception("Error: 'data' key not found in response")

    activities = []

    for res in result['data']:
        description = res.get('description') or res.get('shortDescription')
        pictures = res.get('pictures', [])

        if description and pictures:
            data = {
                "name": res.get("name", "Unknown Activity"),
                "description": description.split('.')[0] + "." if description else "No description available.",
                "picture": pictures[0] if pictures else "No picture available",
            }
            activities.append(data)

    return activities

pprint(get_activities(city="PARIS"))