# Defining tools to interact with the real world
# This will helps us to communicate with the external world
# Serper Dev Tool - It will revolve around the google indexes and wikipedia articles to collect real time data and to give a proper response.

from crewai_tools import SerperDevTool # For interaction with real world
import os # For env
from dotenv import load_dotenv # For detecting env

load_dotenv()

os.environ['SERPER_API_KEY'] = os.getenv("SERPER_API_KEY") # Invoking SERPER API KEY 

tool = SerperDevTool() # Calling the tool

# Conclusion = Here I used serper dev tool to scrape the real time data, according to our requirements we can use the tool. crewAI has a lot of tools and langchain tools can also be integrated with crewAI framework. This is the main advantage.



