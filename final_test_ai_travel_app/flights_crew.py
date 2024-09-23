from crewai import Crew, Process
from final_test_ai_travel_app.agents import AiFlightsAgents
from final_test_ai_travel_app.tasks import AiFlightsTasks
import json


def remove_markdown_syntax(json_string):
    # Remove backticks and any leading/trailing whitespace
    cleaned_json = json_string.strip().replace("```", "").replace("json", "").strip()
    return cleaned_json


llm = "ollama/mistral"

agents = AiFlightsAgents(llm=llm)
tasks = AiFlightsTasks()

flights_preferences_extractor_agent = agents.flights_criteria_agent()
flights_preferences_extractor_task = tasks.extract_flights_criteria_task(
    criteria="I love flights that don't take much time to arrive to destination. I love indian food.",
    agent=flights_preferences_extractor_agent,
)

flights_agent = agents.flights_agent()
flights_task = tasks.flights_task(
    agent=flights_agent,
    city_origin="PARIS",
    city_destination="LONDON",
    departure_date="2024-09-24",
    return_date="2024-09-30",
    adults=1,
)

flight_json_data_agent = agents.flight_json()
flight_json_data_task = tasks.save_flight_json(agent=flight_json_data_agent)

crew = Crew(
    agents=[flights_preferences_extractor_agent, flights_agent, flight_json_data_agent],
    tasks=[flights_preferences_extractor_task, flights_task, flight_json_data_task],
    process=Process.sequential,
)

result = crew.kickoff()

print("*********    start    ********")
print(str(result))
print("*********    end      **********")
