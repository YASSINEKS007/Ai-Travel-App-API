from crewai import Crew

from final_test_ai_travel_app.agents import AiActivitiesAgents
from final_test_ai_travel_app.tasks import AiActivitiesTasks

llm = "ollama/mistral"

agents = AiActivitiesAgents(llm=llm)
tasks = AiActivitiesTasks()

activities_criteria_agent = agents.activities_criteria_agent()
extract_activities_criteria_task = tasks.extract_activities_criteria_task(
    criteria="I love fast flights. I love going to parks and museums",
    agent=activities_criteria_agent,
)


activities_agent = agents.activities_agent()
activities_task = tasks.activities_task(
    city="PARIS", agent=activities_agent, trip_days=5
)

activities_json = agents.activities_json()
save_activities_json = tasks.save_activities_json(agent=activities_json)

crew = Crew(
    agents=[activities_criteria_agent, activities_agent, activities_json],
    tasks=[extract_activities_criteria_task, activities_task, save_activities_json],
)

result = crew.kickoff()

print("************* start *****************")
print(str(result))
print("************* end *****************")
