from crewai import Crew,Process
from agents import blog_researcher,blog_writer
from tasks import research_task,write_task
from dotenv import load_dotenv
import os
 
load_dotenv()

# Set up environment variables for CrewAI to use Gemini
os.environ["GOOGLE_API_KEY"] = os.getenv("GEMINI_API_KEY")

# Forming the tech-focused crew with Gemini LLM
crew = Crew(
  agents=[blog_researcher, blog_writer],
  tasks=[research_task, write_task],
  process=Process.sequential,
  verbose=True
)

## start the task execution process with enhanced feedback
# You can change the topic to research any subject you want
topic_input = input("Enter the topic you want to research and create a blog about: ")
result=crew.kickoff(inputs={'topic': topic_input})
print(result)
