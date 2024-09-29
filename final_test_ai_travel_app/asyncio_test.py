import asyncio
from final_test_ai_travel_app.activities_crew import activities_crew
from final_test_ai_travel_app.flights_crew import flights_crew
from final_test_ai_travel_app.restaurants_crew import restaurants_crew


def execute_crews(
    criteria: str,
    city_origin: str,
    city_destination: str,
    departure_date: str,
    return_date: str,
    adults: int
):
    llm: str = "ollama/llama3.1"
    flights_crew_result = flights_crew(
        llm=llm, criteria=criteria, city_origin=city_origin,
        city_destination=city_destination, departure_date=departure_date,
        return_date=return_date, adults=adults).kickoff()

    activities_crew_result = activities_crew(
        llm=llm, criteria=criteria, destination_city=city_destination).kickoff()

    restaurants_crew_result = restaurants_crew(
        llm=llm, criteria=criteria, destination_city=city_destination).kickoff()

    # These are now synchronous calls, so we don't need asyncio.gather()
    print("Flights Crew Result:", flights_crew_result)
    print("Activities Crew Result:", activities_crew_result)
    print("Restaurants Crew Result:", restaurants_crew_result)


print(execute_crews())
