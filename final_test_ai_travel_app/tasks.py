from crewai import Task, Agent
from textwrap import dedent
from final_test_ai_travel_app.modules.flights import get_flights_by_city
from final_test_ai_travel_app.modules.restaurants import get_restaurants_by_city
from final_test_ai_travel_app.modules.activities import get_activities


class AiFlightsTasks:
    def __init__(self) -> None:
        pass

    def extract_flights_criteria_task(self, criteria: str, agent: Agent):
        return Task(
            description=dedent(
                f"""
                You will receive a text representing the user's preferences for a travel plan, which will be used to generate their plan. 
                Your task is to extract the section of the preferences related to flight options.

                Criteria: {criteria}.

                If no specific flight preferences are mentioned, return: "the best possible".
                And make the response as short as possible.
                """
            ),
            expected_output=dedent(
                "A summary of the user's flight preferences in text format."
            ),
            agent=agent,
        )

    def flights_task(
        self,
        city_origin: str,
        city_destination: str,
        departure_date: str,
        return_date: str,
        adults: int,
        agent: Agent,
    ):

        flights = get_flights_by_city(
            city_origin=city_origin,
            city_destination=city_destination,
            departure_date=departure_date,
            return_date=return_date,
            adults=adults,
        )

        return Task(
            description=dedent(
                f"""
                You will be give a list of available flights in json format from a location to a destination, I want you to select one based on the criteria described here.
                the list of flights in json format : {flights}.
                And in your response return only one flight json object and no need for comments.
            """
            ),
            expected_output="The json object representing the selected flight",
            agent=agent,
        )

    def save_flight_json(self, agent: Agent):
        return Task(
            description=(
                "Process the flight selection task and save the flight data as a JSON file named 'flight.json.' "
                "The JSON structure must include a top-level object called 'flight' containing the relevant flight data. "
                "Ensure that the output is a strictly valid JSON object, with no comments or extra formatting. "
                "Your response should consist solely of the JSON data, without backticks or any other annotations. "
                "The final output must be in plain JSON format to facilitate saving in a JSON file."
            ),
            expected_output=dedent(
                """A strictly valid JSON object with a top-level key 'flight' containing flight task data. example :
            {
                "flight": [
                    {
                    "oneWay": false,
                    "lastTicketingDate": "2024-09-23",
                    "duration": "PT5H30M",
                    "price": "215.02",
                    "currency": "EUR"
                    }
                ]
                }"""
            ),
            output_file="flight.json",
            agent=agent,
            async_execution=False,
        )


class AiRestaurnatsTasks:
    def __init__(self) -> None:
        pass

    def extract_restaurants_criteria_task(self, criteria: str, agent: Agent):
        return Task(
            description=dedent(
                f"""
                You will receive a text representing the user's preferences for a travel plan, which will be used to generate their plan. 
                Your task is to extract the section of the preferences related to restaurants and dining options.

                Criteria: {criteria}.

                If no specific flight preferences are mentioned, return: "the best possible".
                And make the response as short as possible.
                """
            ),
            expected_output=dedent(
                "A summary of the user's restaurants and dining preferences in text format."
            ),
            agent=agent,
        )

    def restaurants_task(self, city: str, agent: Agent):

        restaurants = get_restaurants_by_city(city=city)

        return Task(
            description=dedent(
                f"""
                You will be give a list of available restaurnats in json format, I want you to select one based on the criteria described here.
                the list of restaurants in json format : {restaurants}.
                And in your response return only the three selected restaurants in a json object list and no need for comments.
            """
            ),
            expected_output="The json object representing the selected restaurants",
            agent=agent,
        )

    def save_restaurants_json(self, agent: Agent):
        return Task(
            description=(
                "Process the restaurants selection task and save the restaurants data as a JSON file named 'restaurants.json.' "
                "The JSON structure must include a top-level object called 'restaurants' containing the relevant restaurants data. "
                "Ensure that the output is a strictly valid JSON object, with no comments or extra formatting. "
                "Your response should consist solely of the JSON data, without backticks or any other annotations. "
                "The final output must be in plain JSON format to facilitate saving in a JSON file."
            ),
            expected_output=dedent(
                "A strictly valid JSON object with a top-level key 'restaurants' containing restaurants task data"
            ),
            output_file="restaurants.json",
            agent=agent,
            async_execution=False,
        )


class AiActivitiesTasks:
    def __init__(self) -> None:
        pass

    def extract_activities_criteria_task(self, criteria: str, agent: Agent):
        return Task(
            description=dedent(
                f"""
            You will receive a user's preferences for a travel plan. Your task is to extract the section of these preferences specifically related to travel activities (e.g., sightseeing, outdoor activities, cultural experiences).

            Criteria: {criteria}.

            If no specific activity preferences are mentioned, return: "No specific preferences, suggest popular or recommended activities."

            Keep the response concise and focused only on the relevant activity preferences.
            """
            ),
            expected_output=dedent(
                "A concise summary of the user's activity preferences."
            ),
            agent=agent,
        )

    def activities_task(self, city: str, agent: Agent, trip_days : int):

        activities = get_activities(city=city)

        return Task(
            description=dedent(
                f"""
            You will be given a list of available travel activities in JSON format. Select {trip_days} activities based on the criteria provided.
            The list of activities in JSON format: {activities}.
            In your response, return only the {trip_days} selected activities in a JSON object list, with no comments.
            """
            ),
            expected_output="A JSON object representing the selected activities",
            agent=agent,
            
        )

    def save_activities_json(self, agent: Agent):
        return Task(
            description=(
                "Process the activities selection task and save the activities data as a JSON file named 'activities.json.' "
                "The JSON structure must include a top-level object called 'activities' containing the relevant activities data. "
                "Ensure that the output is a strictly valid JSON object, with no comments or extra formatting. "
                "Your response should consist solely of the JSON data, without backticks or any other annotations. "
                "The final output must be in plain JSON format to facilitate saving in a JSON file."
            ),
            expected_output=dedent(
                "A strictly valid JSON object with a top-level key 'activities' containing the activities task data"
            ),
            output_file="activities.json",
            agent=agent,
            async_execution=False,
        )
