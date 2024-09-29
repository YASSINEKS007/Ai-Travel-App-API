# import asyncio
# from crewai import Agent, Task, Crew, Process
# from crewai_tools import SerperDevTool

# # Set up the tool (example)
# search_tool = SerperDevTool()

# # Define agents for the first crew
# agent1 = Agent(
#     role='Data Collector for Crew 1',
#     goal='Gather information about {topic}',
#     verbose=True,
#     tools=[search_tool]
# )

# # Define agents for the second crew
# agent2 = Agent(
#     role='Data Collector for Crew 2',
#     goal='Research information about {topic}',
#     verbose=True,
#     tools=[search_tool]
# )

# # Define sequential tasks for Crew 1
# task1_crew1 = Task(
#     description="Task 1 for Crew 1: Collect initial data.",
#     expected_output='Data from Task 1 of Crew 1',
#     tools=[search_tool],
#     agent=agent1,
#     async_execution=False  # Ensuring task runs sequentially within the crew
# )

# task2_crew1 = Task(
#     description="Task 2 for Crew 1: Analyze the collected data.",
#     expected_output='Analysis from Task 2 of Crew 1',
#     tools=[search_tool],
#     agent=agent1,
#     async_execution=False  # Runs after Task 1 in the same crew
# )

# # Define sequential tasks for Crew 2
# task1_crew2 = Task(
#     description="Task 1 for Crew 2: Gather information.",
#     expected_output='Data from Task 1 of Crew 2',
#     tools=[search_tool],
#     agent=agent2,
#     async_execution=False  # Ensuring task runs sequentially within the crew
# )

# task2_crew2 = Task(
#     description="Task 2 for Crew 2: Process the gathered information.",
#     expected_output='Processed data from Task 2 of Crew 2',
#     tools=[search_tool],
#     agent=agent2,
#     async_execution=False  # Runs after Task 1 in the same crew
# )

# # Create two crews with sequential tasks
# crew1 = Crew(
#     agents=[agent1],
#     tasks=[task1_crew1, task2_crew1],
#     process=Process.sequential  # Sequential task execution within the crew
# )

# crew2 = Crew(
#     agents=[agent2],
#     tasks=[task1_crew2, task2_crew2],
#     process=Process.sequential  # Sequential task execution within the crew
# )

# # Define an async function to run both crews concurrently
# async def run_crews_concurrently():
#     # Kickoff both crews concurrently
#     result1 = asyncio.create_task(crew1.kickoff(inputs={'topic': 'AI trends in healthcare'}))
#     result2 = asyncio.create_task(crew2.kickoff(inputs={'topic': 'AI trends in education'}))

#     # Await the results from both crews
#     results = await asyncio.gather(result1, result2)

#     # Print the results
#     print("Crew 1 Result:", results[0])
#     print("Crew 2 Result:", results[1])

# # Run the crews concurrently while keeping tasks sequential
# asyncio.run(run_crews_concurrently())


import json

data = json.loads("../restaurants.json")
print(data)