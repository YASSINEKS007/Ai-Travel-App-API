import requests
from final_test_ai_travel_app.modules.access_token import get_access_token
from final_test_ai_travel_app.modules.iata_code import get_geocode_and_iata
from pprint import pprint

def get_activities(city: str):
    iataCode, latitude, longitude = get_geocode_and_iata(city=city).values()
    token = get_access_token()
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(
        f"https://test.api.amadeus.com/v1/shopping/activities?latitude={latitude}&longitude={longitude}&radius=1000",
        headers=headers,
    )

    result = response.json()
    activities = []

    for i in range(len(result["data"])):
        res = result["data"][i]
        if (
            res.get("description") is None
            and res.get("shortDescription") is None
            or res.get("pictures", []) == []
        ):

            pass
        else:
            data = {
                "name": res["name"],
                "description": res.get(
                    "description",
                    res.get("shortDescription", "No description available"),
                ),
                "pictures": res["pictures"][0],
            }

            activities.append(data)


    return activities