# Multi Agent System approach for Real Time Data Analysis 
# Work Done By - [BadriNarayanan S (2348507)]

# This agentic system will not appear like a regular pipelines that we will do in machine learning. Here the total importance is given to automate each and every tasks. That is the importance of agents. I learnt about developing multi agent systems, so I implemented it. It is a different way of analysing data. And it is the current trend in AI industries.

# Importing Necessary Libraries

from crewai import Agent # For creating agents
from dotenv import load_dotenv # For detecting environment variables
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_groq import ChatGroq # Inference engine
import os # For env
from tools import tool # To interact with the real world environment

load_dotenv() # For env

# Detecting Environment Variables

os.environ['GOOGLE_API_KEY'] = os.getenv('GOOGLE_API_KEY')
os.environ['GROQ_API_KEY'] = os.getenv('GROQ_API_KEY')

# Instancing LLMs from Groq Cloud

# groqllm = ChatGroq(model="llama3-70b-8192", verbose=True, temperature=0)
# groqllm = ChatGroq(model="llama-3.1-70b-versatile", verbose=True, temperature=0)
# groqllm = ChatGroq(model="llama3-8b-8192", verbose=True, temperature=0)
# groqllm = ChatGroq(model="gemma2-9b-it", verbose=True, temperature=0)
groqllm = ChatGroq(model="mixtral-8x7b-32768", verbose=True, temperature=0)

# Developing Multiple Agents for the Analysis

# Data Collection Agent

# This agent is responsible to collect the real time data from reddit social media.

data_collector = Agent(
    role="Social Media Data Collector",
    goal="Scrape real-time data from reddit about {topic}.",
    memory= True,
    llm=groqllm,
    backstory= "You're a data scraper collecting real-time social media information from reddit.",
    tools=[tool],
    allow_delegation=False
    
)

# Preprocessing Agent 

# This agent is responsible to preprocess the real time dataset that is obtained by the previous agent. Making it suitable for the model to give the proper results.

preprocessor = Agent(
    role="Data Preprocessor",
    goal="Clean and preprocess the scraped social media data for analysis.",
    backstory="You're a meticulous preprocessor ensuring the data is ready for analysis.",
    llm=groqllm,
    memory=True,
    allow_delegation=False
)

# Model Analysis Agent 

# This agent is responsible to analyze the llm model performance.

analyzer = Agent(
    role="Model Analyzer",
    goal="Apply the LLM model that is given to you to the preprocessed data and evaluate the performance on {topic}.",
    backstory="You're an analytical expert evaluating the performance of the given LLM.",
    memory=True,
    llm=groqllm,
    allow_delegation=False
)

# Conclusion - Developed multiple agents to carry out the workflow and to automate each tasks.
