from crewai import Agent
from textwrap import dedent


class AiFlightsAgents:
    def __init__(self, llm) -> None:
        self.llm = llm

    def flights_criteria_agent(self):
        return Agent(
            role="Flight Preferences Extractor",
            goal="Identify and extract flight preferences from a user description.",
            backstory=dedent(
                "You are a specialist in extracting information from user descriptions. "
                "Your task is to read descriptions and accurately identify the user's flight preferences."
            ),
            verbose=True,
            llm=self.llm,
        )

    def flights_agent(self):
        return Agent(
            role="Flights Selector",
            goal="Conduct a comprehensive research on the available flights",
            backstory=dedent(
                """You are a researcher specialist that search flights and choose the best one"""
            ),
            verbose=True,
            llm=self.llm,
        )

    def flight_json(self):
        return Agent(
            role="Data Processor",
            goal="Process flight data and save it as a valid JSON file without backticks.",
            backstory="You specialize in efficiently handling and processing JSON data, ensuring all invalid characters are removed, "
            "the structure includes a top-level object named 'flight,' and the output is suitable for HTTP requests. That means I shouldn't get your comments on the result return only the json result",
            verbose=True,
            memory=False,
            llm=self.llm,
        )


class AiRestaurantsAgents:
    def __init__(self, llm) -> None:
        self.llm = llm

    def restaurants_criteria_agent(self):
        return Agent(
            role="Dining Preferences Extractor",
            goal="Identify and extract user preferences for dining, including cuisine types and dietary restrictions, from descriptions.",
            backstory=dedent(
                "You are a specialist in extracting dining preferences from user descriptions. "
                "Your task is to read these descriptions and accurately identify the user's restaurant choices, preferred cuisines, and any dietary restrictions."
            ),
            verbose=True,
            llm=self.llm,
        )

    def restaurants_agent(self):
        return Agent(
            role="Restaurants Selector",
            goal="Conduct a comprehensive research on the available restaurants and dining options",
            backstory=dedent(
                """You are a researcher specialist that search restaurants and choose the best one"""
            ),
            verbose=True,
            llm=self.llm,
        )

    def restaurants_json(self):
        return Agent(
            role="Data Processor",
            goal="Process restaurants data and save it as a valid JSON file without backticks.",
            backstory="You specialize in efficiently handling and processing JSON data, ensuring all invalid characters are removed, "
            "the structure includes a top-level object named 'restaurants,' and the output is suitable for HTTP requests. That means I shouldn't get your comments on the result return only the json result",
            verbose=True,
            memory=False,
            llm=self.llm,
        )


class AiActivitiesAgents:
    def __init__(self, llm) -> None:
        self.llm = llm

    def activities_criteria_agent(self):
        return Agent(
            role="Activities Preferences Extractor",
            goal="Identify and extract user preferences for activities from description.",
            backstory=dedent(
                "You are a specialist in extracting activities preferences from user descriptions. "
                "Your task is to read these descriptions and accurately identify the user's activities preferences."
            ),
            verbose=True,
            llm=self.llm,
        )

    def activities_agent(self):
        return Agent(
            role="Activities Selector",
            goal="Conduct a comprehensive research on the available activities options",
            backstory=dedent(
                """You are a researcher specialist that search activities and choose the best one"""
            ),
            verbose=True,
            llm=self.llm,
        )

    def activities_json(self):
        return Agent(
            role="Data Processor",
            goal="Process activities data and save it as a valid JSON file without backticks.",
            backstory="You specialize in efficiently handling and processing JSON data, ensuring all invalid characters are removed, "
            "the structure includes a top-level object named 'activities,' and the output is suitable for HTTP requests. That means I shouldn't get your comments on the result return only the json result",
            verbose=True,
            memory=False,
            llm=self.llm,
        )
