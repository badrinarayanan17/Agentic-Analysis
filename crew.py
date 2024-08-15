# Meshing up agents, tasks, and tools like a crew
# Crew - A group of peoples in real time right, the same applicable here.

from crewai import Crew,Process # Importing required functionality
from agents import data_collector,preprocessor,analyzer # Calling agents
from tasks import datacollection_task,preprocessor_task,analyzer_task # Calling tasks

crew = Crew(
    agents=[data_collector,preprocessor,analyzer],
    tasks=[datacollection_task,preprocessor_task,analyzer_task],
    process=Process.sequential, # To make sure the process between the agentic workflow should be in a sequential manner
)

outcome = crew.kickoff(inputs={'topic':'Olympics 2024'}) # Defining the topic, based on this our agent will scrape the data from a social media, and it will do preprocessing and it will produce the llm model evaluation for the preprocessed dataset.
print(outcome)