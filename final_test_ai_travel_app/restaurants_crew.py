from crewai import Crew, Process
from final_test_ai_travel_app.agents import AiRestaurantsAgents
from final_test_ai_travel_app.tasks import AiRestaurnatsTasks

llm = "ollama/mistral"


agents = AiRestaurantsAgents(llm=llm)
tasks = AiRestaurnatsTasks()

restaurants_criteria_agent = agents.restaurants_criteria_agent()
extract_restaurants_criteria_task = tasks.extract_restaurants_criteria_task(
    criteria="I love fast flights, and I love fast food",
    agent=restaurants_criteria_agent,
)


restaurants_agent = agents.restaurants_agent()
restaurants_task = tasks.restaurants_task(city="PARIS", agent=restaurants_agent)


restaurants_json = agents.restaurants_json()
save_restaurants_json = tasks.save_restaurants_json(agent=restaurants_json)


crew = Crew(
    agents=[restaurants_criteria_agent, restaurants_agent, restaurants_json],
    tasks=[extract_restaurants_criteria_task, restaurants_task, save_restaurants_json],
    process=Process.sequential,
)

result = crew.kickoff()

print("*************** start *************")
res = str(result)
print(res)
print(type(res))
print("*************** end   *************")
