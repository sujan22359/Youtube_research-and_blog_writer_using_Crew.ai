from crewai import Agent
from tools import youtube_search_tool, youtube_channel_tool
from dotenv import load_dotenv

load_dotenv()

import os
# Set up environment variables for CrewAI to use Gemini
os.environ["GOOGLE_API_KEY"] = os.getenv("GEMINI_API_KEY")

## Create a senior blog content researcher

blog_researcher=Agent(
    role='Blog Researcher from Youtube Videos',
    goal='Research and extract relevant information from YouTube videos based on the given topic',
    verbose=True,
    backstory=(
       "Expert in finding and analyzing YouTube videos across various topics including technology, business, education, and trending subjects. Specializes in extracting valuable insights from video content and identifying key information for blog writing." 
    ),
    llm='gemini/gemini-1.5-flash',  # Use Gemini model directly
    allow_delegation=True,
    tools=[youtube_search_tool, youtube_channel_tool]  # Enable YouTube tools for video research
)

## creating a senior blog writer agent with YT tool

blog_writer=Agent(
    role='Blog Writer',
    goal='Create compelling and engaging blog content based on research findings about the given topic',
    verbose=True,
    backstory=(
        "With a flair for simplifying complex topics, you craft "
        "engaging narratives that captivate and educate readers. You excel at "
        "transforming research insights into accessible, well-structured blog posts "
        "that resonate with diverse audiences across various subjects and industries."
    ),
    llm='gemini/gemini-1.5-flash',  # Use Gemini model directly
    allow_delegation=False
)