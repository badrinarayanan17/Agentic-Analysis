# Defining tasks for all the agents
# Tasks will define the agents purpose on the environment

from crewai import Task # For defining task
from agents import data_collector, preprocessor, analyzer # Calling Agents
from tools import tool # Real world environment

# DataCollection Task
# Here we defined the tasks for data collection agent

datacollection_task = Task(
    description=("Scrape real-time data from reddit{topic}."
    "Ensure the data is relevant and covers various perspectives on the topic."),
    expected_output ="A dataset of comments {topic}.",
    tools=[tool],
    agent=data_collector
)

# Preprocessor Task
# Here we defined the tasks for preprocessing agent

preprocessor_task = Task(
    description=("Preprocess the scraped social media data from by cleaning, normalizing, and transforming it as needed."
    "Focus on making the data ready for model analysis."),
    expected_output = "A clean, preprocessed dataset ready for analysis.",
    agent=preprocessor
)

# Analyzer Task
# Here we defined the tasks for analyzing agent

analyzer_task = Task(
    description=("Evaluate the given LLM model to the preprocessed data and compare their performance."
    "Focus on metrics like sentiment analysis accuracy, precision, recall, F1 score, and others as applicable."),
    expected_output = 'A evaluation of the model performances with insights and conclusions.',
    agent=analyzer,
    async_execution = False,
    output_file = 'model_results2.md'
)

# This analyzer agent will gives us a output of the llm model evaluation of the particular dataset that we scraped out from reddit. We can see the sentiment analysis accuracy, precision, recall, f1 score and others. The is generated in a markdown format.

# Conclusion - Each tasks serves the purpose of the each agents. It is helping us to map the functionality of a particular agent. Like this after defining agents we will be defining tasks for every agents. 